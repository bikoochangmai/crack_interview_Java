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
