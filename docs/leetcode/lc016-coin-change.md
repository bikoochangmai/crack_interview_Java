# LC016 — Coin Change

**Difficulty:** Medium · **Pattern:** Dynamic Programming

## Problem

Find the fewest coins needed for an amount, with unlimited coins of each denomination.

## Input, output and constraints

Coins are positive integers with unlimited supply; amount >= 0. Return the minimum count or -1 if impossible. A zero amount needs zero coins.

## Worked example

coins=[1,2,5], amount=11 → 3

## Brute-force baseline

Try every denomination recursively and choose the smallest successful result.

Time: **O(c^(A/m+1)) upper bound, c=coin count, A=amount, m=min coin** · Space: **O(A/m+1) recursion stack**

```java
import java.util.*;
class Solution {
public int coinChange(int[] coins,int amount) {
 if(amount==0) return 0;int best=Integer.MAX_VALUE;
 for(int c:coins) if(c<=amount){int sub=coinChange(coins,amount-c);if(sub>=0) best=Math.min(best,sub+1);}
 return best==Integer.MAX_VALUE ? -1 : best;
}
}
```

## Improved approach

Bottom-up DP stores minimum coins for every reachable amount.

## Step-by-step explanation

dp[a] stores the best count for amount a. For coins [1,2,5], dp[11] can use dp[6]+1=3. Initialize unreachable values above the maximum possible valid count.

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

Time: **O(amount × coins)** · Space: **O(amount)**

## Edge cases and interview discussion

[2], amount=3 → -1; amount=0 → 0; no zero/negative denominations; brute force only for small amounts.

Explain the baseline bottleneck, the improved invariant, and whether either solution mutates its input. A baseline can already be optimal in time (for example palindrome); the improvement may instead reduce memory. Exponential baselines are teaching examples for small inputs only.

[← All problems](README.md)
