// Java 21, standard library only. Compile: javac Lab079.java ; run: java Lab079
// Demonstrates one focused invariant, not a replacement for framework integration tests.
public class Lab079 {
  static void check(boolean ok,String message){if(!ok)throw new AssertionError(message);System.out.println("PASS: "+message);}
  public static void main(String[] args) throws Exception {
    record Resource(String id,String state){}var order=new Resource("42","created");check(order.id().equals("42"),"resource representation; REST uses stateless HTTP methods");
  }
}
