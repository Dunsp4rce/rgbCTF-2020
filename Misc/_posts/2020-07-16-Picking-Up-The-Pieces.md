---
layout: post
title: "Picking Up The Pieces"
author: "AnandSaminathan"
---

Can you help me? I had a flag that I bought at the store, but on the way home, I dropped parts of it on some roads! Now some roads have strings of text, and I can't tell which are part of my flag. I'm very smart and efficient (but somehow not smart or efficient enough to keep my flag), so I know that I took the fastest way from the store back to my house.

I have a map with a list of all 200000 roads between intersections, and what strings are on them. The format of the map is <intersection 1> <intersection 2> <distance> <string on the road>. My house is at intersection 1 and the store is at intersection 200000.

**Files**
- [map.txt]({{site.baseurl}}/assets/Picking-Up-The-Pieces/map.txt)


## Solution

According to the question, we have to find the shortest path between 1 and 200000. Instead of using Dijkstra, we solved it just my manually searching for some strings (substrings of rbgCTF). Luckily, on searching "CTF", we found a road:
```
135893 137329 287162841 bCTF{
```
Then on tracing the path one step backwards using <code>135893</code>, we got the substring "rg". After tracing the path forwards from <code>137329</code> and appending meaningful strings step by step, we got the flag as: <code>rgbCTF{1m_b4d_4t_sh0pping}</code>

## Flag
```
rgbCTF{1m_b4d_4t_sh0pp1ng}
```


