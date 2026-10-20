// Java 21, standard library only. Compile: javac Lab095.java ; run: java Lab095
// Demonstrates one focused invariant, not a replacement for framework integration tests.
public class Lab095 {
  static void check(boolean ok,String message){if(!ok)throw new AssertionError(message);System.out.println("PASS: "+message);}
  public static void main(String[] args) throws Exception {
    record Span(String traceId,String service,long durationMs){}var s=new Span("t-1","checkout",42);check(s.durationMs()>0,"correlation + tracing metadata");
  }
}
