import java.util.*;
public class SequencedCollections {
  public static void main(String[] args) {
    SequencedCollection<String> events = new ArrayList<>(List.of("created","paid","shipped"));
    System.out.println(events.getFirst()); System.out.println(events.reversed());
  }
}
