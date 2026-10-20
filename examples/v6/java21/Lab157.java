// Java 21, standard library only. Compile: javac Lab157.java ; run: java Lab157
// Demonstrates one focused invariant, not a replacement for framework integration tests.
public class Lab157 {
  static void check(boolean ok,String message){if(!ok)throw new AssertionError(message);System.out.println("PASS: "+message);}
  public static void main(String[] args) throws Exception {
    record Decision(int cost,int latency,int risk){}var a=new Decision(10,20,3);var b=new Decision(8,40,6);check(a.latency()<b.latency()&&a.cost()>b.cost(),"explicit tradeoff matrix");
  }
}
