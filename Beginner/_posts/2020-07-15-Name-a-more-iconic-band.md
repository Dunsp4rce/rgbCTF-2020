---
layout: post
title: "Name a more iconic band"
author: "AnandSaminathan"
---

I'll wait.

The flag for this challenge is all the passwords in alphabetical order, each separated by a single white-space as an MD5 hash in lower case

md5(passwordA passwordB passwordC ...)

Example: if the passwords were "dog" and "cat", the flag would be
rgbCTF{md5("cat dog")}
rgbCTF{b89526a82f7ec08c202c2345fbd6aef3}


**Files**
- [data.7z](https://mega.nz/file/ZYBHgYKS#fC4dxyu5vLCogFoHTk7ql5ozI1nGuxGR2FKf4yFN8AU)


## Solution

On decompressing the given .7z file, we get a 1GB sized file called <code>data</code>. On running <code>file</code> command - I got to know that it's some ELF core file (no clue), then I ran <code>binwalk</code> - one of the descriptions was "Microsoft executable, portable (PE)". With this I started searching and found out that it's a windows memory dump and ended up using <code>volatility</code> for memory forensics. With imageinfo plugin, I found that the memory dump was most likely of a Windows 7 system.
![alt text]({{site.baseurl}}/assets/Name-a-more-iconic-band/imageinfo.png)
On searching for windows 7 memory vulnerabilites, I found out that it loads the SAM file that stores users passwords into the memory and the passwords are stored here in a hashed format. To get those password hashes the <code>hashdump</code> plugin of volatility can be used with the profile we found using imageinfo:
![alt text]({{site.baseurl}}/assets/Name-a-more-iconic-band/hashdump.png)

The hash in the final column is the password hash and can be cracked using [crackstation](https://crackstation.net/): 
```
supercollider
anyone can play guitar
my iron lung
karma police
idioteque
pyramid song
there, there
weird fishes/arpeggi
lotus flower
burn the witch
```
On sorting and hashing the passwords (according to the question) - <code>cf271c074989f6073af976de00098fc4</code>

## Flag

```
rgbCTF{cf271c074989f6073af976de00098fc4}
```

