// Java 21, standard library only. Compile: javac Lab076.java ; run: java Lab076
// Demonstrates one focused invariant, not a replacement for framework integration tests.
public class Lab076 {
  static void check(boolean ok,String message){if(!ok)throw new AssertionError(message);System.out.println("PASS: "+message);}
  public static void main(String[] args) throws Exception {
    interface Gateway {boolean pay();}record Checkout(Gateway gateway){boolean run(){return gateway.pay();}}check(new Checkout(()->true).run(),"unit test with fake dependency; Spring slice/integration tests separate");
  }
}
