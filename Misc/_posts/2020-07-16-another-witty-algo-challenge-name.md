---
layout: post
title: "[another witty algo challenge name]"
author: "AnandSaminathan"
---

This is pretty simple. You get a list of 5000 by 5000 grid of ones and zeros, and you have to print the number of islands in the grid.

An island is a collections of ones where each one is adjacent to another one in the island. For a cell to be adjacent to another cell, they must share an edge.

Submit the number wrapped in the flag format, like rgbCTF{123}

**Files**
- [grid.txt]({{site.baseurl}}/assets/another-witty-algo-challenge-name/grid.txt)


## Solution

This is a [standard problem](https://leetcode.com/problems/number-of-islands/) of finding the number of connected components in a grid graph. We just used the same solution (breadth first search on the grid graph) for the linked leetcode problem.

```cpp
#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    
    vector<int> dx, dy;
    int n, m;
    
    vector<vector<bool>> visit;
    
    bool check(int x, int y) {
        return (x >= 0) && (x < n) && 
            (y >= 0) && (y < m);
    }
    
    void bfs(int u, int v, vector<vector<char>>& grid) {
        queue<pair<int, int>> que;
        visit[u][v] = 1;
        que.push({u, v});
        while(que.size()) {
            pair<int, int> f = que.front();
            que.pop();
            int x = f.first, y = f.second;
            for(int i = 0; i < 4; ++i) {
                int p = x + dx[i];
                int q = y + dy[i];
                if(check(p, q) && grid[p][q] == '1' && !visit[p][q]) {
                    visit[p][q] = 1;
                    que.push({p, q});
                }
            }
        }
    }
    
    int numIslands(vector<vector<char>>& grid) {
        this->n = grid.size();
        if(n == 0) return 0;
        
        this->m = grid[0].size();
        
        if(n == 0 || m == 0) return 0;
        
        dx.emplace_back(-1); dy.emplace_back(0);
        dx.emplace_back(1); dy.emplace_back(0);
        dx.emplace_back(0); dy.emplace_back(-1);
        dx.emplace_back(0); dy.emplace_back(1);
        
        
        visit.resize(grid.size());
        for(int i = 0; i < grid.size(); ++i) {
            visit[i].resize(grid[i].size());
        }
        
        int ans = 0;
        
        for(int i = 0; i < grid.size(); ++i) {
            for(int j = 0; j < grid[i].size(); ++j) {
                if(!visit[i][j] && grid[i][j] == '1') {
                    ++ans;
                    bfs(i, j, grid);
                }
            }
        }
        
        return ans;
    }
};

int main() {
  vector<vector<char>> grid(5000, vector<char>(5000));
  for(int i = 0; i < 5000; ++i) {
    for(int j = 0; j < 5000; ++j) {
      cin >> grid[i][j];
    }
  }
  Solution sol;
  cout << sol.numIslands(grid) << '\n';

}
```

The number of islands in the given input was <code>119609</code>.

## Flag
```
rgbCTF{119609}
```





