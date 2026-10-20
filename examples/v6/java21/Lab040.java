// Java 21, standard library only. Compile: javac Lab040.java ; run: java Lab040
// Demonstrates one focused invariant, not a replacement for framework integration tests.
public class Lab040 {
  static void check(boolean ok,String message){if(!ok)throw new AssertionError(message);System.out.println("PASS: "+message);}
  public static void main(String[] args) throws Exception {
    record Point(int x,int y){} Object p=new Point(2,3);check(p instanceof Point(int x,int y) && x+y==5,"record pattern");
  }
}
