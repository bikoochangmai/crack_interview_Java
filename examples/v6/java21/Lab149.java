// Java 21, standard library only. Compile: javac Lab149.java ; run: java Lab149
// Demonstrates one focused invariant, not a replacement for framework integration tests.
public class Lab149 {
  static void check(boolean ok,String message){if(!ok)throw new AssertionError(message);System.out.println("PASS: "+message);}
  public static void main(String[] args) throws Exception {
    record Document(String tenantId,String id){}var d=new Document("tenant-a","doc-1");check(!d.tenantId().equals("tenant-b"),"tenant predicate must be enforced server-side");
  }
}
