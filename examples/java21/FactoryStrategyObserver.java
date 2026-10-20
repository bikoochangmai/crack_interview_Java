import java.util.*;
public class FactoryStrategyObserver {
  interface Discount { int apply(int cents); }
  static Discount factory(String tier) { return tier.equals("VIP") ? c -> c * 9 / 10 : c -> c; }
  interface Listener { void onPaid(String orderId); }
  public static void main(String[] args) {
    List<Listener> listeners = List.of(id -> System.out.println("Email receipt: " + id));
    int total = factory("VIP").apply(1000);
    if (total == 900) listeners.forEach(l -> l.onPaid("order-42"));
  }
}
