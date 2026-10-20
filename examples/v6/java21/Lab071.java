// Java 21, standard library only. Compile: javac Lab071.java ; run: java Lab071
// Demonstrates one focused invariant, not a replacement for framework integration tests.
public class Lab071 {
  static void check(boolean ok,String message){if(!ok)throw new AssertionError(message);System.out.println("PASS: "+message);}
  public static void main(String[] args) throws Exception {
    var snapshot=java.util.Map.of("order",10);var changed=new java.util.HashMap<>(snapshot);changed.put("order",20);check(snapshot.get("order")==10,"snapshot analogy; real isolation requires PostgreSQL sessions");
  }
}
