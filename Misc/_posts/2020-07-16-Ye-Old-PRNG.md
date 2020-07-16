---
layout: post
title: "Ye Old PRNG"
author: "AnandSaminathan"
---

I found a really old prng... can you exploit it? 
<code>nc challenge.rgbsec.xyz 23456</code>


## Solution
The code in the server, printed a menu with options to quit, generate random numbers and guess the next number 10 times for the flag.
On generating random numbers, we got:
![alt text]({site.baseurl}/assets/Ye-Old-PRNG/sshot-1.png)
As we had to guess the <code>next</code> number 10 times, we assumed that every number is generated using the previous number. In the above screenshot, we noticed that <code>22</code> was followed by the number <code>484</code> which is <code>22<sup>2</sup><code>. Then we started checking for the squares of the other numbers and it's relation to the next number, it looked like the next number is always a middle-substring of the square of the previous number whose length is "<=" the given input (3 in the picture). This is bascially middle-square PRNG. 
During guessing, we had to predict the next value for inputs of length 100, 10 times. So all we had to do was find the square of the given number and print the middle substring of length <= 100.
 
```python
from pwn import *

size = 100
prng = remote('challenge.rgbsec.xyz', 23456)

def predict_next(num):
    num = num**2
    num = str(num)
    rem = len(num) - size # size to be removed
    l = (rem // 2) # remove half from starting
    r = len(num) - ((rem // 2) + (rem % 2)) # remove half from ending (+ 1 if odd)
    return str(int(num[l:r]))

for i in range(0, 5): prng.recvline()
prng.sendline("2")

for i in range(0, 10):
    line = prng.recvline().decode()
    inp = line.split(' ')[4] # input number
    num = int(inp[:-1])
    prng.sendline(predict_next(num))
    prng.recvline()

flag = prng.recvline()
log.info(b"flag: " + flag)

```


## Flag
```
rgbCTF{d0nt_us3_midd13_squ4r3}
```


