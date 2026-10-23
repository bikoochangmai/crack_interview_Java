# Mock interview: DSA / Coding

Attempt each prompt before expanding/reading its solution. These are original model answers, not alleged company questions or claimed personal experiences. For behavioral/day-to-day examples, fill the structure with facts from your own work. Banking designs are engineering exercises; actual rail, security and control requirements must be established with the responsible owners.

[All mock rounds](README.md) · [LLD / HLD paths](../lld-hld-learning-path.md)

## 1. Two Sum and its variants

### Interview prompt and example

nums=[2,7,11,15], target=9 → [0,1]

### Clarify and solve

Return indices of two numbers whose sum equals target. At least two integers; exactly one pair exists. Return zero-based indices in either order; never reuse an index.

### Brute force

Compare every pair of distinct indices. Time O(n²); space O(1).

### Improved solution and invariant

Store previously seen values in a map and look up the complement. For [2,7,11,15], store 2 at index 0. At index 1 the complement is 2, so return [0,1]. Look up before inserting to avoid reusing the current index. Time O(n); space O(n).

### Boundary cases

[3,3], target=6 → [0,1]; negative values; pair at the end.

### Variants are different contracts

One pair of indices uses a complement map; sorted input permits two pointers. For unique value pairs, sort a copy and skip duplicate endpoint values after a match. Counting index pairs instead accumulates prior complement frequency: [1,1,1,1] with target 2 has six index pairs but one unique value pair. Use widened arithmetic for sums/complements. The runnable MockCodingDemo implements all four; a request for all output pairs may require quadratic output size.

### Brute-force Java baseline

Method snippet: place inside a class and import java.util.* where needed.

```java
public int[] twoSum(int[] nums, int target) {
 for(int i=0;i<nums.length;i++) for(int j=i+1;j<nums.length;j++)
  if((long)nums[i]+nums[j]==target) return new int[]{i,j};
 return new int[0];
}
```

### Java solution

Code is a complete lab where it declares a public class, otherwise a method/type snippet for a Solution class with java.util imports as needed.

```java
import java.util.*;
class Solution {
 static int[] twoSum(int[] nums,int target){
  Map<Long,Integer> seen=new HashMap<>();
  for(int i=0;i<nums.length;i++){long need=(long)target-nums[i];Integer j=seen.get(need);if(j!=null)return new int[]{j,i};seen.put((long)nums[i],i);}return new int[0];
 }
 // Precondition: nums is sorted ascending; result uses zero-based indices.
 static int[] sortedTwoSum(int[] nums,int target){int l=0,r=nums.length-1;while(l<r){long sum=(long)nums[l]+nums[r];if(sum==target)return new int[]{l,r};if(sum<target)l++;else r--;}return new int[0];}
 static List<List<Integer>> uniqueValuePairs(int[] nums,int target){
  int[] a=nums.clone();Arrays.sort(a);List<List<Integer>> out=new ArrayList<>();int l=0,r=a.length-1;
  while(l<r){long sum=(long)a[l]+a[r];if(sum<target)l++;else if(sum>target)r--;else{
   int x=a[l],y=a[r];out.add(List.of(x,y));while(l<r&&a[l]==x)l++;while(l<r&&a[r]==y)r--;
  }}return out;
 }
 static long countIndexPairs(int[] nums,int target){Map<Long,Long> counts=new HashMap<>();long result=0;for(int x:nums){result+=counts.getOrDefault((long)target-x,0L);counts.merge((long)x,1L,Long::sum);}return result;}

}
```

[Runnable lab source](../../examples/mock/MockCodingDemo.java)

```powershell
javac -d .pattern-classes examples/mock/MockCodingDemo.java
java -cp .pattern-classes MockCodingDemo
```

The local lab proves only its stated invariants, not external banking/hardware/broker behavior.

[Full coding walkthrough](../leetcode/lc001-two-sum.md)

### Interviewer follow-ups

- State the invariant without looking at code.

- Give an adversarial input, not just the supplied sample.

## 2. Merge overlapping intervals

### Interview prompt and example

[[1,3],[2,6],[8,10]] → [[1,6],[8,10]]

### Clarify and solve

Merge all overlapping closed intervals. Each closed interval has start <= end. Touching endpoints overlap. Return disjoint merged intervals; empty input is allowed.

### Brute force

Repeatedly scan all interval pairs and merge any overlap until no pair overlaps. Time O(n³) upper bound; space O(n).

### Improved solution and invariant

Sort by start and merge when the next interval overlaps. Sort by start. After [1,3] merges with [2,6], current becomes [1,6]. [8,10] cannot overlap it, so emit current. Sorting guarantees later starts cannot reconnect a finished interval. Time O(n log n); space O(n) output.

### Boundary cases

[[1,4],[4,5]] → [[1,5]]; nested intervals; optimized code sorts the input array.

### Brute-force Java baseline

Method snippet: place inside a class and import java.util.* where needed.

```java
public int[][] merge(int[][] intervals) {
 List<int[]> a=new ArrayList<>();for(int[] x:intervals) a.add(x.clone());
 boolean changed;
 do {changed=false;
  outer:for(int i=0;i<a.size();i++) for(int j=i+1;j<a.size();j++) {
   int[] x=a.get(i),y=a.get(j);
   if(x[0]<=y[1] && y[0]<=x[1]){x[0]=Math.min(x[0],y[0]);x[1]=Math.max(x[1],y[1]);a.remove(j);changed=true;break outer;}
  }
 }while(changed);
 return a.toArray(new int[0][]);
}
```

### Java solution

Code is a complete lab where it declares a public class, otherwise a method/type snippet for a Solution class with java.util imports as needed.

```java
public int[][] merge(int[][] intervals) {
    if (intervals.length==0) return new int[0][];
    Arrays.sort(intervals, Comparator.comparingInt(a -> a[0]));
    List<int[]> out=new ArrayList<>();
    int[] cur=intervals[0].clone();
    for (int i=1;i<intervals.length;i++) {
        if (intervals[i][0]<=cur[1]) cur[1]=Math.max(cur[1],intervals[i][1]);
        else { out.add(cur); cur=intervals[i].clone(); }
    }
    out.add(cur);
    return out.toArray(new int[0][]);
}
```

[Full coding walkthrough](../leetcode/lc018-merge-intervals.md)

### Interviewer follow-ups

- State the invariant without looking at code.

- Give an adversarial input, not just the supplied sample.

## 3. Validate balanced parentheses

### Interview prompt and example

"([]){}" → true

### Clarify and solve

Determine whether bracket characters are correctly nested and closed. Input contains only (), [] and {}. Every closer must match the most recent unmatched opener; empty input is valid.

### Brute force

Repeatedly remove adjacent matching bracket pairs until no change occurs. Time O(n²); space O(n).

### Improved solution and invariant

Push expected closing brackets and match them on encounter. A stack stores expected closing characters. In ([]){}, ] must close [ before ) can close (. A nonempty stack at the end means missing closers. Time O(n); space O(n).

### Boundary cases

"([)]" → false; "(" → false; "" → true.

### Brute-force Java baseline

Method snippet: place inside a class and import java.util.* where needed.

```java
public boolean isValid(String s) {
 while(true){String next=s.replace("()", "").replace("[]", "").replace("{}", "");if(next.equals(s)) return s.isEmpty();s=next;}
}
```

### Java solution

Code is a complete lab where it declares a public class, otherwise a method/type snippet for a Solution class with java.util imports as needed.

```java
public boolean isValid(String s) {
    Deque<Character> stack = new ArrayDeque<>();
    for (char c : s.toCharArray()) {
        if (c == '(') stack.push(')');
        else if (c == '[') stack.push(']');
        else if (c == '{') stack.push('}');
        else if (stack.isEmpty() || stack.pop() != c) return false;
    }
    return stack.isEmpty();
}
```

[Full coding walkthrough](../leetcode/lc011-valid-parentheses.md)

### Interviewer follow-ups

- State the invariant without looking at code.

- Give an adversarial input, not just the supplied sample.

## 4. LRU Cache from scratch

### Interview prompt and example

Capacity two: put(1,A), put(2,B), get(1), put(3,C). Key 2 must be evicted.

### State and invariant

Use HashMap<K,Node> plus a doubly linked recency list. Every real list node must have one map entry and matching forward/back links. Head is newest and tail is oldest; sentinels handle empty/single-entry boundaries.

### Operations

get misses without mutation or detaches/moves the found node to newest. put updates and refreshes an existing node; a new entry beyond capacity evicts the tail node from both list and map. Define zero capacity and null behavior explicitly.

### Complexity and safety

List work is O(1); hash-table operations are expected/amortized O(1), not a deterministic guarantee under arbitrary collisions. Space is O(capacity). A successful get changes order, so synchronize it with writes for an exact shared local LRU.

### Solution and tests

The linked runnable LruCacheDemo includes explicit nodes rather than delegating the implementation to LinkedHashMap. It tests update recency, zero capacity, list/map invariants and 1,000 deterministic operations against an independent access-ordered reference model.

### Java solution

Code is a complete lab where it declares a public class, otherwise a method/type snippet for a Solution class with java.util imports as needed.

```java
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
```

[Runnable lab source](../../examples/lld/LruCacheDemo.java)

```powershell
javac -d .pattern-classes examples/lld/LruCacheDemo.java
java -cp .pattern-classes LruCacheDemo
```

The local lab proves only its stated invariants, not external banking/hardware/broker behavior.

### Interviewer follow-ups

- Why does get need synchronization?

- What changes if values expire independently of recency?

## 5. Top K frequent elements

### Interview prompt and example

[1,1,1,2,2,3], k=2 → [1,2]

### Clarify and solve

Return the k numbers with the highest occurrence counts. Nonempty integer array; 1 <= k <= distinct values. Assume the top-k set is unique; output order does not matter.

### Brute force

For each distinct value, scan the entire input to count it, then repeatedly pick the largest remaining count. Time O(n²); space O(n).

### Improved solution and invariant

Count frequencies and maintain a min-heap of size k. Counts are {1:3,2:2,3:1}. A heap capped at k removes the least frequent candidate, retaining 1 and 2 for k=2. Time O(n log k); space O(n).

### Boundary cases

k=1; all values equal; k equals distinct count. Heap output is not necessarily sorted.

### Brute-force Java baseline

Method snippet: place inside a class and import java.util.* where needed.

```java
public int[] topKFrequent(int[] nums,int k) {
 List<Integer> values=new ArrayList<>();
 for(int x:nums) if(!values.contains(x)) values.add(x);
 int[] counts=new int[values.size()];
 for(int i=0;i<values.size();i++) for(int x:nums) if(x==values.get(i)) counts[i]++;
 int[] out=new int[k];
 for(int j=0;j<k;j++) {
  int best=0;for(int i=1;i<counts.length;i++) if(counts[i]>counts[best]) best=i;
  out[j]=values.get(best); counts[best]=-1;
 } return out;
}
```

### Java solution

Code is a complete lab where it declares a public class, otherwise a method/type snippet for a Solution class with java.util imports as needed.

```java
public int[] topKFrequent(int[] nums, int k) {
    Map<Integer, Integer> freq = new HashMap<>();
    for (int n : nums) freq.merge(n, 1, Integer::sum);
    PriorityQueue<Integer> heap = new PriorityQueue<>(Comparator.comparingInt(freq::get));
    for (int n : freq.keySet()) {
        heap.offer(n);
        if (heap.size() > k) heap.poll();
    }
    int[] out = new int[k];
    for (int i = 0; i < k; i++) out[i] = heap.poll();
    return out;
}
```

[Full coding walkthrough](../leetcode/lc005-top-k-frequent-elements.md)

### Interviewer follow-ups

- State the invariant without looking at code.

- Give an adversarial input, not just the supplied sample.

## 6. Detect a cycle in a linked list

### Interview prompt and example

Nodes A → B → C → B have cycle entry B. Equal node values alone do not mean a cycle.

### Brute force

Walk the nodes while storing object identities in a set. A repeated node reference reveals the cycle; null ends an acyclic list. Time O(n), extra space O(n). Use reference identity rather than value equality.

### Floyd solution

Advance slow by one and fast by two. In a finite cycle their relative distance moves by one modulo cycle length and eventually becomes zero. Stop only after checking fast and fast.next for null.

### Find the entry

After a meeting, start one pointer at head and advance both by one until they meet at the entry. If the prefix length is mu and cycle length lambda, the meeting-distance relation implies mu steps align their cycle positions. Detection plus entry recovery is O(n) time and O(1) extra space.

### Adversarial tests

Test null, one node with null next, self-loop, a cycle beginning at head, a nonempty prefix, and distinct nodes with equal values. Never modify next links merely to mark visited nodes.

### Java solution

Code is a complete lab where it declares a public class, otherwise a method/type snippet for a Solution class with java.util imports as needed.

```java
static class Node {int value; Node next;}
static Node cycleEntry(Node head) {
 Node slow=head, fast=head;
 while(fast!=null && fast.next!=null) {
  slow=slow.next; fast=fast.next.next;
  if(slow==fast) {
   Node start=head;
   while(start!=slow) {start=start.next; slow=slow.next;}
   return start;
  }
 }
 return null;
}
```

[Runnable lab source](../../examples/mock/MockCodingDemo.java)

```powershell
javac -d .pattern-classes examples/mock/MockCodingDemo.java
java -cp .pattern-classes MockCodingDemo
```

The local lab proves only its stated invariants, not external banking/hardware/broker behavior.

### Interviewer follow-ups

- Prove why the pointers meet inside a cycle.

- How would you calculate the cycle length?

## 7. Number of islands

### Interview prompt and example

[["1","1","0"],["0","1","0"],["0","0","1"]] → 2

### Clarify and solve

Count connected groups of land cells in a 2D grid (4-directional adjacency). Rectangular grid contains only 0 water and 1 land. Count components joined horizontally or vertically; diagonal contact does not join islands.

### Brute force

For every unassigned land cell repeatedly rescan the grid to expand its component until no adjacent land can be added. Time O((rows·cols)²) upper bound; space O(rows·cols).

### Improved solution and invariant

Flood-fill each unvisited land cell using an explicit stack. Flood-fill marks land when pushing it, so each cell enters the stack once. The sample has one three-cell component and one isolated cell. The optimized solution mutates land to water; copy the grid if needed. Time O(rows × cols); space O(rows × cols).

### Boundary cases

Empty grid → 0; all water → 0; diagonal land → separate islands; a long narrow island.

### Brute-force Java baseline

Method snippet: place inside a class and import java.util.* where needed.

```java
public int numIslands(char[][] grid) {
 if(grid.length==0) return 0;
 int rows=grid.length,cols=grid[0].length,count=0;
 int[][] label=new int[rows][cols];int[][] dirs={{1,0},{-1,0},{0,1},{0,-1}};
 for(int r=0;r<rows;r++) for(int c=0;c<cols;c++) {
  if(grid[r][c]!='1' || label[r][c]!=0) continue;
  label[r][c]=++count;boolean changed;
  do {changed=false;
   for(int i=0;i<rows;i++) for(int j=0;j<cols;j++) {
    if(grid[i][j]!='1' || label[i][j]!=0) continue;
    for(int[] d:dirs){int a=i+d[0],b=j+d[1];
     if(a>=0 && a<rows && b>=0 && b<cols && label[a][b]==count){label[i][j]=count;changed=true;break;}}
   }
  } while(changed);
 }return count;
}
```

### Java solution

Code is a complete lab where it declares a public class, otherwise a method/type snippet for a Solution class with java.util imports as needed.

```java
public int numIslands(char[][] grid) {
    if (grid.length == 0) return 0;
    int rows=grid.length, cols=grid[0].length, count=0;
    int[][] dirs={{1,0},{-1,0},{0,1},{0,-1}};
    for (int r=0;r<rows;r++) for (int c=0;c<cols;c++) {
        if (grid[r][c]!='1') continue;
        count++;
        Deque<int[]> stack=new ArrayDeque<>();
        stack.push(new int[]{r,c}); grid[r][c]='0';
        while (!stack.isEmpty()) {
            int[] p=stack.pop();
            for (int[] d:dirs) {
                int nr=p[0]+d[0], nc=p[1]+d[1];
                if (nr>=0 && nr<rows && nc>=0 && nc<cols && grid[nr][nc]=='1') {
                    grid[nr][nc]='0'; stack.push(new int[]{nr,nc});
                }
            }
        }
    }
    return count;
}
```

[Full coding walkthrough](../leetcode/lc017-number-of-islands.md)

### Interviewer follow-ups

- State the invariant without looking at code.

- Give an adversarial input, not just the supplied sample.

## 8. Best time to buy and sell stock

### Interview prompt and example

[7,1,5,3,6,4] → 5

### Clarify and solve

Maximize profit from one buy followed by one sell. Non-null array of nonnegative daily prices. Choose at most one buy and a strictly later sell; return zero if no profit exists.

### Brute force

Try all buy/sell day pairs. Time O(n²); space O(1).

### Improved solution and invariant

Track the lowest price seen and best profit so far. With [7,1,5,3,6,4], the minimum becomes 1 and selling at 6 yields 5. Keeping only the minimum eliminates repeated earlier-day scans. Time O(n); space O(1).

### Boundary cases

Descending prices → 0; empty or singleton → 0; equal prices.

### Brute-force Java baseline

Method snippet: place inside a class and import java.util.* where needed.

```java
public int maxProfit(int[] prices) {
 int best=0;for(int i=0;i<prices.length;i++) for(int j=i+1;j<prices.length;j++) best=Math.max(best,prices[j]-prices[i]);return best;
}
```

### Java solution

Code is a complete lab where it declares a public class, otherwise a method/type snippet for a Solution class with java.util imports as needed.

```java
public int maxProfit(int[] prices) {
    int min = Integer.MAX_VALUE, best = 0;
    for (int p : prices) { min = Math.min(min, p); best = Math.max(best, p-min); }
    return best;
}
```

[Full coding walkthrough](../leetcode/lc009-best-time-to-buy-and-sell-stock.md)

### Interviewer follow-ups

- State the invariant without looking at code.

- Give an adversarial input, not just the supplied sample.

## Reference documentation

- [Java collection contracts](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/package-summary.html)
