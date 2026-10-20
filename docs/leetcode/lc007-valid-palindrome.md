# LC007 — Valid Palindrome

**Difficulty:** Easy · **Pattern:** Two Pointers

## Problem

Ignore punctuation and case while testing whether a string reads the same backward.

## Worked example

`"A man, a plan, a canal: Panama" → true`

## Approach

Move two pointers inward, skipping non-alphanumeric characters.

## Java solution

```java
import java.util.*;

class Solution {
    public boolean isPalindrome(String s) {
        int l = 0, r = s.length() - 1;
        while (l < r) {
            while (l < r && !Character.isLetterOrDigit(s.charAt(l))) l++;
            while (l < r && !Character.isLetterOrDigit(s.charAt(r))) r--;
            if (Character.toLowerCase(s.charAt(l++)) != Character.toLowerCase(s.charAt(r--))) return false;
        }
        return true;
    }
}
```

## Complexity

- Time: **O(n)**
- Space: **O(1)**

[← All problems](README.md)
