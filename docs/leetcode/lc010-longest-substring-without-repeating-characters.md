# LC010 — Longest Substring Without Repeating Characters

**Difficulty:** Medium · **Pattern:** Sliding Window

## Problem

Find the maximum length of a substring with no repeated characters.

## Input, output and constraints

Input is a non-null ASCII string. Return the length of a contiguous substring, not a subsequence, containing no duplicate characters.

## Worked example

"abcabcbb" → 3

## Brute-force baseline

Start at every index and grow a set until a character repeats.

Time: **O(n²)** · Space: **O(min(n, alphabet size))**

```java
import java.util.*;
class Solution {
public int lengthOfLongestSubstring(String s) {
 int best=0;
 for(int i=0;i<s.length();i++) {
  Set<Character> seen=new HashSet<>();
  for(int j=i;j<s.length() && seen.add(s.charAt(j));j++) best=Math.max(best,j-i+1);
 }return best;
}
}
```

## Improved approach

Track last seen index and advance the left boundary.

## Step-by-step explanation

In abcabcbb, the first window reaches abc. Seeing a again moves left past the previous a. Use max(left,last+1) so left never moves backward.

## Java solution

```java
import java.util.*;
class Solution {
public int lengthOfLongestSubstring(String s) {
    Map<Character, Integer> last = new HashMap<>();
    int left = 0, best = 0;
    for (int right = 0; right < s.length(); right++) {
        char c = s.charAt(right);
        if (last.containsKey(c)) left = Math.max(left, last.get(c) + 1);
        last.put(c, right);
        best = Math.max(best, right - left + 1);
    }
    return best;
}
}
```

## Complexity

Time: **O(n)** · Space: **O(k) for distinct chars**

## Edge cases and interview discussion

"abba" → 2; "" → 0; repeated spaces count as characters.

Explain the baseline bottleneck, the improved invariant, and whether either solution mutates its input. A baseline can already be optimal in time (for example palindrome); the improvement may instead reduce memory. Exponential baselines are teaching examples for small inputs only.

[← All problems](README.md)
