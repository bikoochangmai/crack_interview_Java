# LC013 — Search in Rotated Sorted Array

**Difficulty:** Medium · **Pattern:** Binary Search

## Problem

Find a target in a distinct-value sorted array rotated at a pivot.

## Input, output and constraints

Input was strictly ascending before rotation; all values are distinct. Return target index or -1 in O(log n) for the improved solution.

## Worked example

[4,5,6,7,0,1,2], target=0 → 4

## Brute-force baseline

Ignore the rotation and scan every position.

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

At each step identify the sorted half and discard the other.

## Step-by-step explanation

For [4,5,6,7,0,1,2] and target 0, the left half through 7 is sorted but cannot contain 0. Search the right half. Distinct values make this choice unambiguous.

## Java solution

```java
import java.util.*;
class Solution {
public int search(int[] nums, int target) {
    int l=0, r=nums.length-1;
    while (l<=r) {
        int m=l+(r-l)/2;
        if (nums[m]==target) return m;
        if (nums[l]<=nums[m]) {
            if (nums[l]<=target && target<nums[m]) r=m-1;
            else l=m+1;
        } else {
            if (nums[m]<target && target<=nums[r]) l=m+1;
            else r=m-1;
        }
    }
    return -1;
}
}
```

## Complexity

Time: **O(log n)** · Space: **O(1)**

## Edge cases and interview discussion

Unrotated input; singleton; absent target. Duplicates require a different algorithm and may cause linear behavior.

Explain the baseline bottleneck, the improved invariant, and whether either solution mutates its input. A baseline can already be optimal in time (for example palindrome); the improvement may instead reduce memory. Exponential baselines are teaching examples for small inputs only.

[← All problems](README.md)
