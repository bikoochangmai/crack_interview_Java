# LC005 — Top K Frequent Elements

**Difficulty:** Medium · **Pattern:** HashMap / Heap

## Problem

Return the k numbers with the highest occurrence counts.

## Input, output and constraints

Nonempty integer array; 1 <= k <= distinct values. Assume the top-k set is unique; output order does not matter.

## Worked example

[1,1,1,2,2,3], k=2 → [1,2]

## Brute-force baseline

For each distinct value, scan the entire input to count it, then repeatedly pick the largest remaining count.

Time: **O(n²)** · Space: **O(n)**

```java
import java.util.*;
class Solution {
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
}
```

## Improved approach

Count frequencies and maintain a min-heap of size k.

## Step-by-step explanation

Counts are {1:3,2:2,3:1}. A heap capped at k removes the least frequent candidate, retaining 1 and 2 for k=2.

## Java solution

```java
import java.util.*;
class Solution {
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
}
```

## Complexity

Time: **O(n log k)** · Space: **O(n)**

## Edge cases and interview discussion

k=1; all values equal; k equals distinct count. Heap output is not necessarily sorted.

Explain the baseline bottleneck, the improved invariant, and whether either solution mutates its input. A baseline can already be optimal in time (for example palindrome); the improvement may instead reduce memory. Exponential baselines are teaching examples for small inputs only.

[← All problems](README.md)
