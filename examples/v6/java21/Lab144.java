// Java 21, standard library only. Compile: javac Lab144.java ; run: java Lab144
// Demonstrates one focused invariant, not a replacement for framework integration tests.
public class Lab144 {
  static void check(boolean ok,String message){if(!ok)throw new AssertionError(message);System.out.println("PASS: "+message);}
  public static void main(String[] args) throws Exception {
    int replicas=4,throughputPerReplica=100;check(replicas*throughputPerReplica==400,"horizontal capacity estimate");
  }
}
