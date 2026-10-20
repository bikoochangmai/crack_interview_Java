// Java 21, standard library only. Compile: javac Lab072.java ; run: java Lab072
// Demonstrates one focused invariant, not a replacement for framework integration tests.
public class Lab072 {
  static void check(boolean ok,String message){if(!ok)throw new AssertionError(message);System.out.println("PASS: "+message);}
  public static void main(String[] args) throws Exception {
    record Response(int status,String body){}java.util.function.Function<String,Response> handler=path->new Response(200,"ok:"+path);check(handler.apply("/orders").status()==200,"request routing pipeline model");
  }
}
