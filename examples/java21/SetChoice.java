import java.util.*;
public class SetChoice {
  public static void main(String[] args) {
    List<String> values = List.of("b","a","b");
    System.out.println(new HashSet<>(values));
    System.out.println(new LinkedHashSet<>(values));
    System.out.println(new TreeSet<>(values));
  }
}
