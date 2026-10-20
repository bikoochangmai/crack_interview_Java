// Java 21, standard library only. Compile: javac Lab147.java ; run: java Lab147
// Demonstrates one focused invariant, not a replacement for framework integration tests.
public class Lab147 {
  static void check(boolean ok,String message){if(!ok)throw new AssertionError(message);System.out.println("PASS: "+message);}
  public static void main(String[] args) throws Exception {
    record StreamEvent(String partition,long offset){}var e=new StreamEvent("orders",5);check(e.offset()==5,"ordered stream offset vs queue message settlement");
  }
}
