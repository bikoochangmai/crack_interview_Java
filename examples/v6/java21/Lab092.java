// Java 21, standard library only. Compile: javac Lab092.java ; run: java Lab092
// Demonstrates one focused invariant, not a replacement for framework integration tests.
public class Lab092 {
  static void check(boolean ok,String message){if(!ok)throw new AssertionError(message);System.out.println("PASS: "+message);}
  public static void main(String[] args) throws Exception {
    var completed=new java.util.ArrayList<String>();completed.add("reserve");completed.add("charge");completed.remove("charge");completed.remove("reserve");check(completed.isEmpty(),"saga compensation model, not atomic rollback");
  }
}
