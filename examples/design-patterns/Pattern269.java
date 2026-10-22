import java.util.concurrent.atomic.AtomicInteger;
public class Pattern269 {
 interface Documents {String read(String id);}
 static class LegacySdk {String fetchNumeric(int id){return "document:"+id;}}
 // Adapter changes the interface (String ID to legacy numeric ID).
 record LegacyAdapter(LegacySdk sdk) implements Documents {
  public String read(String id){return sdk.fetchNumeric(Integer.parseInt(id));}
 }
 // Decorator keeps the same interface and wraps behavior.
 record MeteredDocuments(Documents delegate,AtomicInteger calls) implements Documents {
  public String read(String id){calls.incrementAndGet();return delegate.read(id);}
 }
 // Facade exposes one convenient use case across several operations.
 record PreviewFacade(Documents documents) {
  String preview(String id){return documents.read(id).toUpperCase(java.util.Locale.ROOT);}
 }
 public static void main(String[] args){
  var calls=new AtomicInteger();
  Documents docs=new MeteredDocuments(new LegacyAdapter(new LegacySdk()),calls);
  String preview=new PreviewFacade(docs).preview("42");
  if(!preview.equals("DOCUMENT:42")||calls.get()!=1)throw new AssertionError();
  try{docs.read("bad-id");throw new AssertionError();}catch(NumberFormatException expected){}
  if(calls.get()!=2)throw new AssertionError("attempts include failures");
  System.out.println("PASS: facade delegates through decorator and adapter");
 }
}
