// Java 21, standard library only. Compile: javac Lab043.java ; run: java Lab043
// Demonstrates one focused invariant, not a replacement for framework integration tests.
public class Lab043 {
  static void check(boolean ok,String message){if(!ok)throw new AssertionError(message);System.out.println("PASS: "+message);}
  public static void main(String[] args) throws Exception {
    try(var exec=java.util.concurrent.Executors.newVirtualThreadPerTaskExecutor()){var f=exec.submit(()->Thread.currentThread().isVirtual());check(f.get(),"virtual thread");}
  }
}
