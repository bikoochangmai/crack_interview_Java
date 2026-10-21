# LC001 — Two Sum

**Difficulty:** Easy · **Pattern:** Array / HashMap

## Problem

Return indices of two numbers whose sum equals target.

## Input, output and constraints

At least two integers; exactly one pair exists. Return zero-based indices in either order; never reuse an index.

## Worked example

nums=[2,7,11,15], target=9 → [0,1]

## Brute-force baseline

Compare every pair of distinct indices.

Time: **O(n²)** · Space: **O(1)**

```java
import java.util.*;
class Solution {
public int[] twoSum(int[] nums, int target) {
 for(int i=0;i<nums.length;i++) for(int j=i+1;j<nums.length;j++)
  if(nums[i]+nums[j]==target) return new int[]{i,j};
 return new int[0];
}
}
```

## Improved approach

Store previously seen values in a map and look up the complement.

## Step-by-step explanation

For [2,7,11,15], store 2 at index 0. At index 1 the complement is 2, so return [0,1]. Look up before inserting to avoid reusing the current index.

## Java solution

```java
import java.util.*;
class Solution {
public int[] twoSum(int[] nums, int target) {
    Map<Integer, Integer> seen = new HashMap<>();
    for (int i = 0; i < nums.length; i++) {
        int need = target - nums[i];
        if (seen.containsKey(need)) return new int[]{seen.get(need), i};
        seen.put(nums[i], i);
    }
    return new int[0];
}
}
```

## Complexity

Time: **O(n)** · Space: **O(n)**

## Edge cases and interview discussion

[3,3], target=6 → [0,1]; negative values; pair at the end.

Explain the baseline bottleneck, the improved invariant, and whether either solution mutates its input. A baseline can already be optimal in time (for example palindrome); the improvement may instead reduce memory. Exponential baselines are teaching examples for small inputs only.

[← All problems](README.md)
