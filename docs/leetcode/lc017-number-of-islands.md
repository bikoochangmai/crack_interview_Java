# LC017 — Number of Islands

**Difficulty:** Medium · **Pattern:** Graph / DFS

## Problem

Count connected groups of land cells in a 2D grid (4-directional adjacency).

## Worked example

`[["1","1","0"],["0","1","0"],["0","0","1"]] → 2`

## Approach

Flood-fill each unvisited land cell using an explicit stack.

## Java solution

```java
import java.util.*;

class Solution {
    public int numIslands(char[][] grid) {
        if (grid.length == 0) return 0;
        int rows=grid.length, cols=grid[0].length, count=0;
        int[][] dirs={{1,0},{-1,0},{0,1},{0,-1}};
        for (int r=0;r<rows;r++) for (int c=0;c<cols;c++) {
            if (grid[r][c]!='1') continue;
            count++;
            Deque<int[]> stack=new ArrayDeque<>();
            stack.push(new int[]{r,c}); grid[r][c]='0';
            while (!stack.isEmpty()) {
                int[] p=stack.pop();
                for (int[] d:dirs) {
                    int nr=p[0]+d[0], nc=p[1]+d[1];
                    if (nr>=0 && nr<rows && nc>=0 && nc<cols && grid[nr][nc]=='1') {
                        grid[nr][nc]='0'; stack.push(new int[]{nr,nc});
                    }
                }
            }
        }
        return count;
    }
}
```

## Complexity

- Time: **O(rows × cols)**
- Space: **O(rows × cols)**

[← All problems](README.md)
