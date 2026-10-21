# LC007 — Valid Palindrome

**Difficulty:** Easy · **Pattern:** Two Pointers

## Problem

Ignore punctuation and case while testing whether a string reads the same backward.

## Input, output and constraints

Input is an ASCII string. Ignore non-alphanumeric characters and case. An empty normalized string is a palindrome.

## Worked example

"A man, a plan, a canal: Panama" → true

## Brute-force baseline

Build a normalized string, reverse a copy, and compare.

Time: **O(n)** · Space: **O(n)**

```java
import java.util.*;
class Solution {
public boolean isPalindrome(String s) {
 StringBuilder clean=new StringBuilder();
 for(char c:s.toCharArray()) if(Character.isLetterOrDigit(c)) clean.append(Character.toLowerCase(c));
 return clean.toString().equals(new StringBuilder(clean).reverse().toString());
}
}
```

## Improved approach

Move two pointers inward, skipping non-alphanumeric characters.

## Step-by-step explanation

Two pointers skip punctuation without allocating the normalized string. Each character is visited at most a constant number of times.

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

Time: **O(n)** · Space: **O(1)**

## Edge cases and interview discussion

".," → true; "race a car" → false; a single letter → true.

Explain the baseline bottleneck, the improved invariant, and whether either solution mutates its input. A baseline can already be optimal in time (for example palindrome); the improvement may instead reduce memory. Exponential baselines are teaching examples for small inputs only.

[← All problems](README.md)
