# LC018 — Merge Intervals

**Difficulty:** Medium · **Pattern:** Sorting / Intervals

## Problem

Merge all overlapping closed intervals.

## Input, output and constraints

Each closed interval has start <= end. Touching endpoints overlap. Return disjoint merged intervals; empty input is allowed.

## Worked example

[[1,3],[2,6],[8,10]] → [[1,6],[8,10]]

## Brute-force baseline

Repeatedly scan all interval pairs and merge any overlap until no pair overlaps.

Time: **O(n³) upper bound** · Space: **O(n)**

```java
import java.util.*;
class Solution {
public int[][] merge(int[][] intervals) {
 List<int[]> a=new ArrayList<>();for(int[] x:intervals) a.add(x.clone());
 boolean changed;
 do {changed=false;
  outer:for(int i=0;i<a.size();i++) for(int j=i+1;j<a.size();j++) {
   int[] x=a.get(i),y=a.get(j);
   if(x[0]<=y[1] && y[0]<=x[1]){x[0]=Math.min(x[0],y[0]);x[1]=Math.max(x[1],y[1]);a.remove(j);changed=true;break outer;}
  }
 }while(changed);
 return a.toArray(new int[0][]);
}
}
```

## Improved approach

Sort by start and merge when the next interval overlaps.

## Step-by-step explanation

Sort by start. After [1,3] merges with [2,6], current becomes [1,6]. [8,10] cannot overlap it, so emit current. Sorting guarantees later starts cannot reconnect a finished interval.

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

Time: **O(n log n)** · Space: **O(n) output**

## Edge cases and interview discussion

[[1,4],[4,5]] → [[1,5]]; nested intervals; optimized code sorts the input array.

Explain the baseline bottleneck, the improved invariant, and whether either solution mutates its input. A baseline can already be optimal in time (for example palindrome); the improvement may instead reduce memory. Exponential baselines are teaching examples for small inputs only.

[← All problems](README.md)
