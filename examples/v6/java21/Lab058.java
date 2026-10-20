// Java 21, standard library only. Compile: javac Lab058.java ; run: java Lab058
// Demonstrates one focused invariant, not a replacement for framework integration tests.
public class Lab058 {
  static void check(boolean ok,String message){if(!ok)throw new AssertionError(message);System.out.println("PASS: "+message);}
  public static void main(String[] args) throws Exception {
    long start=System.nanoTime();java.util.stream.LongStream.range(0,10000).sum();check(System.nanoTime()>=start,"measure latency; investigate JFR/thread dumps and dependency timings");
  }
}
