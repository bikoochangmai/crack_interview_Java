# LC011 — Valid Parentheses

**Difficulty:** Easy · **Pattern:** Stack

## Problem

Determine whether bracket characters are correctly nested and closed.

## Input, output and constraints

Input contains only (), [] and {}. Every closer must match the most recent unmatched opener; empty input is valid.

## Worked example

"([]){}" → true

## Brute-force baseline

Repeatedly remove adjacent matching bracket pairs until no change occurs.

Time: **O(n²)** · Space: **O(n)**

```java
import java.util.*;
class Solution {
public boolean isValid(String s) {
 while(true){String next=s.replace("()", "").replace("[]", "").replace("{}", "");if(next.equals(s)) return s.isEmpty();s=next;}
}
}
```

## Improved approach

Push expected closing brackets and match them on encounter.

## Step-by-step explanation

A stack stores expected closing characters. In ([]){}, ] must close [ before ) can close (. A nonempty stack at the end means missing closers.

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

Time: **O(n)** · Space: **O(n)**

## Edge cases and interview discussion

"([)]" → false; "(" → false; "" → true.

Explain the baseline bottleneck, the improved invariant, and whether either solution mutates its input. A baseline can already be optimal in time (for example palindrome); the improvement may instead reduce memory. Exponential baselines are teaching examples for small inputs only.

[← All problems](README.md)
