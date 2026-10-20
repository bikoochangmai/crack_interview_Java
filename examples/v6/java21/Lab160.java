// Java 21, standard library only. Compile: javac Lab160.java ; run: java Lab160
// Demonstrates one focused invariant, not a replacement for framework integration tests.
public class Lab160 {
  static void check(boolean ok,String message){if(!ok)throw new AssertionError(message);System.out.println("PASS: "+message);}
  public static void main(String[] args) throws Exception {
    var stages=java.util.List.of("inventory","strangler","dual-run","cutover");check(stages.indexOf("dual-run")<stages.indexOf("cutover"),"legacy migration sequence");
  }
}
