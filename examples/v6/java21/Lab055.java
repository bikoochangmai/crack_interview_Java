// Java 21, standard library only. Compile: javac Lab055.java ; run: java Lab055
// Demonstrates one focused invariant, not a replacement for framework integration tests.
public class Lab055 {
  static void check(boolean ok,String message){if(!ok)throw new AssertionError(message);System.out.println("PASS: "+message);}
  public static void main(String[] args) throws Exception {
    var heap=new java.util.ArrayList<byte[]>();heap.add(new byte[1024]);check(heap.get(0).length==1024,"object on heap; stack holds local reference");
  }
}
