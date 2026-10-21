# LC012 — Binary Search

**Difficulty:** Easy · **Pattern:** Binary Search

## Problem

Find target in a sorted ascending array; return -1 if absent.

## Input, output and constraints

Input is a distinct-value ascending integer array. Return the zero-based target index or -1; empty input is allowed.

## Worked example

[-1,0,3,5,9,12], target=9 → 4

## Brute-force baseline

Scan every index until the target is found.

Time: **O(n)** · Space: **O(1)**

```java
import java.util.*;
class Solution {
public int search(int[] nums,int target) {
 for(int i=0;i<nums.length;i++) if(nums[i]==target) return i;return -1;
}
}
```

## Improved approach

Halve the remaining search range each step.

## Step-by-step explanation

On [-1,0,3,5,9,12], midpoint 3 is too small for target 9. Discard indices 0..2, then locate 9 at index 4.

## Java solution

```java
import java.util.*;
class Solution {
public int search(int[] nums, int target) {
    int l = 0, r = nums.length - 1;
    while (l <= r) {
        int m = l + (r-l)/2;
        if (nums[m] == target) return m;
        if (nums[m] < target) l = m+1;
        else r = m-1;
    }
    return -1;
}
}
```

## Complexity

Time: **O(log n)** · Space: **O(1)**

## Edge cases and interview discussion

Empty array → -1; first/last index; absent target.

Explain the baseline bottleneck, the improved invariant, and whether either solution mutates its input. A baseline can already be optimal in time (for example palindrome); the improvement may instead reduce memory. Exponential baselines are teaching examples for small inputs only.

[← All problems](README.md)
