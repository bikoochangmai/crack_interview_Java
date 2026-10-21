# LC019 — Kth Largest Element in an Array

**Difficulty:** Medium · **Pattern:** Heap

## Problem

Return the kth largest value (including duplicates).

## Input, output and constraints

Nonempty array; 1 <= k <= n. Count duplicate values separately when ranking; return a value, not an index.

## Worked example

[3,2,1,5,6,4], k=2 → 5

## Brute-force baseline

Repeatedly scan for the largest unused position k times.

Time: **O(n·k)** · Space: **O(n)**

```java
import java.util.*;
class Solution {
public int findKthLargest(int[] nums,int k) {
 boolean[] used=new boolean[nums.length];int best=-1;
 for(int rank=0;rank<k;rank++) {
  best=-1;for(int i=0;i<nums.length;i++) if(!used[i] && (best<0 || nums[i]>nums[best])) best=i;
  used[best]=true;
 }return nums[best];
}
}
```

## Improved approach

Keep a min-heap with at most k elements.

## Step-by-step explanation

A min-heap of size k retains the k largest values seen. Its root is the smallest of those retained values, which is exactly the kth largest overall.

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

Time: **O(n log k)** · Space: **O(k)**

## Edge cases and interview discussion

[3,3,2], k=2 → 3; k=1; k=n; negative values.

Explain the baseline bottleneck, the improved invariant, and whether either solution mutates its input. A baseline can already be optimal in time (for example palindrome); the improvement may instead reduce memory. Exponential baselines are teaching examples for small inputs only.

[← All problems](README.md)
