// Java 21, standard library only. Compile: javac Lab035.java ; run: java Lab035
// Demonstrates one focused invariant, not a replacement for framework integration tests.
public class Lab035 {
  static void check(boolean ok,String message){if(!ok)throw new AssertionError(message);System.out.println("PASS: "+message);}
  public static void main(String[] args) throws Exception {
    String json="""
 {"orderId":"o-1","status":"PAID"}
 """;check(json.contains("PAID"),"text block");
  }
}
