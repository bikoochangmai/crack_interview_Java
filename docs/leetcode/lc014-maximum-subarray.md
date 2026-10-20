# LC014 — Maximum Subarray

**Difficulty:** Medium · **Pattern:** Dynamic Programming

## Problem

Find the largest sum of any nonempty contiguous subarray.

## Worked example

`[-2,1,-3,4,-1,2,1,-5,4] → 6`

## Approach

Kadane’s algorithm chooses to extend or restart the current subarray.

## Java solution

```java
import java.util.*;

class Solution {
    public int maxSubArray(int[] nums) {
        int current = nums[0], best = nums[0];
        for (int i = 1; i < nums.length; i++) {
            current = Math.max(nums[i], current + nums[i]);
            best = Math.max(best, current);
        }
        return best;
    }
}
```

## Complexity

- Time: **O(n)**
- Space: **O(1)**

[← All problems](README.md)
