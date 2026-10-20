// Java 21, standard library only. Compile: javac Lab077.java ; run: java Lab077
// Demonstrates one focused invariant, not a replacement for framework integration tests.
public class Lab077 {
  static void check(boolean ok,String message){if(!ok)throw new AssertionError(message);System.out.println("PASS: "+message);}
  public static void main(String[] args) throws Exception {
    var client=java.net.http.HttpClient.newHttpClient();var request=java.net.http.HttpRequest.newBuilder(java.net.URI.create("https://example.invalid/health")).GET().build();check(client!=null&&request.method().equals("GET"),"HTTP client construction only; no network call");
  }
}
