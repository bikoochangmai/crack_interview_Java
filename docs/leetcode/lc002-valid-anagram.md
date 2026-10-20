# LC002 — Valid Anagram

**Difficulty:** Easy · **Pattern:** String / HashMap

## Problem

Check whether two lowercase English-letter strings have the same character counts.

## Worked example

`s="anagram", t="nagaram" → true`

## Approach

Count characters in a fixed-size array.

## Java solution

```java
import java.util.*;

class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;
        int[] count = new int[26];
        for (int i = 0; i < s.length(); i++) {
            count[s.charAt(i) - 'a']++;
            count[t.charAt(i) - 'a']--;
        }
        for (int n : count) if (n != 0) return false;
        return true;
    }
}
```

## Complexity

- Time: **O(n)**
- Space: **O(1)**

[← All problems](README.md)
