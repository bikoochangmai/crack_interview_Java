// Java 21, standard library only. Compile: javac Lab059.java ; run: java Lab059
// Demonstrates one focused invariant, not a replacement for framework integration tests.
public class Lab059 {
  static void check(boolean ok,String message){if(!ok)throw new AssertionError(message);System.out.println("PASS: "+message);}
  public static void main(String[] args) throws Exception {
    interface Repo {String find();}record Service(Repo repo){String handle(){return repo.find();}}check(new Service(()->"ok").handle().equals("ok"),"IoC/constructor DI model");
  }
}
