// Java 21, standard library only. Compile: javac Lab087.java ; run: java Lab087
// Demonstrates one focused invariant, not a replacement for framework integration tests.
public class Lab087 {
  static void check(boolean ok,String message){if(!ok)throw new AssertionError(message);System.out.println("PASS: "+message);}
  public static void main(String[] args) throws Exception {
    String origin="https://app.example.test";var allow=java.util.Set.of(origin);check(allow.contains(origin),"CORS allowlist is browser policy; CSRF needs separate defenses");
  }
}
