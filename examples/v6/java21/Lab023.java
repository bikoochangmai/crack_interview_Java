// Java 21, standard library only. Compile: javac Lab023.java ; run: java Lab023
// Demonstrates one focused invariant, not a replacement for framework integration tests.
public class Lab023 {
  static void check(boolean ok,String message){if(!ok)throw new AssertionError(message);System.out.println("PASS: "+message);}
  public static void main(String[] args) throws Exception {
    var ids=java.util.List.of("a","bb"); var sizes=ids.stream().map(String::length).toList(); check(sizes.equals(java.util.List.of(1,2)),"instance method reference");
  }
}
