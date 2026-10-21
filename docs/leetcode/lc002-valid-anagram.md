# LC002 — Valid Anagram

**Difficulty:** Easy · **Pattern:** String / HashMap

## Problem

Check whether two lowercase English-letter strings have the same character counts.

## Input, output and constraints

Inputs are non-null lowercase a-z strings. Return a boolean; unequal lengths cannot be anagrams.

## Worked example

s="anagram", t="nagaram" → true

## Brute-force baseline

For each source character, find and consume one matching unused target character.

Time: **O(n²)** · Space: **O(n)**

```java
import java.util.*;
class Solution {
public boolean isAnagram(String s,String t) {
 if(s.length()!=t.length()) return false;
 boolean[] used=new boolean[t.length()];
 for(char c:s.toCharArray()) {
  int j=0; while(j<t.length() && (used[j] || t.charAt(j)!=c)) j++;
  if(j==t.length()) return false; used[j]=true;
 }
 return true;
}
}
```

## Improved approach

Count characters in a fixed-size array.

## Step-by-step explanation

Counting increments for s and decrements for t cancel exactly when all multiplicities match. Equal sets of characters alone are insufficient.

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

Time: **O(n)** · Space: **O(1)**

## Edge cases and interview discussion

aab / abb → false; empty strings → true; different lengths.

Explain the baseline bottleneck, the improved invariant, and whether either solution mutates its input. A baseline can already be optimal in time (for example palindrome); the improvement may instead reduce memory. Exponential baselines are teaching examples for small inputs only.

[← All problems](README.md)
