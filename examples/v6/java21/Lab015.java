// Java 21, standard library only. Compile: javac Lab015.java ; run: java Lab015
// Demonstrates one focused invariant, not a replacement for framework integration tests.
public class Lab015 {
  static void check(boolean ok,String message){if(!ok)throw new AssertionError(message);System.out.println("PASS: "+message);}
  public static void main(String[] args) throws Exception {
    interface Gateway { String charge(int cents); } record Stripe() implements Gateway { public String charge(int c){return "paid:"+c;} } record Checkout(Gateway gateway){String run(){return gateway.charge(500);}} check(new Checkout(new Stripe()).run().equals("paid:500"),"constructor injection");
  }
}
