// Java 21, standard library only. Compile: javac Lab028.java ; run: java Lab028
// Demonstrates one focused invariant, not a replacement for framework integration tests.
public class Lab028 {
  static void check(boolean ok,String message){if(!ok)throw new AssertionError(message);System.out.println("PASS: "+message);}
  public static void main(String[] args) throws Exception {
    interface Policy {default boolean allowed(int n){return n>0;} static Policy standard(){return new Policy(){};}} check(Policy.standard().allowed(1)&&!Policy.standard().allowed(0),"interface defaults");
  }
}
