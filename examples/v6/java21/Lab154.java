// Java 21, standard library only. Compile: javac Lab154.java ; run: java Lab154
// Demonstrates one focused invariant, not a replacement for framework integration tests.
public class Lab154 {
  static void check(boolean ok,String message){if(!ok)throw new AssertionError(message);System.out.println("PASS: "+message);}
  public static void main(String[] args) throws Exception {
    record Chunk(String docId,String text){}var chunks=java.util.List.of(new Chunk("policy-1","retain audit logs"));check(chunks.stream().anyMatch(c->c.text().contains("audit")),"toy lexical retrieval; production RAG requires embeddings, access filtering, citations");
  }
}
