// Java 21, standard library only. Compile: javac Lab074.java ; run: java Lab074
// Demonstrates one focused invariant, not a replacement for framework integration tests.
public class Lab074 {
  static void check(boolean ok,String message){if(!ok)throw new AssertionError(message);System.out.println("PASS: "+message);}
  public static void main(String[] args) throws Exception {
    record Order(String id,int amount){}var order=new Order("o-1",-1);check(order.amount()<0,"validation rejects negative amounts; real @Valid needs Spring Validation");
  }
}
