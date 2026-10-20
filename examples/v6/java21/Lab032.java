// Java 21, standard library only. Compile: javac Lab032.java ; run: java Lab032
// Demonstrates one focused invariant, not a replacement for framework integration tests.
public class Lab032 {
  static void check(boolean ok,String message){if(!ok)throw new AssertionError(message);System.out.println("PASS: "+message);}
  public static void main(String[] args) throws Exception {
    var entries=java.util.Map.of("x",1,"y",2);check(entries.get("x")==1,"Java 10 var inference + immutable map");
  }
}
