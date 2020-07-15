---
layout: post
title: "Joke Check!"
author: "anishbadhri"
tags: ['Beginner']
---

What do you call a chicken staring at lettuce?

**Files**
- [punchline.txt]({{site.baseurl}}/assets/Joke-Check/punchline.txt)

## Solution

By observing the first few letters and comparing with `rgbCTF` it is observed that each character is caesar shifted by 11. On rotating it back, the flag is obtained.

**Solution**
- [solution.py]({{site.baseurl}}/assets/Joke-Check/solution.py)

## Flag

```
rgbCTF{a_chicken_caesar_salad}
```