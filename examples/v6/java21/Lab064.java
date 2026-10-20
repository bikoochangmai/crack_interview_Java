// Java 21, standard library only. Compile: javac Lab064.java ; run: java Lab064
// Demonstrates one focused invariant, not a replacement for framework integration tests.
public class Lab064 {
  static void check(boolean ok,String message){if(!ok)throw new AssertionError(message);System.out.println("PASS: "+message);}
  public static void main(String[] args) throws Exception {
    interface Client {String call();}record Config(){Client client(){return ()->"configured";}}check(new Config().client().call().equals("configured"),"factory method vs component discovery");
  }
}
