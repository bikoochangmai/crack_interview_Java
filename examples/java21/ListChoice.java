import java.util.*;
public class ListChoice {
  public static void main(String[] args) {
    List<String> ids = new ArrayList<>(List.of("a","b","c"));
    System.out.println(ids.get(1));
    Deque<String> queue = new ArrayDeque<>(ids);
    while (!queue.isEmpty()) System.out.println(queue.removeFirst());
  }
}
