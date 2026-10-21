# LC015 — Climbing Stairs

**Difficulty:** Easy · **Pattern:** Dynamic Programming

## Problem

Count ways to climb n stairs taking 1 or 2 steps at a time.

## Input, output and constraints

1 <= n <= 45. Steps have size one or two; different orderings count separately. The answer fits int.

## Worked example

n=4 → 5

## Brute-force baseline

Recursively enumerate every possible next step without memoization.

Time: **O(2^n) upper bound** · Space: **O(n) recursion stack**

```java
import java.util.*;
class Solution {
public int climbStairs(int n) {
 if(n<=1) return 1;return climbStairs(n-1)+climbStairs(n-2);
}
}
```

## Improved approach

Each count equals the sum of the preceding two counts.

## Step-by-step explanation

Every path to step n ends with either a one-step move from n-1 or a two-step move from n-2. For n=4 the counts 2+3 give 5. Two variables replace repeated recursion.

## Java solution

```java
import java.util.*;
class Solution {
public int climbStairs(int n) {
    int a=1, b=1;
    for (int i=2; i<=n; i++) { int next=a+b; a=b; b=next; }
    return b;
}
}
```

## Complexity

Time: **O(n)** · Space: **O(1)**

## Edge cases and interview discussion

n=1 → 1; n=2 → 2; n=45 fits int; brute force only for small n.

Explain the baseline bottleneck, the improved invariant, and whether either solution mutates its input. A baseline can already be optimal in time (for example palindrome); the improvement may instead reduce memory. Exponential baselines are teaching examples for small inputs only.

[← All problems](README.md)
