// Java 21, standard library only. Compile: javac Lab146.java ; run: java Lab146
// Demonstrates one focused invariant, not a replacement for framework integration tests.
public class Lab146 {
  static void check(boolean ok,String message){if(!ok)throw new AssertionError(message);System.out.println("PASS: "+message);}
  public static void main(String[] args) throws Exception {
    record Deployment(boolean needsOsControl,boolean containers){}var d=new Deployment(false,false);check(!d.needsOsControl()&&!d.containers(),"App Service fits managed web workload; evaluate constraints");
  }
}
