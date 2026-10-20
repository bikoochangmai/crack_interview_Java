// Java 21, standard library only. Compile: javac Lab150.java ; run: java Lab150
// Demonstrates one focused invariant, not a replacement for framework integration tests.
public class Lab150 {
  static void check(boolean ok,String message){if(!ok)throw new AssertionError(message);System.out.println("PASS: "+message);}
  public static void main(String[] args) throws Exception {
    int rtoMinutes=30,rpoMinutes=5;check(rtoMinutes>=rpoMinutes,"RTO downtime and RPO data loss are distinct targets");
  }
}
