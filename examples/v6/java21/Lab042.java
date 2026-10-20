// Java 21, standard library only. Compile: javac Lab042.java ; run: java Lab042
// Demonstrates one focused invariant, not a replacement for framework integration tests.
public class Lab042 {
  static void check(boolean ok,String message){if(!ok)throw new AssertionError(message);System.out.println("PASS: "+message);}
  public static void main(String[] args) throws Exception {
    record Stable(String id){} check(new Stable("a").id().equals("a"),"finalized record; preview features require --enable-preview and matching JDK");
  }
}
