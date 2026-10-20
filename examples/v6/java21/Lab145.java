// Java 21, standard library only. Compile: javac Lab145.java ; run: java Lab145
// Demonstrates one focused invariant, not a replacement for framework integration tests.
public class Lab145 {
  static void check(boolean ok,String message){if(!ok)throw new AssertionError(message);System.out.println("PASS: "+message);}
  public static void main(String[] args) throws Exception {
    var cache=new java.util.HashMap<String,String>();cache.put("asset:1","cached");check(cache.get("asset:1").equals("cached"),"cache hit; CDN/LB are external infrastructure");
  }
}
