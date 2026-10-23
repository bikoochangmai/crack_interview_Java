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
