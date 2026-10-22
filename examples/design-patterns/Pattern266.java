import java.util.*;

// SRP: checkout coordinates; gateway charges; receipt store persists.
public class Pattern266 {
 interface Charger { String charge(long paise); } // ISP: narrow capability
 interface ReceiptStore { void save(String receipt); }
 record Checkout(Charger charger, ReceiptStore receipts) { // DIP: depend on contracts
  String pay(long paise) {
   if(paise<=0) throw new IllegalArgumentException("positive amount required");
   String result=charger.charge(paise); receipts.save(result); return result;
  }
 }
 // OCP: another conforming gateway leaves Checkout unchanged.
 static class Card implements Charger { public String charge(long amount){return "card:"+amount;} }
 static class Upi implements Charger { public String charge(long amount){return "upi:"+amount;} }
 static void check(boolean ok){if(!ok)throw new AssertionError();}
 public static void main(String[] args){
  List<String> saved=new ArrayList<>();
  for(Charger gateway:List.of(new Card(),new Upi())) {
   // LSP: either implementation honors the positive-amount charge contract.
   String receipt=new Checkout(gateway,saved::add).pay(5000);
   check(receipt.endsWith(":5000"));
  }
  check(saved.size()==2);
  try{new Checkout(new Card(),saved::add).pay(0);throw new AssertionError();}
  catch(IllegalArgumentException expected){check(saved.size()==2);}
  System.out.println("PASS: gateway substitution, receipt persistence and input guard");
 }
}
