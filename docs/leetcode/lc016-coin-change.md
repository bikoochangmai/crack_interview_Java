# LC016 — Coin Change

**Difficulty:** Medium · **Pattern:** Dynamic Programming

## Problem

Find the fewest coins needed for an amount, with unlimited coins of each denomination.

## Worked example

`coins=[1,2,5], amount=11 → 3`

## Approach

Bottom-up DP stores minimum coins for every reachable amount.

## Java solution

```java
import java.util.*;

class Solution {
    public int coinChange(int[] coins, int amount) {
        int[] dp = new int[amount+1];
        Arrays.fill(dp, amount+1);
        dp[0]=0;
        for (int a=1; a<=amount; a++)
            for (int c : coins)
                if (c<=a) dp[a]=Math.min(dp[a], dp[a-c]+1);
        return dp[amount]>amount ? -1 : dp[amount];
    }
}
```

## Complexity

- Time: **O(amount × coins)**
- Space: **O(amount)**

[← All problems](README.md)
