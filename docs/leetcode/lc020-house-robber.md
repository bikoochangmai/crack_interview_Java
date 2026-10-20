# LC020 — House Robber

**Difficulty:** Medium · **Pattern:** Dynamic Programming

## Problem

Maximize money from nonadjacent houses.

## Worked example

`[2,7,9,3,1] → 12`

## Approach

At each house, choose between skipping it or adding it to the best two houses back.

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

- Time: **O(n)**
- Space: **O(1)**

[← All problems](README.md)
