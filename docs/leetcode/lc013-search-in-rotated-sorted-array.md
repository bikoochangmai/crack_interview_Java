# LC013 — Search in Rotated Sorted Array

**Difficulty:** Medium · **Pattern:** Binary Search

## Problem

Find a target in a distinct-value sorted array rotated at a pivot.

## Worked example

`[4,5,6,7,0,1,2], target=0 → 4`

## Approach

At each step identify the sorted half and discard the other.

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

- Time: **O(log n)**
- Space: **O(1)**

[← All problems](README.md)
