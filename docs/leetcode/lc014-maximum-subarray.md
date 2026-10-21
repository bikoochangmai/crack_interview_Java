# LC014 — Maximum Subarray

**Difficulty:** Medium · **Pattern:** Dynamic Programming

## Problem

Find the largest sum of any nonempty contiguous subarray.

## Input, output and constraints

Input has at least one integer. Return the largest sum of a nonempty contiguous subarray. Assume relevant sums fit int.

## Worked example

[-2,1,-3,4,-1,2,1,-5,4] → 6

## Brute-force baseline

Enumerate every start/end pair and maintain a running sum for each start.

Time: **O(n²)** · Space: **O(1)**

```java
import java.util.*;
class Solution {
public int maxSubArray(int[] nums) {
 int best=nums[0];for(int i=0;i<nums.length;i++){int sum=0;for(int j=i;j<nums.length;j++){sum+=nums[j];best=Math.max(best,sum);}}return best;
}
}
```

## Improved approach

Kadane’s algorithm chooses to extend or restart the current subarray.

## Step-by-step explanation

At each index Kadane keeps the best sum ending exactly there: extend the previous segment or start at the current value. [4,-1,2,1] sums to 6.

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

Time: **O(n)** · Space: **O(1)**

## Edge cases and interview discussion

[-3,-1,-2] → -1, not zero; singleton; all zeros.

Explain the baseline bottleneck, the improved invariant, and whether either solution mutates its input. A baseline can already be optimal in time (for example palindrome); the improvement may instead reduce memory. Exponential baselines are teaching examples for small inputs only.

[← All problems](README.md)
