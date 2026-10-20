// Java 21, standard library only. Compile: javac Lab063.java ; run: java Lab063
// Demonstrates one focused invariant, not a replacement for framework integration tests.
public class Lab063 {
  static void check(boolean ok,String message){if(!ok)throw new AssertionError(message);System.out.println("PASS: "+message);}
  public static void main(String[] args) throws Exception {
    var singleton=new Object();java.util.function.Supplier<Object> prototype=Object::new;check(singleton==singleton&&prototype.get()!=prototype.get(),"singleton vs prototype lifecycle");
  }
}
