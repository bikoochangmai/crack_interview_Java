// Java 21, standard library only. Compile: javac Lab030.java ; run: java Lab030
// Demonstrates one focused invariant, not a replacement for framework integration tests.
public class Lab030 {
  static void check(boolean ok,String message){if(!ok)throw new AssertionError(message);System.out.println("PASS: "+message);}
  public static void main(String[] args) throws Exception {
    var data=java.util.stream.IntStream.range(0,1000).boxed().toList();int total=data.parallelStream().mapToInt(Integer::intValue).sum();check(total==499500,"parallel reduction, no shared mutation");
  }
}
