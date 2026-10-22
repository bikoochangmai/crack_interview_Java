import java.util.*;
public class Pattern268 {
 interface PaymentStrategy {String pay(long paise,String requestKey);}
 record Card() implements PaymentStrategy {public String pay(long a,String k){return "card:"+k+":"+a;}}
 record Upi() implements PaymentStrategy {public String pay(long a,String k){return "upi:"+k+":"+a;}}
 record Checkout(Map<String,PaymentStrategy> strategies) {
  Checkout {strategies=Map.copyOf(strategies);}
  String pay(String method,long paise,String requestKey){
   if(paise<=0||requestKey==null||requestKey.isBlank())throw new IllegalArgumentException("amount/key required");
   PaymentStrategy selected=strategies.get(method);
   if(selected==null)throw new IllegalArgumentException("unsupported method");
   return selected.pay(paise,requestKey);
  }
 }
 static void check(boolean ok){if(!ok)throw new AssertionError();}
 public static void main(String[] args){
  var checkout=new Checkout(Map.of("card",new Card(),"upi",new Upi()));
  check(checkout.pay("upi",5000,"order-81").equals("upi:order-81:5000"));
  check(checkout.pay("card",5000,"order-82").startsWith("card:"));
  try{checkout.pay("cash",5000,"order-83");throw new AssertionError();}catch(IllegalArgumentException expected){}
  System.out.println("PASS: policy selection and interchangeable payment behavior");
 }
}
