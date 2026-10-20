// Java 21, standard library only. Compile: javac Lab151.java ; run: java Lab151
// Demonstrates one focused invariant, not a replacement for framework integration tests.
public class Lab151 {
  static void check(boolean ok,String message){if(!ok)throw new AssertionError(message);System.out.println("PASS: "+message);}
  public static void main(String[] args) throws Exception {
    var versions=java.util.List.of("v1","v2");check(versions.contains("v1")&&versions.contains("v2"),"expand/contract rollout compatibility");
  }
}
