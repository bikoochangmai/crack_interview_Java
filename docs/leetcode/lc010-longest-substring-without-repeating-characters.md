# LC010 — Longest Substring Without Repeating Characters

**Difficulty:** Medium · **Pattern:** Sliding Window

## Problem

Find the maximum length of a substring with no repeated characters.

## Worked example

`"abcabcbb" → 3`

## Approach

Track last seen index and advance the left boundary.

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

- Time: **O(n)**
- Space: **O(k) for distinct chars**

[← All problems](README.md)
