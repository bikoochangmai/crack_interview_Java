// Java 21, standard library only. Compile: javac Lab165.java ; run: java Lab165
// Demonstrates one focused invariant, not a replacement for framework integration tests.
public class Lab165 {
  static void check(boolean ok,String message){if(!ok)throw new AssertionError(message);System.out.println("PASS: "+message);}
  public static void main(String[] args) throws Exception {
    int requestsPerSecond=500,averageMs=200;double concurrency=requestsPerSecond*averageMs/1000.0;check(concurrency==100,"Little law estimate under stable assumptions");
  }
}
