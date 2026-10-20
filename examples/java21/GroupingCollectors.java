import java.util.*;
import java.util.stream.*;
public class GroupingCollectors {
  record Finding(String team, boolean open) {}
  public static void main(String[] args) {
    var findings = List.of(new Finding("A",true),new Finding("B",false),new Finding("A",false));
    System.out.println(findings.stream().collect(Collectors.groupingBy(Finding::team)));
    System.out.println(findings.stream().collect(Collectors.partitioningBy(Finding::open)));
  }
}
