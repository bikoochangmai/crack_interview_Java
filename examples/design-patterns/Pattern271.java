import java.util.concurrent.*;
public class Pattern271 {
 // One enum instance per defining classloader; no cross-replica guarantee.
 enum Rules {INSTANCE;
  long total(long unitPaise,int quantity){if(unitPaise<0||quantity<0)throw new IllegalArgumentException();return Math.multiplyExact(unitPaise,quantity);}
 }
 // A Spring-managed service should similarly keep request values in locals.
 static class OrderService {
  final Rules rules;
  OrderService(Rules rules){this.rules=rules;}
  long price(long unitPaise,int quantity){return rules.total(unitPaise,quantity);}
 }
 public static void main(String[] args)throws Exception{
  if(Rules.INSTANCE!=Rules.INSTANCE)throw new AssertionError();
  var shared=new OrderService(Rules.INSTANCE);
  try(var pool=Executors.newFixedThreadPool(2)){
   var a=pool.submit(()->shared.price(5000,2));var b=pool.submit(()->shared.price(7000,3));
   if(a.get()!=10000L||b.get()!=21000L)throw new AssertionError();
  }
  // Merely using the same class does not make manually constructed services identical.
  if(new OrderService(Rules.INSTANCE)==shared)throw new AssertionError();
  System.out.println("PASS: enum identity and independent concurrent request values");
 }
}
