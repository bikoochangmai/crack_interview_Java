# LC011 — Valid Parentheses

**Difficulty:** Easy · **Pattern:** Stack

## Problem

Determine whether bracket characters are correctly nested and closed.

## Worked example

`"([]){}" → true`

## Approach

Push expected closing brackets and match them on encounter.

## Java solution

```java
import java.util.*;

class Solution {
    public boolean isValid(String s) {
        Deque<Character> stack = new ArrayDeque<>();
        for (char c : s.toCharArray()) {
            if (c == '(') stack.push(')');
            else if (c == '[') stack.push(']');
            else if (c == '{') stack.push('}');
            else if (stack.isEmpty() || stack.pop() != c) return false;
        }
        return stack.isEmpty();
    }
}
```

## Complexity

- Time: **O(n)**
- Space: **O(n)**

[← All problems](README.md)
