public class PatternSwitch {
  static String describe(Object value) { return switch(value) {
    case Integer n -> "number:" + n;
    case String s -> "text:" + s;
    case null -> "missing";
    default -> "other";
  }; }
  public static void main(String[] args) { System.out.println(describe(42)); }
}
