import java.util.*;
import java.util.function.*;
public class Lambdas {
  public static void main(String[] args) {
    Predicate<String> valid = s -> s != null && !s.isBlank();
    System.out.println(List.of("", "approved").stream().filter(valid).toList());
  }
}
