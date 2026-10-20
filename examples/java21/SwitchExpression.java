public class SwitchExpression {
  static int fee(String tier) { return switch(tier) { case "GOLD" -> 0; case "SILVER" -> 5; default -> 10; }; }
  public static void main(String[] args) { System.out.println(fee("GOLD")); }
}
