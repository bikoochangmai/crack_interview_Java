// Java 21, standard library only. Compile: javac Lab158.java ; run: java Lab158
// Demonstrates one focused invariant, not a replacement for framework integration tests.
public class Lab158 {
  static void check(boolean ok,String message){if(!ok)throw new AssertionError(message);System.out.println("PASS: "+message);}
  public static void main(String[] args) throws Exception {
    record Incident(String symptom,String mitigation,String outcome){}var i=new Incident("timeouts","shed load","recovered");check(i.outcome().equals("recovered"),"STAR outline; replace with real personal evidence");
  }
}
