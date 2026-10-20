public class RecordPattern {
  record Customer(String id, int points) {}
  public static void main(String[] args) {
    Object obj = new Customer("C-1", 100);
    if (obj instanceof Customer(String id, int points)) System.out.println(id + ":" + points);
  }
}
