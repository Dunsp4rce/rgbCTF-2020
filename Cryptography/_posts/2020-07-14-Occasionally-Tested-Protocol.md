---
layout: post
title: "Occasionally Tested Protocol"
author: "anishbadhri"
tags: ['Cryptography']
---

But clearly not tested enough... can you get the flag?

`nc challenge.rgbsec.xyz 12345`

**Files**:
- [otp.py]({{site.baseurl}}/assets/Occasionally-Tested-Protocol/otp.py) 

## Solution

From the given code, it is seen that the RNG is seeded with the current time.
The seed can range from the start time of the program to the end time of the program.
The exact value of the seed can be determined by generating 10 random numbers with the current seed and comparing it against the original 10 values given. If there's a match, the current seed is the seed value used in the program.

Thus, this seed can be used to generate more numbers and xor is performed with the bytes of integer n. The flag is then obtained.

**Program**
- [solution.py]({{site.baseurl}}/assets/Occasionally-Tested-Protocol/solution.py)

## Flag
```
rgbCTF{random_is_not_secure}
```

