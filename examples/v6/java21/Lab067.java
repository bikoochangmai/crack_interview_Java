// Java 21, standard library only. Compile: javac Lab067.java ; run: java Lab067
// Demonstrates one focused invariant, not a replacement for framework integration tests.
public class Lab067 {
  static void check(boolean ok,String message){if(!ok)throw new AssertionError(message);System.out.println("PASS: "+message);}
  public static void main(String[] args) throws Exception {
    record Properties(boolean enabled){}var config=new Properties(true);String bean=config.enabled()?"auto-configured":"disabled";check(bean.equals("auto-configured"),"conditional configuration concept");
  }
}
