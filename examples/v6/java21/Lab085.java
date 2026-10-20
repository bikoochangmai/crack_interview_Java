// Java 21, standard library only. Compile: javac Lab085.java ; run: java Lab085
// Demonstrates one focused invariant, not a replacement for framework integration tests.
public class Lab085 {
  static void check(boolean ok,String message){if(!ok)throw new AssertionError(message);System.out.println("PASS: "+message);}
  public static void main(String[] args) throws Exception {
    String header="Bearer eyJ...";check(header.startsWith("Bearer "),"token transport only; never trust JWT without signature/issuer/audience/expiry checks");
  }
}
