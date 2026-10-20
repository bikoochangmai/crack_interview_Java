// Java 21, standard library only. Compile: javac Lab159.java ; run: java Lab159
// Demonstrates one focused invariant, not a replacement for framework integration tests.
public class Lab159 {
  static void check(boolean ok,String message){if(!ok)throw new AssertionError(message);System.out.println("PASS: "+message);}
  public static void main(String[] args) throws Exception {
    record ADR(String option,String reason){}var adr=new ADR("queue","decouple ingestion");check(!adr.reason().isBlank(),"architecture decision record outline");
  }
}
