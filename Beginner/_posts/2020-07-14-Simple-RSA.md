---
layout: post
title: "Simple RSA"
author: "raghul-rajasekar"
---
Can you find a way to attack this RSA implementation?

**Files:**
- [simple_rsa.txt]({{site.baseurl}}/assets/Simple-RSA/simple_rsa.txt)
- [simple_rsa.py]({{site.baseurl}}/assets/Simple-RSA/simple_rsa.py)

**Hint:**
What's the simplest attack against RSA?

## Solution

In `simple_rsa.py`, we note that `q` is rather small (less than 10<sup>9</sup>), so we could just enumerate all possible values of `q` in order to factorize `n`. The easiest way, of course, is to just pop `n` into [http://factordb.com/](http://factordb.com/), giving us `p = 22034393943473183756163118460342519430053` and `q = 255097177`, which can be used to decrypt the RSA ciphertext.

## Flag

`rgbCTF{brut3_f0rc3}`

