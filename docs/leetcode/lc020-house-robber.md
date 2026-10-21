# LC020 — House Robber

**Difficulty:** Medium · **Pattern:** Dynamic Programming

## Problem

Maximize money from nonadjacent houses.

## Input, output and constraints

Non-null array of nonnegative house amounts. You may skip all houses; never select adjacent positions. Return maximum money; totals fit int.

## Worked example

[2,7,9,3,1] → 12

## Brute-force baseline

At each index explore both skipping this house and taking it then skipping its neighbor.

Time: **O(2^n) upper bound** · Space: **O(n) recursion stack**

```java
import java.util.*;
class Solution {
public int rob(int[] nums) {return choose(nums,0);}
private int choose(int[] nums,int i) {
 if(i>=nums.length) return 0;return Math.max(choose(nums,i+1),nums[i]+choose(nums,i+2));
}
}
```

## Improved approach

At each house, choose between skipping it or adding it to the best two houses back.

## Step-by-step explanation

For [2,7,9,3,1], running best values become 2,7,11,11,12. Taking a house uses the best two positions back; skipping uses the previous best.

## Java solution

```java
import java.util.*;
class Solution {
public int rob(int[] nums) {
    int prev2=0, prev1=0;
    for (int n:nums) { int next=Math.max(prev1,prev2+n); prev2=prev1; prev1=next; }
    return prev1;
}
}
```

## Complexity

Time: **O(n)** · Space: **O(1)**

## Edge cases and interview discussion

[] → 0; [5] → 5; [2,1,1,2] → 4; all zeros.

Explain the baseline bottleneck, the improved invariant, and whether either solution mutates its input. A baseline can already be optimal in time (for example palindrome); the improvement may instead reduce memory. Exponential baselines are teaching examples for small inputs only.

[← All problems](README.md)
