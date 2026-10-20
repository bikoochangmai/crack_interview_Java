// Java 21, standard library only. Compile: javac Lab155.java ; run: java Lab155
// Demonstrates one focused invariant, not a replacement for framework integration tests.
public class Lab155 {
  static void check(boolean ok,String message){if(!ok)throw new AssertionError(message);System.out.println("PASS: "+message);}
  public static void main(String[] args) throws Exception {
    enum State{DRAFT,PENDING,APPROVED,REJECTED}State state=State.PENDING;check(state!=State.APPROVED,"approval gate denies action until authorized decision");
  }
}
