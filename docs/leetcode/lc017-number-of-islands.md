# LC017 — Number of Islands

**Difficulty:** Medium · **Pattern:** Graph / DFS

## Problem

Count connected groups of land cells in a 2D grid (4-directional adjacency).

## Input, output and constraints

Rectangular grid contains only 0 water and 1 land. Count components joined horizontally or vertically; diagonal contact does not join islands.

## Worked example

[["1","1","0"],["0","1","0"],["0","0","1"]] → 2

## Brute-force baseline

For every unassigned land cell repeatedly rescan the grid to expand its component until no adjacent land can be added.

Time: **O((rows·cols)²) upper bound** · Space: **O(rows·cols)**

```java
import java.util.*;
class Solution {
public int numIslands(char[][] grid) {
 if(grid.length==0) return 0;
 int rows=grid.length,cols=grid[0].length,count=0;
 int[][] label=new int[rows][cols];int[][] dirs={{1,0},{-1,0},{0,1},{0,-1}};
 for(int r=0;r<rows;r++) for(int c=0;c<cols;c++) {
  if(grid[r][c]!='1' || label[r][c]!=0) continue;
  label[r][c]=++count;boolean changed;
  do {changed=false;
   for(int i=0;i<rows;i++) for(int j=0;j<cols;j++) {
    if(grid[i][j]!='1' || label[i][j]!=0) continue;
    for(int[] d:dirs){int a=i+d[0],b=j+d[1];
     if(a>=0 && a<rows && b>=0 && b<cols && label[a][b]==count){label[i][j]=count;changed=true;break;}}
   }
  } while(changed);
 }return count;
}
}
```

## Improved approach

Flood-fill each unvisited land cell using an explicit stack.

## Step-by-step explanation

Flood-fill marks land when pushing it, so each cell enters the stack once. The sample has one three-cell component and one isolated cell. The optimized solution mutates land to water; copy the grid if needed.

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

Time: **O(rows × cols)** · Space: **O(rows × cols)**

## Edge cases and interview discussion

Empty grid → 0; all water → 0; diagonal land → separate islands; a long narrow island.

Explain the baseline bottleneck, the improved invariant, and whether either solution mutates its input. A baseline can already be optimal in time (for example palindrome); the improvement may instead reduce memory. Exponential baselines are teaching examples for small inputs only.

[← All problems](README.md)
