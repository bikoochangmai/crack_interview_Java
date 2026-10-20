// Java 21, standard library only. Compile: javac Lab056.java ; run: java Lab056
// Demonstrates one focused invariant, not a replacement for framework integration tests.
public class Lab056 {
  static void check(boolean ok,String message){if(!ok)throw new AssertionError(message);System.out.println("PASS: "+message);}
  public static void main(String[] args) throws Exception {
    var gc=java.lang.management.ManagementFactory.getGarbageCollectorMXBeans();check(!gc.isEmpty(),"inspect collector names/counts; G1 vs ZGC selected at JVM startup");
  }
}
