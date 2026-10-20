// Java 21, standard library only. Compile: javac Lab084.java ; run: java Lab084
// Demonstrates one focused invariant, not a replacement for framework integration tests.
public class Lab084 {
  static void check(boolean ok,String message){if(!ok)throw new AssertionError(message);System.out.println("PASS: "+message);}
  public static void main(String[] args) throws Exception {
    record Principal(String name,java.util.Set<String> roles){}var p=new Principal("u",java.util.Set.of("reader"));check(p.name()!=null&&!p.roles().contains("admin"),"authentication identity != authorization grant");
  }
}
