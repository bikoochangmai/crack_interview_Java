# LC009 — Best Time to Buy and Sell Stock

**Difficulty:** Easy · **Pattern:** Sliding Window / Array

## Problem

Maximize profit from one buy followed by one sell.

## Input, output and constraints

Non-null array of nonnegative daily prices. Choose at most one buy and a strictly later sell; return zero if no profit exists.

## Worked example

[7,1,5,3,6,4] → 5

## Brute-force baseline

Try all buy/sell day pairs.

Time: **O(n²)** · Space: **O(1)**

```java
import java.util.*;
class Solution {
public int maxProfit(int[] prices) {
 int best=0;for(int i=0;i<prices.length;i++) for(int j=i+1;j<prices.length;j++) best=Math.max(best,prices[j]-prices[i]);return best;
}
}
```

## Improved approach

Track the lowest price seen and best profit so far.

## Step-by-step explanation

With [7,1,5,3,6,4], the minimum becomes 1 and selling at 6 yields 5. Keeping only the minimum eliminates repeated earlier-day scans.

## Java solution

```java
import java.util.*;
class Solution {
public int maxProfit(int[] prices) {
    int min = Integer.MAX_VALUE, best = 0;
    for (int p : prices) { min = Math.min(min, p); best = Math.max(best, p-min); }
    return best;
}
}
```

## Complexity

Time: **O(n)** · Space: **O(1)**

## Edge cases and interview discussion

Descending prices → 0; empty or singleton → 0; equal prices.

Explain the baseline bottleneck, the improved invariant, and whether either solution mutates its input. A baseline can already be optimal in time (for example palindrome); the improvement may instead reduce memory. Exponential baselines are teaching examples for small inputs only.

[← All problems](README.md)
