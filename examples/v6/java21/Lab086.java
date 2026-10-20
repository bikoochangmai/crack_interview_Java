// Java 21, standard library only. Compile: javac Lab086.java ; run: java Lab086
// Demonstrates one focused invariant, not a replacement for framework integration tests.
public class Lab086 {
  static void check(boolean ok,String message){if(!ok)throw new AssertionError(message);System.out.println("PASS: "+message);}
  public static void main(String[] args) throws Exception {
    var verifier=java.util.Base64.getUrlEncoder().withoutPadding().encodeToString("verifier".getBytes(java.nio.charset.StandardCharsets.UTF_8));check(!verifier.isEmpty(),"PKCE verifier encoding illustration; production requires cryptographic random verifier and SHA-256 challenge");
  }
}
