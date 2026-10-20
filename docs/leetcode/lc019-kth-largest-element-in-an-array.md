# LC019 — Kth Largest Element in an Array

**Difficulty:** Medium · **Pattern:** Heap

## Problem

Return the kth largest value (including duplicates).

## Worked example

`[3,2,1,5,6,4], k=2 → 5`

## Approach

Keep a min-heap with at most k elements.

## Java solution

```java
import java.util.*;

class Solution {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> pq=new PriorityQueue<>();
        for (int n:nums) { pq.offer(n); if (pq.size()>k) pq.poll(); }
        return pq.peek();
    }
}
```

## Complexity

- Time: **O(n log k)**
- Space: **O(k)**

[← All problems](README.md)
