# LC015 — Climbing Stairs

**Difficulty:** Easy · **Pattern:** Dynamic Programming

## Problem

Count ways to climb n stairs taking 1 or 2 steps at a time.

## Worked example

`n=4 → 5`

## Approach

Each count equals the sum of the preceding two counts.

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

- Time: **O(n)**
- Space: **O(1)**

[← All problems](README.md)
