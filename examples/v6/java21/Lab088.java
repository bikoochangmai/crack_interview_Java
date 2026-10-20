// Java 21, standard library only. Compile: javac Lab088.java ; run: java Lab088
// Demonstrates one focused invariant, not a replacement for framework integration tests.
public class Lab088 {
  static void check(boolean ok,String message){if(!ok)throw new AssertionError(message);System.out.println("PASS: "+message);}
  public static void main(String[] args) throws Exception {
    record User(String team,java.util.Set<String> roles){}var u=new User("audit",java.util.Set.of("reviewer"));check(u.roles().contains("reviewer")&&u.team().equals("audit"),"RBAC role + ABAC attribute");
  }
}
