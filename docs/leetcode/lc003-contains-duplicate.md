# LC003 — Contains Duplicate

**Difficulty:** Easy · **Pattern:** Array / HashSet

## Problem

Determine whether any value occurs more than once.

## Worked example

`[1,2,3,1] → true`

## Approach

Insert into a set; a failed insertion reveals a duplicate.

## Java solution

```java
import java.util.*;

class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> seen = new HashSet<>();
        for (int n : nums) if (!seen.add(n)) return true;
        return false;
    }
}
```

## Complexity

- Time: **O(n)**
- Space: **O(n)**

[← All problems](README.md)
