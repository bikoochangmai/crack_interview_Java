import java.util.*;
public class OptionalReturn {
  static Optional<String> findEmail(Map<Long,String> db, long id) { return Optional.ofNullable(db.get(id)); }
  public static void main(String[] args) {
    String email = findEmail(Map.of(1L,"a@example.test"),2L).orElse("unknown");
    System.out.println(email);
  }
}
