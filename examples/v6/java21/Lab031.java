// Java 21, standard library only. Compile: javac Lab031.java ; run: java Lab031
// Demonstrates one focused invariant, not a replacement for framework integration tests.
public class Lab031 {
  static void check(boolean ok,String message){if(!ok)throw new AssertionError(message);System.out.println("PASS: "+message);}
  public static void main(String[] args) throws Exception {
    var immutable=java.util.List.of("A","B");check(immutable.size()==2,"Java 9 collection factories");
  }
}
