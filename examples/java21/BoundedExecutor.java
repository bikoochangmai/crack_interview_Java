import java.util.concurrent.*;
public class BoundedExecutor {
  public static void main(String[] args) throws Exception {
    try (ThreadPoolExecutor pool = new ThreadPoolExecutor(2,2,0,TimeUnit.SECONDS,
        new ArrayBlockingQueue<>(4),new ThreadPoolExecutor.CallerRunsPolicy())) {
      for (int i=0;i<8;i++) { final int id=i; pool.submit(() -> System.out.println("job-"+id)); }
    }
  }
}
