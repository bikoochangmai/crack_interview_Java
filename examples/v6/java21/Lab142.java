// Java 21, standard library only. Compile: javac Lab142.java ; run: java Lab142
// Demonstrates one focused invariant, not a replacement for framework integration tests.
public class Lab142 {
  static void check(boolean ok,String message){if(!ok)throw new AssertionError(message);System.out.println("PASS: "+message);}
  public static void main(String[] args) throws Exception {
    record Architecture(String context,String component,String deployment){}var a=new Architecture("users","orders","aks");check(!a.context().isBlank(),"HLD context vs LLD component contracts");
  }
}
