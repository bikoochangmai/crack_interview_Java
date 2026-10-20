// Java 21, standard library only. Compile: javac Lab163.java ; run: java Lab163
// Demonstrates one focused invariant, not a replacement for framework integration tests.
public class Lab163 {
  static void check(boolean ok,String message){if(!ok)throw new AssertionError(message);System.out.println("PASS: "+message);}
  public static void main(String[] args) throws Exception {
    record Citation(String documentId,String span){}var c=new Citation("policy-1","p2");check(!c.span().isBlank(),"grounding citation; judge-based faithfulness requires external evaluation");
  }
}
