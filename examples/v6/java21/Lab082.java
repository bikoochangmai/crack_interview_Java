// Java 21, standard library only. Compile: javac Lab082.java ; run: java Lab082
// Demonstrates one focused invariant, not a replacement for framework integration tests.
public class Lab082 {
  static void check(boolean ok,String message){if(!ok)throw new AssertionError(message);System.out.println("PASS: "+message);}
  public static void main(String[] args) throws Exception {
    var statuses=java.util.Map.of(200,"OK",201,"Created",409,"Conflict",429,"Too Many Requests");check(statuses.get(409).equals("Conflict"),"status classification");
  }
}
