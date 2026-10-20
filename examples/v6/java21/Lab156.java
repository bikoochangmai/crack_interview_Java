// Java 21, standard library only. Compile: javac Lab156.java ; run: java Lab156
// Demonstrates one focused invariant, not a replacement for framework integration tests.
public class Lab156 {
  static void check(boolean ok,String message){if(!ok)throw new AssertionError(message);System.out.println("PASS: "+message);}
  public static void main(String[] args) throws Exception {
    record Incident(long detectedAt,long mitigatedAt){}var i=new Incident(100,145);check(i.mitigatedAt()-i.detectedAt()==45,"MTTR measurement");
  }
}
