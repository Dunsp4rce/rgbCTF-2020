---
layout: post
title: "Five Fives"
author: "raghul-rajasekar"
---

java SecureRandom is supposed to be, well, secure, right? `nc challenge.rgbsec.xyz 7425`

**Files:**
- [Main.java]({{site.baseurl}}/assets/Five-Fives/Main.java)

## Solution

Looking at `Main.java`, we see that the seed for `SecureRandom` is set by sleeping for a random time (up to 10 seconds) which is determined by `ThreadLocalRandom.current().nextInt(10000)`, setting the seed as the UNIX timestamp in milliseconds at that point and finally sleeping for the remaining duration so that the user doesn't know what the seed is.

Since the program also prints the first 5 random numbers from `SecureRandom`, a possible solution was to brute-force over all possible values of the seed (at most 10000) and get tickets corresponding to the limited number of seeds which generated the first 5 random numbers correctly (as a maximum of 20 tickets could be bought, it was almost sure that one ticket would match). Weirdly, when testing `SecureRandom`, even setting the seed wasn't enough to produce the same sequence of random numbers (we're still not sure why).

Thus, the only approach remaining is brute-force. Since there are a total of 5<sup>5</sup> = 3125 possible tickets and we could buy 20 tickets each time, the probability of finding the correct ticket by just choosing random tickets is `20/3125 = 4/625`. By entering the lotto `x` times, the probability of winning at least once is <code>1 - (1 - 4/625)<sup>x</sup></code>. For `x = 150`, this gives a 62% of winning. Also, since entering the lotto each time takes around 10 seconds, for `x = 150`, it will take around 25 minutes roughly. The crude code I used is as follows:
```python
from pwn import remote
from random import randint
ctr = 1 
while ctr > 0:
    print(ctr) 
    p = remote('challenge.rgbsec.xyz', 7425)
    ret = b'' 
    while b'seed' not in ret: 
        ret = p.read() 
    print(ret) 
    print(p.read()) 
    p.write("20\n") 
    for i in range(20): 
        while b'spaces' not in ret: 
            ret = p.read() 
        ret = b'spaces' 
        cand = ' '.join([str(randint(1, 5)) for _ in range(5)]) + '\n'
        print(cand) 
        p.write(cand) 
        while b'win' not in ret: 
            ret = p.read() 
        print(ret) 
        if b'Cong' in ret: 
            print(ret)
            while True:
                print(p.read()) 
            ctr = -1 
            break 
    p.close()
    ctr += 1  
```

Finally, the flag was printed after around 20 minutes.

## Flag

`rgbCTF{s0m3t1m3s_4ll_y0u_n33d_1s_f0rc3}`

