// Java 21, standard library only. Compile: javac Lab166.java ; run: java Lab166
// Demonstrates one focused invariant, not a replacement for framework integration tests.
public class Lab166 {
  static void check(boolean ok,String message){if(!ok)throw new AssertionError(message);System.out.println("PASS: "+message);}
  public static void main(String[] args) throws Exception {
    record Decision(String concern,String experiment){}var d=new Decision("latency","load test");check(!d.experiment().isBlank(),"resolve disagreements using measurable experiment");
  }
}
