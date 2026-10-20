// Java 21, standard library only. Compile: javac Lab090.java ; run: java Lab090
// Demonstrates one focused invariant, not a replacement for framework integration tests.
public class Lab090 {
  static void check(boolean ok,String message){if(!ok)throw new AssertionError(message);System.out.println("PASS: "+message);}
  public static void main(String[] args) throws Exception {
    var routes=java.util.Map.of("/orders","order-service","/users","identity-service");check(routes.get("/orders").equals("order-service"),"gateway routing model");
  }
}
