import java.util.concurrent.*;
public class FutureRecovery {
  public static void main(String[] args) {
    CompletableFuture<String> result = CompletableFuture.<String>failedFuture(new RuntimeException("timeout"))
      .exceptionally(ex -> "cached-fallback");
    System.out.println(result.join());
  }
}
