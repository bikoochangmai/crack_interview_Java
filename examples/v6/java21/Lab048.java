// Java 21, standard library only. Compile: javac Lab048.java ; run: java Lab048
// Demonstrates one focused invariant, not a replacement for framework integration tests.
public class Lab048 {
  static void check(boolean ok,String message){if(!ok)throw new AssertionError(message);System.out.println("PASS: "+message);}
  public static void main(String[] args) throws Exception {
    var value=new java.util.concurrent.atomic.AtomicInteger();try(var ex=java.util.concurrent.Executors.newVirtualThreadPerTaskExecutor()){var tasks=new java.util.ArrayList<java.util.concurrent.Future<?>>();for(int i=0;i<100;i++)tasks.add(ex.submit(value::incrementAndGet));for(var f:tasks)f.get();}check(value.get()==100,"atomic update avoids race");
  }
}
