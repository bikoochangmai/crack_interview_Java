// Java 21, standard library only. Compile: javac Lab060.java ; run: java Lab060
// Demonstrates one focused invariant, not a replacement for framework integration tests.
public class Lab060 {
  static void check(boolean ok,String message){if(!ok)throw new AssertionError(message);System.out.println("PASS: "+message);}
  public static void main(String[] args) throws Exception {
    interface Repository {String read();}record Service(Repository repository){String call(){return repository.read();}}check(new Service(()->"db").call().equals("db"),"stereotype roles modeled; real annotations require Spring");
  }
}
