# LC001 — Two Sum

**Difficulty:** Easy · **Pattern:** Array / HashMap

## Problem

Return indices of two numbers whose sum equals target.

## Worked example

`nums=[2,7,11,15], target=9 → [0,1]`

## Approach

Store previously seen values in a map and look up the complement.

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

- Time: **O(n)**
- Space: **O(n)**

[← All problems](README.md)
