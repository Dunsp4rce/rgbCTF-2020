---
layout: post
title: "Laser-2-Sorting"
author: "anishbadhri"
tags: ['Misc']
---

[https://github.com/Quintec/LaserLang](https://github.com/Quintec/LaserLang)

Here's a harder Laser challenge. Given an input stack of numbers, sort them in descending order. 

`nc challenge.rgbsec.xyz 7678`

Input: 1 2 7 3 ~~down the rockefeller street~~

Output: 7 3 2 1

## Solution

The algorithm implemented in laser lang is the following:

The program initially has 4 stacks
- Stack S0 for input. Initialized with input.
- Stack S1 for final result. Initialized with one element: 0
- Stack S2 for element to push
- Stack S3 for comparisons

The algorithm is as follows
1. If S0 is empty, go to step 12, otherwise go to step 2
2. Move top of S0 to S2
3. Copy top of S1 to S3
4. Copy top of S2 to S3
5. Check greater than on S3
6. If 0 flag on top of S3, go to step 7, otherwise go to step 9
7. Move top of stack S2 to S1
8. Go to step 1
9. Move top of S1 to S0
10. Move top of S2 to S0
11. Go to step 1
12. Perform cyclic shift and pop initial 0 on stack S1
13. Print S1

**Solution**:
- [solution.lsr]({site.baseurl}/assets/Laser-2-Sorting/solution.lsr)

## Flag
```
rgbCTF{1_f33l_y0ur_p41n_trust_m3}
```
