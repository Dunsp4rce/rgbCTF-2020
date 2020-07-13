---
layout: post
title: "A Basic Challenge"
author: "anishbadhri"
tags: ['Beginner']
---

This is a nice and basic challenge

**Files**:
- [basic_chall.txt]({{site.baseurl}}/assets/A-Basic-Challenge/basic_chall.txt)

## Solution

The text file contains space separated binary numbers. When converted to ascii, this yields a string of space separated hex values. On converting these hex values to ascii, a base64 encoded string is obtained. On decoding the base64 string, a set of numbers are obtained. On close observation, it is seen that each digit is less than 8 and hence the numbers are octal. When converted to decimal and then ascii, the flag is obtained. 

**Program**
- [solution.py]({{site.baseurl}}/assets/A-Basic-Challenge/solution.py)

## Flag
```
rgbCTF{c0ngr4ts_0n_b3ing_B4SIC}
```

