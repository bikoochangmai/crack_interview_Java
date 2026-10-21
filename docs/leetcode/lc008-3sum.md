# LC008 — 3Sum

**Difficulty:** Medium · **Pattern:** Two Pointers / Sorting

## Problem

Find unique triples of numbers summing to zero.

## Input, output and constraints

Return distinct value triplets with sum zero, using three different indices. Output order does not matter. Assume abs(value) <= 100000.

## Worked example

[-1,0,1,2,-1,-4] → [[-1,-1,2],[-1,0,1]]

## Brute-force baseline

Enumerate every index triple; sort each matching triple and deduplicate with a set.

Time: **O(n³)** · Space: **O(t) result storage for t unique triples**

```java
import java.util.*;
class Solution {
public List<List<Integer>> threeSum(int[] nums) {
 Set<List<Integer>> out=new HashSet<>();
 for(int i=0;i<nums.length;i++) for(int j=i+1;j<nums.length;j++) for(int k=j+1;k<nums.length;k++)
  if(nums[i]+nums[j]+nums[k]==0){int[] a={nums[i],nums[j],nums[k]};Arrays.sort(a);out.add(Arrays.asList(a[0],a[1],a[2]));}
 return new ArrayList<>(out);
}
}
```

## Improved approach

Sort; fix one element and sweep the remaining pair.

## Step-by-step explanation

After sorting [-4,-1,-1,0,1,2], fixing -1 allows a two-pointer sweep to find (-1,-1,2) and (-1,0,1). Skip duplicate fixed values and matched endpoints.

## Java solution

```java
import java.util.*;
class Solution {
public List<List<Integer>> threeSum(int[] nums) {
    Arrays.sort(nums);
    List<List<Integer>> out = new ArrayList<>();
    for (int i = 0; i < nums.length - 2; i++) {
        if (i > 0 && nums[i] == nums[i-1]) continue;
        int l = i+1, r = nums.length-1;
        while (l < r) {
            int sum = nums[i] + nums[l] + nums[r];
            if (sum < 0) l++;
            else if (sum > 0) r--;
            else {
                out.add(Arrays.asList(nums[i], nums[l], nums[r]));
                l++; r--;
                while (l < r && nums[l] == nums[l-1]) l++;
                while (l < r && nums[r] == nums[r+1]) r--;
            }
        }
    }
    return out;
}
}
```

## Complexity

Time: **O(n²)** · Space: **O(1) extra excluding output/sort**

## Edge cases and interview discussion

[0,0,0,0] → [[0,0,0]]; fewer than three values; optimized code sorts input.

Explain the baseline bottleneck, the improved invariant, and whether either solution mutates its input. A baseline can already be optimal in time (for example palindrome); the improvement may instead reduce memory. Exponential baselines are teaching examples for small inputs only.

[← All problems](README.md)
