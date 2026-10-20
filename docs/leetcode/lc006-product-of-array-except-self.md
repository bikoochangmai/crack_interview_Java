# LC006 — Product of Array Except Self

**Difficulty:** Medium · **Pattern:** Array / Prefix

## Problem

Compute each index’s product of all other values without division.

## Worked example

`[1,2,3,4] → [24,12,8,6]`

## Approach

Multiply prefix products and then suffix products.

## Java solution

```java
import java.util.*;

class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] out = new int[nums.length];
        int prefix = 1;
        for (int i = 0; i < nums.length; i++) { out[i] = prefix; prefix *= nums[i]; }
        int suffix = 1;
        for (int i = nums.length - 1; i >= 0; i--) { out[i] *= suffix; suffix *= nums[i]; }
        return out;
    }
}
```

## Complexity

- Time: **O(n)**
- Space: **O(1) extra excluding output**

[← All problems](README.md)
