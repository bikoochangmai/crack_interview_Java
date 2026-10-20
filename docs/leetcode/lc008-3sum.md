# LC008 — 3Sum

**Difficulty:** Medium · **Pattern:** Two Pointers / Sorting

## Problem

Find unique triples of numbers summing to zero.

## Worked example

`[-1,0,1,2,-1,-4] → [[-1,-1,2],[-1,0,1]]`

## Approach

Sort; fix one element and sweep the remaining pair.

## Java solution

```java
import java.util.*;

class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> out = new ArrayList<>();
        for (int i = 0; i < nums.length - 2; i++) {
            if (i > 0 && nums[i] == nums[i-1]) continue;
            int l = i+1, r = nums.length-1;
            while (l < r) {
                int sum = nums[i] + nums[l] + nums[r];
                if (sum < 0) l++;
                else if (sum > 0) r--;
                else {
                    out.add(Arrays.asList(nums[i], nums[l], nums[r]));
                    l++; r--;
                    while (l < r && nums[l] == nums[l-1]) l++;
                    while (l < r && nums[r] == nums[r+1]) r--;
                }
            }
        }
        return out;
    }
}
```

## Complexity

- Time: **O(n²)**
- Space: **O(1) extra excluding output/sort**

[← All problems](README.md)
