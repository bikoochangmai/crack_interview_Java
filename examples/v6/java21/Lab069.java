// Java 21, standard library only. Compile: javac Lab069.java ; run: java Lab069
// Demonstrates one focused invariant, not a replacement for framework integration tests.
public class Lab069 {
  static void check(boolean ok,String message){if(!ok)throw new AssertionError(message);System.out.println("PASS: "+message);}
  public static void main(String[] args) throws Exception {
    record Tx(boolean active){}java.util.function.Function<Tx,String> service=t->t.active()?"committed":"rejected";check(service.apply(new Tx(true)).equals("committed"),"transaction boundary model; Spring proxy semantics need integration test");
  }
}
