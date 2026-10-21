# LC006 — Product of Array Except Self

**Difficulty:** Medium · **Pattern:** Array / Prefix

## Problem

Compute each index’s product of all other values without division.

## Input, output and constraints

At least two integers; products of prefixes/suffixes fit int. Return one product per index, without division; zeros are allowed.

## Worked example

[1,2,3,4] → [24,12,8,6]

## Brute-force baseline

For each index multiply all other positions.

Time: **O(n²)** · Space: **O(1) extra excluding output**

```java
import java.util.*;
class Solution {
public int[] productExceptSelf(int[] nums) {
 int[] out=new int[nums.length];
 for(int i=0;i<nums.length;i++){out[i]=1;for(int j=0;j<nums.length;j++) if(i!=j) out[i]*=nums[j];}
 return out;
}
}
```

## Improved approach

Multiply prefix products and then suffix products.

## Step-by-step explanation

For [1,2,3,4], prefix values in output are [1,1,2,6]. A reverse suffix pass multiplies them by [24,12,4,1].

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

Time: **O(n)** · Space: **O(1) extra excluding output**

## Edge cases and interview discussion

[0,2,3] → [6,0,0]; two zeros → all zero; negative values.

Explain the baseline bottleneck, the improved invariant, and whether either solution mutates its input. A baseline can already be optimal in time (for example palindrome); the improvement may instead reduce memory. Exponential baselines are teaching examples for small inputs only.

[← All problems](README.md)
