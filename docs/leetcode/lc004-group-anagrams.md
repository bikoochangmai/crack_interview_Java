# LC004 — Group Anagrams

**Difficulty:** Medium · **Pattern:** String / HashMap

## Problem

Group strings that contain the same letters with the same frequencies.

## Input, output and constraints

Input is an array of lowercase a-z strings, including possible empty strings and duplicates. Return groups in any order; keep every occurrence.

## Worked example

["eat","tea","tan","ate","nat","bat"] → groups [eat,tea,ate], [tan,nat], [bat]

## Brute-force baseline

Compare each word against the representative of every existing group using letter counts.

Time: **O(n²·k), k = maximum word length** · Space: **O(n·k) including output**

```java
import java.util.*;
class Solution {
public List<List<String>> groupAnagrams(String[] strs) {
 List<List<String>> out=new ArrayList<>();
 for(String s:strs) {
  List<String> found=null;
  for(List<String> g:out) if(same(s,g.get(0))) {found=g;break;}
  if(found==null) {found=new ArrayList<>();out.add(found);} found.add(s);
 }
 return out;
}
private boolean same(String a,String b) {
 if(a.length()!=b.length()) return false;
 int[] count=new int[26];
 for(int i=0;i<a.length();i++){count[a.charAt(i)-'a']++;count[b.charAt(i)-'a']--;}
 for(int x:count) if(x!=0) return false; return true;
}
}
```

## Improved approach

Use a sorted character sequence as a canonical key.

## Step-by-step explanation

Sorting eat, tea and ate yields the same key aet. A canonical key avoids checking every existing group.

## Java solution

```java
import java.util.*;
class Solution {
public List<List<String>> groupAnagrams(String[] strs) {
    Map<String, List<String>> groups = new HashMap<>();
    for (String s : strs) {
        char[] chars = s.toCharArray();
        Arrays.sort(chars);
        groups.computeIfAbsent(new String(chars), k -> new ArrayList<>()).add(s);
    }
    return new ArrayList<>(groups.values());
}
}
```

## Complexity

Time: **O(n·k log k)** · Space: **O(n·k)**

## Edge cases and interview discussion

["",""] → one group of two; duplicate words; singleton groups.

Explain the baseline bottleneck, the improved invariant, and whether either solution mutates its input. A baseline can already be optimal in time (for example palindrome); the improvement may instead reduce memory. Exponential baselines are teaching examples for small inputs only.

[← All problems](README.md)
