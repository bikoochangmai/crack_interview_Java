import java.util.*;
public class LruCacheDemo {
 static class Lru<K,V> {
  private static class Node<K,V>{K key;V value;Node<K,V> prev,next;Node(K k,V v){key=k;value=v;}}
  private final int capacity;private final Map<K,Node<K,V>> index=new HashMap<>();
  private final Node<K,V> head=new Node<>(null,null),tail=new Node<>(null,null);
  Lru(int capacity){if(capacity<0)throw new IllegalArgumentException();this.capacity=capacity;head.next=tail;tail.prev=head;}
  private void detach(Node<K,V> n){n.prev.next=n.next;n.next.prev=n.prev;}
  private void newest(Node<K,V> n){n.next=head.next;n.prev=head;head.next.prev=n;head.next=n;}
  synchronized Optional<V> get(K key){Objects.requireNonNull(key);Node<K,V> n=index.get(key);if(n==null)return Optional.empty();detach(n);newest(n);return Optional.of(n.value);}
  synchronized void put(K key,V value){Objects.requireNonNull(key);Objects.requireNonNull(value);
   Node<K,V> n=index.get(key);if(n!=null){n.value=value;detach(n);newest(n);return;}
   if(capacity==0)return;n=new Node<>(key,value);index.put(key,n);newest(n);
   if(index.size()>capacity){Node<K,V> old=tail.prev;detach(old);index.remove(old.key);}
  }
  synchronized void verify(){
   int count=0;Node<K,V> previous=head;
   for(Node<K,V> n=head.next;n!=tail;n=n.next){if(n.prev!=previous||index.get(n.key)!=n)throw new AssertionError();previous=n;if(++count>index.size())throw new AssertionError("cycle");}
   if(tail.prev!=previous||count!=index.size()||count>capacity)throw new AssertionError();
  }
 }
 static void check(boolean ok){if(!ok)throw new AssertionError();}
 public static void main(String[] args){
  Lru<Integer,String> cache=new Lru<>(2);cache.put(1,"A");cache.put(2,"B");cache.get(1);cache.put(3,"C");
  check(cache.get(2).isEmpty());check(cache.get(1).orElseThrow().equals("A"));cache.verify();
  cache.put(1,"A2");cache.put(4,"D");check(cache.get(3).isEmpty());check(cache.get(1).orElseThrow().equals("A2"));cache.verify();
  Lru<Integer,String> zero=new Lru<>(0);zero.put(1,"X");check(zero.get(1).isEmpty());zero.verify();
  Random random=new Random(81);Lru<Integer,Integer> actual=new Lru<>(5);
  LinkedHashMap<Integer,Integer> model=new LinkedHashMap<>(16,.75f,true);
  for(int i=0;i<1000;i++){
   int key=random.nextInt(12);
   if(random.nextBoolean()){int v=random.nextInt(100);actual.put(key,v);model.put(key,v);if(model.size()>5)model.remove(model.keySet().iterator().next());}
   else check(actual.get(key).equals(Optional.ofNullable(model.get(key))));
   actual.verify();
  }
  System.out.println("PASS: access/update recency, eviction, zero capacity, list invariants and reference-model comparison");
 }
}
