// Java 21, standard library only. Compile: javac Lab068.java ; run: java Lab068
// Demonstrates one focused invariant, not a replacement for framework integration tests.
public class Lab068 {
  static void check(boolean ok,String message){if(!ok)throw new AssertionError(message);System.out.println("PASS: "+message);}
  public static void main(String[] args) throws Exception {
    var settings=java.util.Map.of("dev","jdbc:postgresql://localhost/dev","prod","jdbc:postgresql://db/prod");check(!settings.get("dev").equals(settings.get("prod")),"external profile settings");
  }
}
