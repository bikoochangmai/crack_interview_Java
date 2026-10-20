# LC005 — Top K Frequent Elements

**Difficulty:** Medium · **Pattern:** HashMap / Heap

## Problem

Return the k numbers with the highest occurrence counts.

## Worked example

`[1,1,1,2,2,3], k=2 → [1,2]`

## Approach

Count frequencies and maintain a min-heap of size k.

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

- Time: **O(n log k)**
- Space: **O(n)**

[← All problems](README.md)
