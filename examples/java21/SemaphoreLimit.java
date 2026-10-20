import java.util.concurrent.*;
public class SemaphoreLimit {
  static final Semaphore permits = new Semaphore(2);
  static void call() throws InterruptedException {
    permits.acquire(); try { System.out.println("request allowed"); } finally { permits.release(); }
  }
  public static void main(String[] args) throws Exception { call(); }
}
