public class ThreadLocalCleanup {
  static final ThreadLocal<String> trace = new ThreadLocal<>();
  public static void main(String[] args) {
    trace.set("trace-1");
    try { System.out.println(trace.get()); }
    finally { trace.remove(); }
  }
}
