import java.util.*;
public class SecondHighestSalary {
  public static void main(String[] args) {
    var salaries = List.of(100,200,200,300);
    System.out.println(salaries.stream().distinct().sorted(Comparator.reverseOrder()).skip(1).findFirst());
  }
}
