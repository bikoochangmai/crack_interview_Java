import java.util.concurrent.*;
public class CallableExample {
  public static void main(String[] args) throws Exception {
    try (ExecutorService executor = Executors.newSingleThreadExecutor()) {
      Future<Integer> result = executor.submit(() -> 40 + 2);
      System.out.println(result.get());
    }
  }
}
