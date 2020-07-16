---
layout: post
title: "[insert creative algo chall name]"
author: "AnandSaminathan"
---

**File**
- [question.txt]({{site.baseurl}}/assets/insert-creative-algo-chall-name/question.txt)


## Solution

The given file has an algo question. We had to find the number of unique combinations for the input x = 4 and n = 12.
This was solved using brute-force. We generated all possible combinations using recursion, very element in the set of values <code>r</code> can fall into one of the <code>x</code> subsets for a particular combination. So we maintained an array <code>sums</code> of size <code>x</code> where <code>sums[i]</code> is the sum of all elements in subset <code>i</code>. For each element, we did the following:
```cpp
  for(int i = 0; i < x ; ++i) {
    sum[i] += (1 << cur);
    rec(cur + 1, sum);
    sum[i] -= (1 << cur);
  }
```
Where <code>rec</code> is the recursive function. In each iteration of the for loop, we assumed that the current element(<code>cur</code>) belonged to subset <code>i</code> and moved on to the next one. The base case of the recurrence is:
```cpp
  if(cur == n) {
    for(int i = 0; i < sum.size(); ++i) {
      if(sum[i] == 0) {
        // ith subset is empty
        return ;  
      }   
    }
    auto x = sum;
    // sort because [16, 2, 3, 4] and [4, 3, 2, 16] should be counted only once 
    sort(x.begin(), x.end());
    st.insert(x);
    return ;
  }
```
After making a choice for all the elements, we checked if some subset is empty, if not we sorted the sum array and inserted it into a set (<code>st</code>) for unique combinations. Finally the answer is just the size of the set. Complete code:
```cpp
#include <bits/stdc++.h>

using  namespace std;

set<vector<int>> st;
int n;
int x;

void rec(int cur, vector<int> sum) {
  if(cur == n) {
    for(int i = 0; i < sum.size(); ++i) {
      if(sum[i] == 0) {
        // ith subset is empty
        return ;  
      }   
    }
    auto x = sum;
    // sort because [16, 2, 3, 4] and [4, 3, 2, 16] should be counted only once 
    sort(x.begin(), x.end());
    st.insert(x);
    return ;
  }
  for(int i = 0; i < x ; ++i) {
    sum[i] += (1 << cur);
    rec(cur + 1, sum);
    sum[i] -= (1 << cur);
  }
}

int main() {
  cin >> x >> n;
  vector<int> sum(x, 0);
  rec(0, sum);
  cout << st.size() << "\n";
}
```
The number of unique combinations for x = 4 and n = 12 was 611501.

## Flag
```
rgbCTF{611501}
```


