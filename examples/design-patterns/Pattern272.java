import java.util.*;
import java.util.function.Predicate;
public class Pattern272 {
 record Audit(long id,String owner,String status){}
 interface Audits {List<Audit> matching(Predicate<Audit> specification);void save(Audit audit);}
 // Teaching model of staged changes. Not a database/ORM or concurrency implementation.
 static class UnitOfWork implements Audits,AutoCloseable {
  final List<Audit> database;final List<Audit> pending=new ArrayList<>();
  UnitOfWork(List<Audit> database){this.database=database;}
  public void save(Audit audit){pending.add(audit);}
  public List<Audit> matching(Predicate<Audit> spec){return database.stream().filter(spec).toList();}
  void commit(){database.addAll(pending);pending.clear();}
  public void close(){pending.clear();} // discard uncommitted changes
 }
 public static void main(String[] args){
  var rows=new ArrayList<Audit>();
  try(var work=new UnitOfWork(rows)){work.save(new Audit(1,"alice","OPEN"));work.commit();}
  try(var work=new UnitOfWork(rows)){work.save(new Audit(2,"bob","OPEN"));} // no commit
  Predicate<Audit> owned=a->a.owner().equals("alice");Predicate<Audit> open=a->a.status().equals("OPEN");
  try(var work=new UnitOfWork(rows)){
   if(work.matching(owned.and(open)).size()!=1||rows.size()!=1)throw new AssertionError();
  }
  System.out.println("PASS: repository query, composed predicate, commit and discarded staging");
 }
}
