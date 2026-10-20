// Java 21, standard library only. Compile: javac Lab057.java ; run: java Lab057
// Demonstrates one focused invariant, not a replacement for framework integration tests.
public class Lab057 {
  static void check(boolean ok,String message){if(!ok)throw new AssertionError(message);System.out.println("PASS: "+message);}
  public static void main(String[] args) throws Exception {
    var ref=new java.lang.ref.WeakReference<>(new Object());check(ref!=null,"weak reference is not a substitute for heap dump + retention-path analysis");
  }
}
