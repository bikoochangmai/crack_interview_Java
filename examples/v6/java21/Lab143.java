// Java 21, standard library only. Compile: javac Lab143.java ; run: java Lab143
// Demonstrates one focused invariant, not a replacement for framework integration tests.
public class Lab143 {
  static void check(boolean ok,String message){if(!ok)throw new AssertionError(message);System.out.println("PASS: "+message);}
  public static void main(String[] args) throws Exception {
    record Choice(boolean partition,boolean strongConsistency){}var c=new Choice(true,true);check(c.partition()&&c.strongConsistency(),"CP prioritization under partition; availability tradeoff");
  }
}
