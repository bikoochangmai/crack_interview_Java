import java.util.*;
public class Pattern273 {
 interface Documents {String read(String id);}
 record Router(Documents legacy,Documents modern,Set<String> migrated) implements Documents {
  Router{migrated=Set.copyOf(migrated);}
  public String read(String id){return (migrated.contains(id)?modern:legacy).read(id);}
 }
 public static void main(String[] args){
  Documents legacy=id->"legacy:"+id,modern=id->"modern:"+id;
  Documents canary=new Router(legacy,modern,Set.of("42"));
  if(!canary.read("42").equals("modern:42")||!canary.read("7").equals("legacy:7"))throw new AssertionError();
  Documents rollback=new Router(legacy,modern,Set.of());
  if(!rollback.read("42").equals("legacy:42"))throw new AssertionError();
  // Only route rollback is demonstrated. Data parity and write ownership need a separate protocol.
  System.out.println("PASS: migrated routing, legacy routing and route-only rollback");
 }
}
