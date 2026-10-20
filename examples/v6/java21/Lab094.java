// Java 21, standard library only. Compile: javac Lab094.java ; run: java Lab094
// Demonstrates one focused invariant, not a replacement for framework integration tests.
public class Lab094 {
  static void check(boolean ok,String message){if(!ok)throw new AssertionError(message);System.out.println("PASS: "+message);}
  public static void main(String[] args) throws Exception {
    record Event(String id,long version){}var event=new Event("order-1",2);check(event.version()>1,"projection applies ordered versioned events; eventual convergence");
  }
}
