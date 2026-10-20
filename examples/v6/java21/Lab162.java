// Java 21, standard library only. Compile: javac Lab162.java ; run: java Lab162
// Demonstrates one focused invariant, not a replacement for framework integration tests.
public class Lab162 {
  static void check(boolean ok,String message){if(!ok)throw new AssertionError(message);System.out.println("PASS: "+message);}
  public static void main(String[] args) throws Exception {
    record IndexedDoc(String id,long version){}var doc=new IndexedDoc("doc-1",4);check(doc.version()>0,"index version; actual Elasticsearch integration needs client");
  }
}
