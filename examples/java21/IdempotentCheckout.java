import java.util.*;
public class IdempotentCheckout {
  record Receipt(String id, long amount) {}
  private final Map<String,Receipt> receipts = new HashMap<>();
  synchronized Receipt charge(String key, long amount) {
    Receipt existing = receipts.get(key);
    if (existing != null) {
      if (existing.amount() != amount) throw new IllegalArgumentException("Key reused with different amount");
      return existing;
    }
    Receipt r = new Receipt(UUID.randomUUID().toString(),amount);
    receipts.put(key,r); return r;
  }
  public static void main(String[] args) {
    var api = new IdempotentCheckout();
    System.out.println(api.charge("request-1",500).equals(api.charge("request-1",500)));
  }
}
