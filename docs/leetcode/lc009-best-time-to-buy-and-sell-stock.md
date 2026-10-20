# LC009 — Best Time to Buy and Sell Stock

**Difficulty:** Easy · **Pattern:** Sliding Window / Array

## Problem

Maximize profit from one buy followed by one sell.

## Worked example

`[7,1,5,3,6,4] → 5`

## Approach

Track the lowest price seen and best profit so far.

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

- Time: **O(n)**
- Space: **O(1)**

[← All problems](README.md)
