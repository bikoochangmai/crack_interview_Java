import java.util.*;
public class Comparators {
  record Order(int priority, String id) implements Comparable<Order> {
    public int compareTo(Order other) { return id.compareTo(other.id); }
  }
  public static void main(String[] args) {
    List<Order> orders = new ArrayList<>(List.of(new Order(2,"b"),new Order(1,"a")));
    orders.sort(Comparator.comparingInt(Order::priority).thenComparing(Order::id));
    System.out.println(orders);
  }
}
