import java.util.*;
import java.util.concurrent.*;
import java.util.concurrent.atomic.*;
import java.util.function.LongSupplier;
public class TokenBucketDemo {
 static class Bucket {
  private final double capacity,perSecond;private final LongSupplier clock;private double tokens;private long last;
  Bucket(int capacity,double perSecond,LongSupplier clock){
   if(capacity<1||!Double.isFinite(perSecond)||perSecond<=0)throw new IllegalArgumentException();
   this.capacity=capacity;this.perSecond=perSecond;this.clock=Objects.requireNonNull(clock);tokens=capacity;last=clock.getAsLong();
  }
  synchronized boolean allow(int cost){
   if(cost<1)throw new IllegalArgumentException("positive cost required");long now=clock.getAsLong();long elapsed=now-last;
   if(elapsed>0){tokens=Math.min(capacity,tokens+elapsed/1_000_000_000.0*perSecond);last=now;}
   if(tokens<cost)return false;tokens-=cost;return true;
  }
 }
 // A fixed authenticated-tenant registry avoids unbounded attacker-created keys in this demo.
 record Limiter(Map<String,Bucket> configured){
  Limiter{configured=Map.copyOf(configured);}
  boolean allow(String trustedTenant,int cost){Bucket b=configured.get(trustedTenant);if(b==null)throw new IllegalArgumentException("unknown tenant");return b.allow(cost);}
 }
 static void check(boolean ok){if(!ok)throw new AssertionError();}
 public static void main(String[] args)throws Exception{
  AtomicLong time=new AtomicLong();Bucket b=new Bucket(2,1,time::get);check(b.allow(1));check(b.allow(1));check(!b.allow(1));
  time.addAndGet(500_000_000);check(!b.allow(1));time.addAndGet(500_000_000);check(b.allow(1));check(!b.allow(1));
  Bucket racing=new Bucket(10,1,time::get);AtomicInteger accepted=new AtomicInteger();
  try(var pool=Executors.newFixedThreadPool(8)){
   List<Future<?>> work=new ArrayList<>();for(int i=0;i<50;i++)work.add(pool.submit(()->{if(racing.allow(1))accepted.incrementAndGet();}));for(var f:work)f.get();
  }
  check(accepted.get()==10);
  Limiter limiter=new Limiter(Map.of("A",new Bucket(1,1,time::get),"B",new Bucket(1,1,time::get)));
  check(limiter.allow("A",1));check(!limiter.allow("A",1));check(limiter.allow("B",1));
  try{b.allow(0);throw new AssertionError();}catch(IllegalArgumentException expected){}
  System.out.println("PASS: burst/refill without sleeps, final-token concurrency, independent tenants and invalid cost");
 }
}
