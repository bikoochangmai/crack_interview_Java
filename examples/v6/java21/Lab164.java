// Java 21, standard library only. Compile: javac Lab164.java ; run: java Lab164
// Demonstrates one focused invariant, not a replacement for framework integration tests.
public class Lab164 {
  static void check(boolean ok,String message){if(!ok)throw new AssertionError(message);System.out.println("PASS: "+message);}
  public static void main(String[] args) throws Exception {
    record Review(String author,String reviewer,boolean testsPass){}var r=new Review("dev","peer",true);check(r.testsPass()&&!r.author().equals(r.reviewer()),"review gate");
  }
}
