---
layout: post
title: "Typeracer"
author: "anishbadhri"
tags: ['Web']
---

I AM SPEED! Beat me at TypeRacer and the flag is all yours!
[http://challenge.rgbsec.xyz:8973/](http://challenge.rgbsec.xyz:8973/)

## Solution

The webpage requires a high wpm to get the flag. This can be done by inserting a script to read from the textbox and then performing the corresponding keystrokes.

However, the textbox doesn't store the text directly but is jumbled into a random order. The text can be rearranged by using the **order** attribute of each word.

Then, from the the constructed string, the keypress of each character is simulated and leads to a high wpm.

The webpage returns a base64 encoded string. On decoding this string, the flag is obtained.

**Solution**:
- [solution.html]({{site.baseurl}}/assets/Typeracer/solution.html)

## Flag
```
rgbCTF{w40w_j4v42cr1p7_12_4nn0y1ng}
```