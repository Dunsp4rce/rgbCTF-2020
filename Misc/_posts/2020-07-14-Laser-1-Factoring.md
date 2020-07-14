---
layout: post
title: "Laser 1-Factoring"
author: "vishalananth"
tags: ['Misc']
---

Do you like lasers? I like lasers! Here's a warmup: create a program that factors the one number given as input. Output factors on one line in ascending order (or just leave them on the stack, as Laser has implicit output)

Example:

Input: 42

Output: 1 2 3 6 7 14 21 42

## Solution

We take a look at the LaserLang at [https://github.com/Quintec/LaserLang](https://github.com/Quintec/LaserLang) and understand it works with a set of stacks and an instruction pointer which can move in 2D. So after playing with it for sometime and trying out the different functionalities, we implement the following:

The program initially has 2 stacks
- Stack S0 for input and checking.
- Stack S1 for storing final result

The algorithm is as follows
1. Get the input number(N) from the user
2. Start from the number itself(i) and check if it is divisible by N (N%i==0)
3. If it is divisible push it in Stack 1
4. Decrement i and repeat Steps 2 and 3 till i becomes 0
5. Once i becomes 0, switch the current stack to Stack 1 and print the output, since we started factorizing in reverse, the stack will have the factors in ascending order

**Solution**:
- [test.lsr]({site.baseurl}/assets/Laser-1-Factoring/test.lsr)

**Note:** Read more about how the language works, clone the repo and try a few simple programs before trying to understand this code. Also, try running this code locally with verbose to get a better idea of how it works:
```
java Laser test.lsr  -v 36
```

