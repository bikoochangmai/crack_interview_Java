import java.util.*;
import java.util.function.Consumer;
public class Pattern270 {
 record OrderCreated(String eventId){}
 // In-process observer: synchronous delivery in this deliberately small demo.
 static class OrderEvents {
  final List<Consumer<OrderCreated>> listeners=new ArrayList<>();
  void subscribe(Consumer<OrderCreated> listener){listeners.add(listener);}
  void publish(OrderCreated event){for(var listener:List.copyOf(listeners))listener.accept(event);}
 }
 // Consumer-local deduplication models one concern of broker pub/sub.
 // In production use durable transactional state, not this in-memory set.
 static class EmailConsumer {
  final Set<String> processed=new HashSet<>();int sent;
  void on(OrderCreated event){if(processed.add(event.eventId()))sent++;}
 }
 // Mediator explicitly coordinates collaboration for one use case.
 record CheckoutMediator(List<String> workflow) {
  void checkout(){workflow.add("reserve");workflow.add("record order");workflow.add("request payment");}
 }
 public static void main(String[] args){
  var events=new OrderEvents();var email=new EmailConsumer();var analytics=new ArrayList<String>();
  events.subscribe(email::on);events.subscribe(e->analytics.add(e.eventId()));
  var event=new OrderCreated("e81");events.publish(event);events.publish(event);
  if(email.sent!=1||analytics.size()!=2)throw new AssertionError();
  var steps=new ArrayList<String>();new CheckoutMediator(steps).checkout();
  if(!steps.equals(List.of("reserve","record order","request payment")))throw new AssertionError();
  System.out.println("PASS: local observers, per-consumer deduplication and mediator sequence");
 }
}
