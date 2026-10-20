// Java 21, standard library only. Compile: javac Lab062.java ; run: java Lab062
// Demonstrates one focused invariant, not a replacement for framework integration tests.
public class Lab062 {
  static void check(boolean ok,String message){if(!ok)throw new AssertionError(message);System.out.println("PASS: "+message);}
  public static void main(String[] args) throws Exception {
    record Request(String pathId,String query,String body){}var r=new Request("42","verbose=true","{\"status\":\"ok\"}");check(r.pathId().equals("42")&&r.body().contains("status"),"three HTTP input locations");
  }
}
