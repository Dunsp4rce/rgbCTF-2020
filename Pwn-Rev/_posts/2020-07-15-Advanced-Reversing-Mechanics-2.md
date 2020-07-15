---
layout: post
title: "Advanced Reversing Mechanics 2"
author: "raghul-rajasekar"
---
More advanced than very very advanced  

`0A, FB, F4, 88, DD, 9D, 7D, 5F, 9E, A3, C6, BA, F5, 95, 5D, 88, 3B, E1, 31, 50, C7, FA, F5, 81, 99, C9, 7C, 23, A1, 91, 87, B5, B1, 95, E4,`

**Files:**
- [hard.o]({{site.baseurl}}/assets/Advanced-Reversing-Mechanics-2/hard.o)

## Solution

Popping `hard.o` into Ghidra, we get the following decompiled code for `encryptFlag`:
```C
void encryptFlag(byte *param_1)

{
  byte *pbVar1;
  byte *pbVar2;
  uint uVar3;
  byte bVar4;
  uint uVar5;
  uint uVar6;
  
  bVar4 = *param_1;
  pbVar1 = param_1;
  if (bVar4 == 0) {
    return;
  }
  while( true ) {
    uVar5 = (uint)bVar4;
    uVar3 = uVar5 - 10 & 0xff;
    uVar6 = uVar5;
    if ((bVar4 < 0x50) && (uVar6 = uVar3, 0x50 < uVar3)) {
      uVar6 = uVar5 + 0x46 & 0xff;
    }
    uVar6 = (uVar6 - 7 ^ 0x43) & 0xff;
    pbVar2 = pbVar1 + 1;
    *pbVar1 = (byte)(uVar6 << 6) | (byte)(uVar6 >> 2);
    bVar4 = *pbVar2;
    if (bVar4 == 0) break;
    uVar6 = (int)(pbVar2 + -(int)param_1) % 5;
    bVar4 = bVar4 << (-uVar6 & 7) | bVar4 >> (uVar6 & 0xff);
    if (uVar6 == 2) {
      bVar4 = bVar4 - 1;
    }
    *pbVar2 = bVar4;
    bVar4 = *pbVar2;
    pbVar1 = pbVar2;
  }
  return;
}
```

From this, I wrote my own `forward` and `reverse` functions in Python to encrypt and decrypt a character `c` at position `ind` respectively:
```python
def forward(ind, c): 
    ind %= 5 
    c = ((c << (-ind & 7)) | (c >> ind)) & 0xff 
    if ind == 2: 
        c -= 1 
    c3 = (c - 10) & 0xff 
    if c < 0x50: 
        if 0x50 < c3: 
            c = (c + 0x46) & 0xff 
        else: 
            c = c3 
    c = (c - 7 ^ 0x43) & 0xff 
    c = ((c << 6) | (c >> 2)) & 0xff 
    return c

def reverse(ind, c): 
    ind %= 5 
    orig = c 
    c = ((c >> 6) | (c << 2)) & 0xff 
    c = ((c ^ 0x43) + 7) & 0xff 
    candidate = [] 
    candidate.append(c) 
    candidate.append((c + 10) & 0xff) 
    candidate.append((c - 0x46) & 0xff) 
    for ch in candidate: 
        if ind == 2: 
            ch += 1 
        ch = ((ch >> (-ind & 7)) | (ch << ind)) & 0xff 
        if forward(ind, ch) == orig: 
            return ch 
    return 0 
```
> Note: Since the forward function has three cases depending on the original ASCII value of the character, we evaluate three candidates for the reverse function and see which candidate consistently gets encrypted to give the original ciphertext character.

We apply this reversing procedure to the list of ASCII values given to retrieve the flag.

## Flag

```
rgbCTF{ARM_ar1thm3t1c_r0cks_fad961}
```
