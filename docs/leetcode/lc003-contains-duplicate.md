# LC003 — Contains Duplicate

**Difficulty:** Easy · **Pattern:** Array / HashSet

## Problem

Determine whether any value occurs more than once.

## Input, output and constraints

Input is a non-null integer array. Return true if any two different positions contain equal values.

## Worked example

[1,2,3,1] → true

## Brute-force baseline

Compare every index with every later index.

Time: **O(n²)** · Space: **O(1)**

```java
import java.util.*;
class Solution {
public boolean containsDuplicate(int[] nums) {
 for(int i=0;i<nums.length;i++) for(int j=i+1;j<nums.length;j++)
  if(nums[i]==nums[j]) return true;
 return false;
}
}
```

## Improved approach

Insert into a set; a failed insertion reveals a duplicate.

## Step-by-step explanation

A HashSet contains precisely the previously visited values. In [1,2,3,1], the last insertion fails, revealing the duplicate.

## Java solution

```java
import java.util.*;
class Solution {
public boolean containsDuplicate(int[] nums) {
    Set<Integer> seen = new HashSet<>();
    for (int n : nums) if (!seen.add(n)) return true;
    return false;
}
}
```

## Complexity

Time: **O(n)** · Space: **O(n)**

## Edge cases and interview discussion

[] → false; [1] → false; [1,1] → true.

Explain the baseline bottleneck, the improved invariant, and whether either solution mutates its input. A baseline can already be optimal in time (for example palindrome); the improvement may instead reduce memory. Exponential baselines are teaching examples for small inputs only.

[← All problems](README.md)
