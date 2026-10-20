# LC012 — Binary Search

**Difficulty:** Easy · **Pattern:** Binary Search

## Problem

Find target in a sorted ascending array; return -1 if absent.

## Worked example

`[-1,0,3,5,9,12], target=9 → 4`

## Approach

Halve the remaining search range each step.

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

- Time: **O(log n)**
- Space: **O(1)**

[← All problems](README.md)
