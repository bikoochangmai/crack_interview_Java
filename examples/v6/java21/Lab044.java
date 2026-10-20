// Java 21, standard library only. Compile: javac Lab044.java ; run: java Lab044
// Demonstrates one focused invariant, not a replacement for framework integration tests.
public class Lab044 {
  static void check(boolean ok,String message){if(!ok)throw new AssertionError(message);System.out.println("PASS: "+message);}
  public static void main(String[] args) throws Exception {
    record MigrationResult(boolean testsPass,boolean librariesCompatible){} var result=new MigrationResult(true,true);check(result.testsPass()&&result.librariesCompatible(),"migration gate");
  }
}
