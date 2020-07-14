
---
layout: post
title: "I Love Rainbows"
author: "INXS_JOY"
tags: ['Cryptography']
---

Can you figure out why?

## Solution
The prompt kinda hints that it has something to do with the rainbow hash attack. Surprising enough we find hashes in the rainbows.txt file.
There are two types of hashes in the file
```
1.MD5 Hash i.e the short ones
2.SHA256 Hash i.e the long ones
```
So now we need to reverse these hashes to see what as the original text. For this I used https://md5.gromweb.com/ , for MD5 reversing and https://md5decrypt.net/en/Sha256/ , for SHA256 reversing. 
Some hashed cannot be reversed on these sites then use this https://crackstation.net/ which is basically a brute force try on the hashes. Each hash would give one or two letter of the flag. Stringing them all together we get the flag.
  
## Flag
>rgbCTF{alw4ys_us3_s4lt_wh3n_h4shing}
