# LC004 — Group Anagrams

**Difficulty:** Medium · **Pattern:** String / HashMap

## Problem

Group strings that contain the same letters with the same frequencies.

## Worked example

`["eat","tea","tan","ate","nat","bat"] → groups [eat,tea,ate], [tan,nat], [bat]`

## Approach

Use a sorted character sequence as a canonical key.

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

- Time: **O(n·k log k)**
- Space: **O(n·k)**

[← All problems](README.md)
