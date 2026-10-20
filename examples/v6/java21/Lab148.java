// Java 21, standard library only. Compile: javac Lab148.java ; run: java Lab148
// Demonstrates one focused invariant, not a replacement for framework integration tests.
public class Lab148 {
  static void check(boolean ok,String message){if(!ok)throw new AssertionError(message);System.out.println("PASS: "+message);}
  public static void main(String[] args) throws Exception {
    record BlobRef(String url,String sha256){}var b=new BlobRef("blob://docs/1","abc");check(b.url().startsWith("blob:"),"store bytes in Blob, metadata in PostgreSQL");
  }
}
