// Java 21, standard library only. Compile: javac Lab083.java ; run: java Lab083
// Demonstrates one focused invariant, not a replacement for framework integration tests.
public class Lab083 {
  static void check(boolean ok,String message){if(!ok)throw new AssertionError(message);System.out.println("PASS: "+message);}
  public static void main(String[] args) throws Exception {
    var orders=java.util.List.of("a","b","c","d");var page=orders.subList(1,3);check(page.equals(java.util.List.of("b","c")),"offset pagination demo; cursor recommended for mutable feeds");
  }
}
