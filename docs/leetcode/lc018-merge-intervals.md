# LC018 — Merge Intervals

**Difficulty:** Medium · **Pattern:** Sorting / Intervals

## Problem

Merge all overlapping closed intervals.

## Worked example

`[[1,3],[2,6],[8,10]] → [[1,6],[8,10]]`

## Approach

Sort by start and merge when the next interval overlaps.

## Java solution

```java
import java.util.*;

class Solution {
    public int[][] merge(int[][] intervals) {
        if (intervals.length==0) return new int[0][];
        Arrays.sort(intervals, Comparator.comparingInt(a -> a[0]));
        List<int[]> out=new ArrayList<>();
        int[] cur=intervals[0].clone();
        for (int i=1;i<intervals.length;i++) {
            if (intervals[i][0]<=cur[1]) cur[1]=Math.max(cur[1],intervals[i][1]);
            else { out.add(cur); cur=intervals[i].clone(); }
        }
        out.add(cur);
        return out.toArray(new int[0][]);
    }
}
```

## Complexity

- Time: **O(n log n)**
- Space: **O(n) output**

[← All problems](README.md)
