// Java 21, standard library only. Compile: javac Lab033.java ; run: java Lab033
// Demonstrates one focused invariant, not a replacement for framework integration tests.
public class Lab033 {
  static void check(boolean ok,String message){if(!ok)throw new AssertionError(message);System.out.println("PASS: "+message);}
  public static void main(String[] args) throws Exception {
    String s="  hi  ";check(s.strip().equals("hi")&&"x\ny".lines().count()==2,"Java 11 string APIs");
  }
}
