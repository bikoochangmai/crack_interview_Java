public class TokenBucket {
  private final long capacity; private long tokens; private long lastNanos;
  TokenBucket(long capacity) { this.capacity=capacity; this.tokens=capacity; this.lastNanos=System.nanoTime(); }
  synchronized boolean allow() {
    long now=System.nanoTime(); long refill=(now-lastNanos)/1_000_000_000L;
    if (refill>0) { tokens=Math.min(capacity,tokens+refill); lastNanos+=refill*1_000_000_000L; }
    if (tokens==0) return false; tokens--; return true;
  }
  public static void main(String[] args) { var bucket=new TokenBucket(2); System.out.println(bucket.allow()+" "+bucket.allow()+" "+bucket.allow()); }
}
