---
layout: post
title: "Advanced Reversing Mechanics 1"
author: "raghul-rajasekar"
---

Very very advanced trust me  

`71, 66, 61, 42, 53, 45, 7A, 40, 51, 4C, 5E, 30, 79, 5E, 31, 5E, 64, 59, 5E, 38, 61, 36, 65, 37, 63, 7C,`

**Files:**
- [easy.o]({{site.baseurl}}/assets/Advanced-Reversing-Mechanics-1/easy.o)

## Solution

Clearly, by the challenge name, the file is an ARM file. Opening it using Ghidra, the `main` function is decompiled to give:
```C
undefined4 main(undefined4 param_1,int param_2)

{
  char *pcVar1;
  byte *pbVar2;
  byte *pbVar3;
  byte local_110 [256];
  
  pbVar2 = local_110;
  pcVar1 = stpcpy((char *)local_110,*(char **)(param_2 + 4));
  while (local_110[0] != 0) {
    *pbVar2 = local_110[0] - 1;
    pbVar2 = pbVar2 + 1;
    local_110[0] = *pbVar2;
  }
  if (pcVar1 + -(int)local_110 != (char *)0x0) {
    pbVar2 = local_110;
    do {
      pbVar3 = pbVar2 + 1;
      printf("%02X, ",(uint)*pbVar2);
      pbVar2 = pbVar3;
    } while (local_110 + (int)(pcVar1 + -(int)local_110) != pbVar3);
  }
  putchar(10);
  return 0;
}
```

Seems like all the program does is decrements the ASCII value of each character and prints the value in hexadecimal form. Once we know what is happening, reversing it is a piece of cake and the flag is easily found.

## Flag

`rgbCTF{ARM_1z_2_eZ_9b7f8d}`

