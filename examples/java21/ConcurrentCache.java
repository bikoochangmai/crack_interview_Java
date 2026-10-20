import java.util.concurrent.*;
import java.util.concurrent.atomic.*;
public class ConcurrentCache {
  public static void main(String[] args) {
    var counts = new ConcurrentHashMap<String,LongAdder>();
    counts.computeIfAbsent("tenant-a", key -> new LongAdder()).increment();
    System.out.println(counts.get("tenant-a").sum());
  }
}
