import java.util.ArrayList;
import java.util.concurrent.*;

public class VirtualThreadDemo {
 public static void main(String[] args) throws Exception {
  var permits = new Semaphore(4); // simulated downstream capacity
  var results = new ArrayList<Future<String>>();
  try (var executor = Executors.newVirtualThreadPerTaskExecutor()) {
   for (int i = 0; i < 12; i++) {
    final int id = i;
    results.add(executor.submit(() -> {
     if (!permits.tryAcquire(1, TimeUnit.SECONDS))
      throw new TimeoutException("Downstream busy");
     try {
      Thread.sleep(20); // simulate waiting for I/O; no network needed
      return id + ": virtual=" + Thread.currentThread().isVirtual();
     } finally { permits.release(); }
    }));
   }
   try {
    for (var result : results) System.out.println(result.get(2, TimeUnit.SECONDS));
   } catch (InterruptedException e) {
    results.forEach(f -> f.cancel(true));
    Thread.currentThread().interrupt();
    throw e;
   } catch (ExecutionException | TimeoutException e) {
    results.forEach(f -> f.cancel(true));
    throw e;
   }
  } // close waits for tasks to finish
 }
}
