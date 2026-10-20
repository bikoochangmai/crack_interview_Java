// Java 21, standard library only. Compile: javac Lab153.java ; run: java Lab153
// Demonstrates one focused invariant, not a replacement for framework integration tests.
public class Lab153 {
  static void check(boolean ok,String message){if(!ok)throw new AssertionError(message);System.out.println("PASS: "+message);}
  public static void main(String[] args) throws Exception {
    var redirects=new java.util.HashMap<String,String>();redirects.put("ab12","https://example.test/docs");check(redirects.get("ab12").startsWith("https"),"short code lookup, uniqueness/abuse checks omitted");
  }
}
