// Java 21, standard library only. Compile: javac Lab096.java ; run: java Lab096
// Demonstrates one focused invariant, not a replacement for framework integration tests.
public class Lab096 {
  static void check(boolean ok,String message){if(!ok)throw new AssertionError(message);System.out.println("PASS: "+message);}
  public static void main(String[] args) throws Exception {
    var scopes=java.util.Set.of("orders.read");check(scopes.contains("orders.read")&&!scopes.contains("orders.write"),"least privilege; production mTLS/OAuth requires infrastructure");
  }
}
