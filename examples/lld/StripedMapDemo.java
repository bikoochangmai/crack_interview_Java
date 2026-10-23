import java.util.*;
import java.util.concurrent.*;
import java.util.concurrent.locks.*;
import java.util.function.BiFunction;
public class StripedMapDemo {
 static class Bucket<K,V>{final Map<K,V> values=new HashMap<>();final ReadWriteLock lock=new ReentrantReadWriteLock();}
 // Fixed stripes; not ConcurrentHashMap's implementation or performance contract.
 static class StripedMap<K,V>{
  private final List<Bucket<K,V>> buckets;
  StripedMap(int stripes){if(stripes<1)throw new IllegalArgumentException();buckets=new ArrayList<>();for(int i=0;i<stripes;i++)buckets.add(new Bucket<>());}
  private Bucket<K,V> bucket(K key){Objects.requireNonNull(key);return buckets.get(Math.floorMod(key.hashCode(),buckets.size()));}
  V get(K key){var b=bucket(key);b.lock.readLock().lock();try{return b.values.get(key);}finally{b.lock.readLock().unlock();}}
  void put(K key,V value){Objects.requireNonNull(value);var b=bucket(key);b.lock.writeLock().lock();try{b.values.put(key,value);}finally{b.lock.writeLock().unlock();}}
  V compute(K key,BiFunction<K,V,V> change){Objects.requireNonNull(change);var b=bucket(key);b.lock.writeLock().lock();try{
   V next=change.apply(key,b.values.get(key));if(next==null)b.values.remove(key);else b.values.put(key,next);return next;
  }finally{b.lock.writeLock().unlock();}}
  // Callbacks must not invoke this map (including snapshot) or block on external work.
  Map<K,V> snapshot(){for(var b:buckets)b.lock.readLock().lock();try{
   Map<K,V> copy=new HashMap<>();for(var b:buckets)copy.putAll(b.values);return Map.copyOf(copy);
  }finally{for(int i=buckets.size()-1;i>=0;i--)buckets.get(i).lock.readLock().unlock();}}
 }
 record Collision(String key){public int hashCode(){return Integer.MIN_VALUE;}}
 public static void main(String[] args)throws Exception{
  var map=new StripedMap<String,Integer>(8);map.put("count",0);
  try(var pool=Executors.newFixedThreadPool(8)){
   List<Future<?>> work=new ArrayList<>();for(int t=0;t<8;t++)work.add(pool.submit(()->{for(int i=0;i<1000;i++)map.compute("count",(k,v)->v+1);}));
   for(var f:work)f.get();
  }
  if(map.get("count")!=8000||map.snapshot().get("count")!=8000)throw new AssertionError();
  map.compute("count",(k,v)->null);if(map.get("count")!=null)throw new AssertionError();
  var collisions=new StripedMap<Collision,Integer>(3);collisions.put(new Collision("A"),1);collisions.put(new Collision("B"),2);
  if(collisions.get(new Collision("A"))!=1||collisions.get(new Collision("B"))!=2)throw new AssertionError();
  try{map.put("bad",null);throw new AssertionError();}catch(NullPointerException expected){}
  System.out.println("PASS: atomic increments, collision equality, MIN_VALUE hash, removal and consistent snapshot");
 }
}
