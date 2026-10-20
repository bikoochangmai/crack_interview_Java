// Java 21, standard library only. Compile: javac Lab167.java ; run: java Lab167
// Demonstrates one focused invariant, not a replacement for framework integration tests.
public class Lab167 {
  static void check(boolean ok,String message){if(!ok)throw new AssertionError(message);System.out.println("PASS: "+message);}
  public static void main(String[] args) throws Exception {
    record Finding(String control,String evidenceId,boolean approved){}var f=new Finding("AC-1","ev-3",false);check(!f.approved(),"human approval gate in compliance audit");
  }
}
