---
layout: post
title: "Object Oriented Programming"
author: "raghul-rajasekar"
---

There's this small up and coming language called java I want to tell you about

**Files:**
- [src.zip]({{site.baseurl}}/assets/Object-Oriented-Programming/src.zip)

## Solution

Extracting from `src.zip` gives us a bunch of Java files with two-letter names and an rather verbose `Main.java` file. Each two-letter Java file has several two-letter functions, each returning some other two-letter string. The gist of `Main.java` is:
- It takes as input a string of length 16 from the user.
- It first converts this input into a new string by XORing each character with a "secure encryption key", which is the difference between the characters at index 7 and 1 of the canonical name of the encryption key generator class.
	- I don't have much knowledge of Java, so I guessed this canonical name is `Main.EncryptionKeyInstantiator.EncryptionKeyFactory`, which would mean the encryption key is 2. Thankfully, I was right :)
- It breaks up the new string into 4 chunks of 4 characters each.
- For each chunk, it encrypts it as follows:
	- From the Java file having the first half of the chunk (of length 2 characters) as its name, it calls the function whose name matches the second half of the chunk.
	- The function in the same Java file whose name matches the return value of the first function is called.
	- The function in the same Java file whose name matches the return value of the second function is called.
	- The return value of the third function is the final encryption of the chunk.
- Once the input is converted into an 8-character string in this manner, it checks if this string equals the package name of `scanner` (without any punctuation), which I found out is `javautil`. If so, the user input is the flag.

This sufficiently detailed explanation should be enough to get the flag. The chunks corresponding to `ja`, `va`, `ut` and `il` were found to be `glvg`, `prpk`, `qgam` and `fggg` respectively. XORing `glvgprpkqgamfggg` with 2 gave `enterprisecodeee`, which was the flag.

## Flag

```
rgbCTF{enterprisecodeee}
```
