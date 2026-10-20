public class SealedTypes {
  sealed interface Result permits Success, Failure {}
  record Success(String id) implements Result {}
  record Failure(String reason) implements Result {}
  public static void main(String[] args) { Result r = new Success("ok"); System.out.println(r); }
}
