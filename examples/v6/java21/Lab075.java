// Java 21, standard library only. Compile: javac Lab075.java ; run: java Lab075
// Demonstrates one focused invariant, not a replacement for framework integration tests.
public class Lab075 {
  static void check(boolean ok,String message){if(!ok)throw new AssertionError(message);System.out.println("PASS: "+message);}
  public static void main(String[] args) throws Exception {
    record Health(boolean database,boolean queue){}var h=new Health(true,false);check(!h.queue(),"readiness should fail when critical dependency fails");
  }
}
