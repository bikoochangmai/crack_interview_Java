// Java 21, standard library only. Compile: javac Lab065.java ; run: java Lab065
// Demonstrates one focused invariant, not a replacement for framework integration tests.
public class Lab065 {
  static void check(boolean ok,String message){if(!ok)throw new AssertionError(message);System.out.println("PASS: "+message);}
  public static void main(String[] args) throws Exception {
    record Service(java.util.function.Supplier<String> dependency){}check(new Service(()->"ready").dependency().get().equals("ready"),"constructor-injected mandatory dependency");
  }
}
