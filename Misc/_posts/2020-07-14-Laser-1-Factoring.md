---
layout: post
title: "Laser-1-Factoring"
author: "vishalananth"
tags: ['Misc']
---

Do you like lasers? I like lasers! Here's a warmup: create a program that factors the one number given as input. Output factors on one line in ascending order (or just leave them on the stack, as Laser has implicit output)

Example:

Input: 42

Output: 1 2 3 6 7 14 21 42

## Solution

We take a look at the LaserLang at https://github.com/Quintec/LaserLang and understand it works with a set of stacks and an instruction pointer which can move in 2D. So after playing with it for sometime and trying out the different functionalities, we arrive at the code for factorizing a number:

```
ir>ruru%  ⌜pu⌜ \
  \⌝(<srup/
 #U<         
     \         /
```
Submitting this code gets us the flag

**Note:** Read more about how the language works and try a few simple programs before trying to understand this code. Try running this code locally with verbose to get a better idea of how the code works:
```
java Laser test.lsr  -v 36
```

