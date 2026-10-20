// Java 21, standard library only. Compile: javac Lab078.java ; run: java Lab078
// Demonstrates one focused invariant, not a replacement for framework integration tests.
public class Lab078 {
  static void check(boolean ok,String message){if(!ok)throw new AssertionError(message);System.out.println("PASS: "+message);}
  public static void main(String[] args) throws Exception {
    var required=java.util.Set.of("DATABASE_URL","JWT_ISSUER");var configured=java.util.Set.of("DATABASE_URL");check(!configured.containsAll(required),"fail-fast startup config check");
  }
}
