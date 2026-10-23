# Mock interview: Low-Level Design

Attempt each prompt before expanding/reading its solution. These are original model answers, not alleged company questions or claimed personal experiences. For behavioral/day-to-day examples, fill the structure with facts from your own work. Banking designs are engineering exercises; actual rail, security and control requirements must be established with the responsible owners.

[All mock rounds](README.md) · [LLD / HLD paths](../lld-hld-learning-path.md)

## 9. Design an ATM

### Interview prompt and example

Alice withdraws 600 units from notes {500:1, 200:3}; greedy 500 first cannot finish, but three 200 notes can.

### Clarify operations and trust

Separate session authentication, account permission, cash inventory, withdrawal orchestration and hardware adapter. The ATM/controller verifies card/PIN through an appropriate secure banking integration; the lab does not handle real PINs or card data. Derive trusted identity at that boundary rather than treating a passed user string as proof.

### Domain and transitions

Model Account/Balance, CashInventory, Withdrawal(requestKey, amount, state) and Dispenser. A real state machine can progress AUTHORIZED → CASH_RESERVED → DISPENSE_REQUESTED → DISPENSED or an explicit UNKNOWN/REVERSED path. Enforce positive amount, limits, funds and an exact feasible denomination plan before decrementing anything.

### Implement the local decision

The Java lab uses bounded-note backtracking because a greedy choice can fail for available denominations. Under one local lock it checks owner, idempotency key/payload and balance, finds a plan, then updates balance and inventory together. A duplicate key returns the prior result; a mismatched amount is rejected.

### Do not confuse local atomicity with dispensing

A physical dispense can succeed while its reply is lost. Persist a durable operation journal and reconcile device counters/sensor events; do not blindly debit again or instantly reverse while the cash outcome is unknown. A database transaction cannot atomically roll back cash already handed out. Network-bank authorization and local cash reservation need a recovery protocol.

### Solution limits and tests

AtmDemo simulates only the local logical decision; it does not operate hardware, persist a ledger or implement banking compliance. It tests non-greedy exact notes, replay, unauthorized subject, conflicting key and no-change failure. Backtracking is exponential in denomination/count choices; bound withdrawal sizes and select an appropriate bounded-change algorithm for a real configuration.

### Java solution

Code is a complete lab where it declares a public class, otherwise a method/type snippet for a Solution class with java.util imports as needed.

```java
import java.util.*;
public class AtmDemo {
 record Withdrawal(long id,int amount,Map<Integer,Integer> notes){Withdrawal{notes=Map.copyOf(notes);}}
 record Attempt(int amount,Withdrawal result){}
 static class Atm {
  private final String owner;private int balance;private final Map<Integer,Integer> cash;private final Map<String,Attempt> done=new HashMap<>();private long sequence;
  Atm(String owner,int balance,Map<Integer,Integer> cash){this.owner=owner;this.balance=balance;this.cash=new HashMap<>(cash);if(balance<0||cash.entrySet().stream().anyMatch(e->e.getKey()<=0||e.getValue()<0))throw new IllegalArgumentException();}
  synchronized Withdrawal withdraw(String authenticatedSubject,String key,int amount){
   if(!owner.equals(authenticatedSubject))throw new SecurityException("not account owner");
   if(key==null||key.isBlank()||amount<=0)throw new IllegalArgumentException();
   Attempt old=done.get(key);if(old!=null){if(old.amount()!=amount)throw new IllegalArgumentException("key payload mismatch");return old.result();}
   if(amount>balance)throw new IllegalStateException("insufficient balance");
   var denominations=cash.keySet().stream().sorted(Comparator.reverseOrder()).toList();Map<Integer,Integer> plan=new HashMap<>();
   if(!plan(denominations,0,amount,plan))throw new IllegalStateException("cannot dispense exact amount");
   balance-=amount;plan.forEach((d,n)->cash.put(d,cash.get(d)-n));
   Withdrawal result=new Withdrawal(++sequence,amount,plan);done.put(key,new Attempt(amount,result));return result;
  }
  private boolean plan(List<Integer> denominations,int index,int remaining,Map<Integer,Integer> result){
   if(remaining==0)return true;if(index==denominations.size())return false;int d=denominations.get(index);
   for(int n=Math.min(cash.get(d),remaining/d);n>=0;n--){if(n==0)result.remove(d);else result.put(d,n);if(plan(denominations,index+1,remaining-n*d,result))return true;}
   result.remove(d);return false;
  }
  synchronized int balance(){return balance;}
 }
 public static void main(String[] args){
  Atm atm=new Atm("alice",1000,Map.of(500,1,200,3));
  Withdrawal w=atm.withdraw("alice","w81",600);if(!w.notes().equals(Map.of(200,3))||atm.balance()!=400)throw new AssertionError();
  if(atm.withdraw("alice","w81",600)!=w||atm.balance()!=400)throw new AssertionError();
  try{atm.withdraw("bob","w82",100);throw new AssertionError();}catch(SecurityException expected){}
  try{atm.withdraw("alice","w81",200);throw new AssertionError();}catch(IllegalArgumentException expected){}
  try{atm.withdraw("alice","w83",100);throw new AssertionError();}catch(IllegalStateException expected){}
  if(atm.balance()!=400)throw new AssertionError();
  System.out.println("PASS: bounded-note backtracking, owner check, replay, conflict and no-change failure");
 }
}
```

[Runnable lab source](../../examples/mock/AtmDemo.java)

```powershell
javac -d .pattern-classes examples/mock/AtmDemo.java
java -cp .pattern-classes AtmDemo
```

The local lab proves only its stated invariants, not external banking/hardware/broker behavior.

### Interviewer follow-ups

- What if cash was dispensed but the confirmation was lost?

- How do two ATMs coordinate one account’s available funds?

## 10. Design a stock order book

### Interview prompt and example

S1 sells five units at 100; S2 sells three at 100. B1 buys six with limit 101: fill S1 first for five and S2 for one, at maker price 100.

### Specify the market contract

This exercise is one instrument, integer price ticks, positive quantities and limit orders with price-time priority. State whether matching uses maker price, how cancellation works and whether market orders/self-trade prevention/auctions exist. The lab deliberately omits those extra market rules.

### Data structures

Maintain a buy priority queue ordered by highest price then server sequence and a sell queue ordered by lowest price then sequence. Orders carry stable IDs, immutable original request and mutable remaining quantity. An active-ID map supports cancellation; cancelled heap nodes are lazily skipped. A production price-level book may use ordered price maps plus FIFO queues.

### Matching operation

A sequenced submit repeatedly inspects the best opposite order, verifies crossing prices and trades min(takerRemaining,makerRemaining). Update both remaining quantities, remove a finished maker and rest the taker only if quantity remains. Do not reorder same-price makers by client timestamps. The lab serializes commands with synchronized and uses server sequence numbers.

### Retries and cancellation

Retain request/result identity so retrying the exact original order ID returns its original submission result without rematching. Reusing the ID with changed parameters conflicts. A cancel applies to the currently resting remainder once; it cannot erase an executed trade. In a real service authenticate clients, bind order ownership and authorize cancellation.

### Recovery and cost

The runnable lab tests maker price, same-price FIFO, partial fills, replay, cancellation and payload conflict. It is in-memory, uses lazy tombstones and keeps deduplication history indefinitely, so it is not a production exchange. Journal accepted commands with deterministic sequencing, snapshots/replay and retention in a real design. For t matches, heap work is roughly O((t+1) log n), plus lazy cleanup; cancellation marks O(1) but memory cleanup is deferred.

### Java solution

Code is a complete lab where it declares a public class, otherwise a method/type snippet for a Solution class with java.util imports as needed.

```java
import java.util.*;
public class OrderBookDemo {
 enum Side{BUY,SELL}
 record Request(String id,Side side,long price,long quantity){}
 record Trade(String buyer,String seller,long price,long quantity){}
 static class Order{final Request request;final long sequence;long remaining;Order(Request r,long s){request=r;remaining=r.quantity();sequence=s;}}
 static class Book{
  private final PriorityQueue<Order> buys=new PriorityQueue<>(Comparator.<Order>comparingLong(o->o.request.price()).reversed().thenComparingLong(o->o.sequence));
  private final PriorityQueue<Order> sells=new PriorityQueue<>(Comparator.<Order>comparingLong(o->o.request.price()).thenComparingLong(o->o.sequence));
  private final Map<String,Order> active=new HashMap<>();private final Map<String,Request> requests=new HashMap<>();private final Map<String,List<Trade>> results=new HashMap<>();private long sequence;
  synchronized List<Trade> submit(Request request){
   if(request.id()==null||request.id().isBlank()||request.side()==null||request.price()<=0||request.quantity()<=0)throw new IllegalArgumentException();
   if(requests.containsKey(request.id())){if(!requests.get(request.id()).equals(request))throw new IllegalArgumentException("id payload mismatch");return results.get(request.id());}
   Order taker=new Order(request,++sequence);var opposing=request.side()==Side.BUY?sells:buys;List<Trade> trades=new ArrayList<>();
   while(taker.remaining>0){
    while(!opposing.isEmpty()&&opposing.peek().remaining==0)opposing.poll();if(opposing.isEmpty())break;
    Order maker=opposing.peek();boolean crosses=request.side()==Side.BUY?request.price()>=maker.request.price():request.price()<=maker.request.price();if(!crosses)break;
    long quantity=Math.min(taker.remaining,maker.remaining);
    trades.add(new Trade(request.side()==Side.BUY?request.id():maker.request.id(),request.side()==Side.SELL?request.id():maker.request.id(),maker.request.price(),quantity));
    taker.remaining-=quantity;maker.remaining-=quantity;if(maker.remaining==0){opposing.poll();active.remove(maker.request.id());}
   }
   if(taker.remaining>0){(request.side()==Side.BUY?buys:sells).offer(taker);active.put(request.id(),taker);}
   requests.put(request.id(),request);var result=List.copyOf(trades);results.put(request.id(),result);return result;
  }
  synchronized boolean cancel(String id){Order order=active.remove(id);if(order==null)return false;order.remaining=0;return true;}
 }
 public static void main(String[] args){
  Book b=new Book();b.submit(new Request("S1",Side.SELL,100,5));b.submit(new Request("S2",Side.SELL,100,3));
  Request buy=new Request("B1",Side.BUY,101,6);var trades=b.submit(buy);
  if(!trades.equals(List.of(new Trade("B1","S1",100,5),new Trade("B1","S2",100,1))))throw new AssertionError();
  if(!b.submit(buy).equals(trades))throw new AssertionError();b.submit(new Request("B2",Side.BUY,99,1));if(!b.cancel("B2")||b.cancel("B2"))throw new AssertionError();
  if(!b.submit(new Request("B3",Side.BUY,100,2)).equals(List.of(new Trade("B3","S2",100,2))))throw new AssertionError();
  try{b.submit(new Request("B1",Side.BUY,101,7));throw new AssertionError();}catch(IllegalArgumentException expected){}
  System.out.println("PASS: price-time priority, maker price, partial fill, replay, cancel and payload conflict");
 }
}
```

[Runnable lab source](../../examples/mock/OrderBookDemo.java)

```powershell
javac -d .pattern-classes examples/mock/OrderBookDemo.java
java -cp .pattern-classes OrderBookDemo
```

The local lab proves only its stated invariants, not external banking/hardware/broker behavior.

### Interviewer follow-ups

- Which state wins when cancel and execution race?

- Why can a retry not simply submit a new order ID?

## 11. Design a parking lot

### Interview prompt and example

Two entry gates compete for one free car slot.

### Model answer

Define immutable Vehicle/Slot/Gate/Ticket values and one authoritative lot allocator. Select a documented compatibility/nearest-level policy, then assign slot and record active ticket atomically. Exit validates an active ticket and exit gate before freeing the exact slot once.

### Concurrency and recovery

A synchronized local allocator is enough only for one process. Multiple replicas need a transaction/constraint or a single assignment owner. Persist admissions and reconcile sensors for restart recovery. Keep payment/hardware I/O outside a coarse slot lock.

### Worked solution

The full ParkingLotDemo and tutorial cover levels, entry/exit directions, duplicate plates, closed tickets and two concurrent entry attempts. State which errors leave occupancy unchanged and which operations are intentionally outside the demo.

### Java solution

Code is a complete lab where it declares a public class, otherwise a method/type snippet for a Solution class with java.util imports as needed.

```java
import java.util.*;
import java.util.concurrent.*;

public class ParkingLotDemo {
 enum Kind {BIKE,CAR,TRUCK}
 enum Direction {ENTRY,EXIT}
 record Gate(String id,int level,Direction direction){}
 record Slot(String id,int level,Kind kind){}
 record Vehicle(String plate,Kind kind){}
 record Ticket(long id,Vehicle vehicle,Slot slot,String entryGate){}
 static class Lot {
  private final Map<String,Gate> gates=new HashMap<>();
  private final Map<String,Slot> free=new HashMap<>();
  private final Map<Long,Ticket> active=new HashMap<>();
  private final Set<String> parked=new HashSet<>();
  private long nextId=1;
  Lot(List<Gate> gates,List<Slot> slots){
   for(Gate g:gates)if(this.gates.putIfAbsent(g.id(),g)!=null)throw new IllegalArgumentException("duplicate gate");
   for(Slot s:slots)if(free.putIfAbsent(s.id(),s)!=null)throw new IllegalArgumentException("duplicate slot");
  }
  private Gate gate(String id,Direction direction){
   Gate g=gates.get(id);if(g==null||g.direction()!=direction)throw new IllegalArgumentException("invalid gate");return g;
  }
  synchronized Optional<Ticket> enter(String gateId,Vehicle vehicle){
   Gate entry=gate(gateId,Direction.ENTRY);Objects.requireNonNull(vehicle);
   if(vehicle.plate()==null||vehicle.plate().isBlank()||vehicle.kind()==null)throw new IllegalArgumentException("vehicle required");
   if(parked.contains(vehicle.plate()))throw new IllegalStateException("already parked");
   // Explicit policy: exact kind, nearest level to gate, then stable slot ID.
   Optional<Slot> candidate=free.values().stream().filter(s->s.kind()==vehicle.kind())
    .min(Comparator.<Slot>comparingLong(s->Math.abs((long)s.level()-entry.level())).thenComparing(Slot::id));
   if(candidate.isEmpty())return Optional.empty();
   Slot slot=candidate.get();Ticket ticket=new Ticket(nextId++,vehicle,slot,gateId);
   free.remove(slot.id());parked.add(vehicle.plate());active.put(ticket.id(),ticket);return Optional.of(ticket);
  }
  synchronized Ticket exit(String gateId,long ticketId){
   gate(gateId,Direction.EXIT);Ticket ticket=active.get(ticketId);
   if(ticket==null)throw new IllegalArgumentException("unknown or closed ticket");
   active.remove(ticketId);parked.remove(ticket.vehicle().plate());free.put(ticket.slot().id(),ticket.slot());return ticket;
  }
 }
 static void check(boolean value){if(!value)throw new AssertionError();}
 public static void main(String[] args)throws Exception{
  var gates=List.of(new Gate("E0",0,Direction.ENTRY),new Gate("E1",1,Direction.ENTRY),new Gate("X0",0,Direction.EXIT));
  Lot lot=new Lot(gates,List.of(new Slot("L0-C1",0,Kind.CAR),new Slot("L1-C1",1,Kind.CAR),new Slot("L0-B1",0,Kind.BIKE)));
  Ticket ticket=lot.enter("E1",new Vehicle("CAR-81",Kind.CAR)).orElseThrow();check(ticket.slot().level()==1);
  try{lot.enter("E0",ticket.vehicle());throw new AssertionError();}catch(IllegalStateException expected){}
  try{lot.exit("E0",ticket.id());throw new AssertionError();}catch(IllegalArgumentException expected){}
  check(lot.exit("X0",ticket.id()).equals(ticket));
  try{lot.exit("X0",ticket.id());throw new AssertionError();}catch(IllegalArgumentException expected){}
  Lot one=new Lot(gates,List.of(new Slot("only",0,Kind.CAR)));
  try(var pool=Executors.newFixedThreadPool(2)){
   var a=pool.submit(()->one.enter("E0",new Vehicle("A",Kind.CAR)).isPresent());
   var b=pool.submit(()->one.enter("E1",new Vehicle("B",Kind.CAR)).isPresent());
   check((a.get()?1:0)+(b.get()?1:0)==1);
  }
  System.out.println("PASS: levels, gate validation, exact-kind policy, closed tickets and competing entries");
 }
}
```

[Runnable lab source](../../examples/lld/ParkingLotDemo.java)

```powershell
javac -d .pattern-classes examples/lld/ParkingLotDemo.java
java -cp .pattern-classes ParkingLotDemo
```

The local lab proves only its stated invariants, not external banking/hardware/broker behavior.

### Interviewer follow-ups

- How would you change the slot-selection policy without changing ticket lifecycle?

## 12. Design a rate limiter class

### Interview prompt and example

One tenant has one token left and two request threads arrive together.

### Model answer

Bucket owns capacity, fractional tokens, refill rate, last time and injected monotonic clock. Refill, compare and consume must happen inside one atomic boundary. Limiter selects a configured bucket using trusted caller/tenant identity.

### Error behavior and scale

Reject invalid cost/unknown tenant; deny without enough tokens. A controller translates deny to 429 with retry guidance. Independent process-local buckets multiply the effective global limit; use one key owner/shared atomic operation or explicitly allocated local budgets across servers.

### Worked solution

TokenBucketDemo tests refill with an injected clock instead of sleeps, burst capacity and 50 competing calls for ten tokens. It explains outage policy, tenant memory bounds and why rate limiting does not replace in-flight backpressure.

### Java solution

Code is a complete lab where it declares a public class, otherwise a method/type snippet for a Solution class with java.util imports as needed.

```java
import java.util.*;
import java.util.concurrent.*;
import java.util.concurrent.atomic.*;
import java.util.function.LongSupplier;
public class TokenBucketDemo {
 static class Bucket {
  private final double capacity,perSecond;private final LongSupplier clock;private double tokens;private long last;
  Bucket(int capacity,double perSecond,LongSupplier clock){
   if(capacity<1||!Double.isFinite(perSecond)||perSecond<=0)throw new IllegalArgumentException();
   this.capacity=capacity;this.perSecond=perSecond;this.clock=Objects.requireNonNull(clock);tokens=capacity;last=clock.getAsLong();
  }
  synchronized boolean allow(int cost){
   if(cost<1)throw new IllegalArgumentException("positive cost required");long now=clock.getAsLong();long elapsed=now-last;
   if(elapsed>0){tokens=Math.min(capacity,tokens+elapsed/1_000_000_000.0*perSecond);last=now;}
   if(tokens<cost)return false;tokens-=cost;return true;
  }
 }
 // A fixed authenticated-tenant registry avoids unbounded attacker-created keys in this demo.
 record Limiter(Map<String,Bucket> configured){
  Limiter{configured=Map.copyOf(configured);}
  boolean allow(String trustedTenant,int cost){Bucket b=configured.get(trustedTenant);if(b==null)throw new IllegalArgumentException("unknown tenant");return b.allow(cost);}
 }
 static void check(boolean ok){if(!ok)throw new AssertionError();}
 public static void main(String[] args)throws Exception{
  AtomicLong time=new AtomicLong();Bucket b=new Bucket(2,1,time::get);check(b.allow(1));check(b.allow(1));check(!b.allow(1));
  time.addAndGet(500_000_000);check(!b.allow(1));time.addAndGet(500_000_000);check(b.allow(1));check(!b.allow(1));
  Bucket racing=new Bucket(10,1,time::get);AtomicInteger accepted=new AtomicInteger();
  try(var pool=Executors.newFixedThreadPool(8)){
   List<Future<?>> work=new ArrayList<>();for(int i=0;i<50;i++)work.add(pool.submit(()->{if(racing.allow(1))accepted.incrementAndGet();}));for(var f:work)f.get();
  }
  check(accepted.get()==10);
  Limiter limiter=new Limiter(Map.of("A",new Bucket(1,1,time::get),"B",new Bucket(1,1,time::get)));
  check(limiter.allow("A",1));check(!limiter.allow("A",1));check(limiter.allow("B",1));
  try{b.allow(0);throw new AssertionError();}catch(IllegalArgumentException expected){}
  System.out.println("PASS: burst/refill without sleeps, final-token concurrency, independent tenants and invalid cost");
 }
}
```

[Runnable lab source](../../examples/lld/TokenBucketDemo.java)

```powershell
javac -d .pattern-classes examples/lld/TokenBucketDemo.java
java -cp .pattern-classes TokenBucketDemo
```

The local lab proves only its stated invariants, not external banking/hardware/broker behavior.

### Interviewer follow-ups

- What happens to quota when an idle bucket is evicted and recreated?
