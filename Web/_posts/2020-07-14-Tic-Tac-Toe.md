---
layout: post
title: "Tic-Tac-Toe"
author: "shreyas-sriram"
tags: ['Web']
---

Hello there, I invite you to one of the largest online global events in history ... the Tic Tac Toe World Championships!

Site: `http://challenge.rgbsec.xyz:8974/`

## Solution

> Note : This solution is unintended.

* Act dumb and just play the game
* One winning scenario which worked :
```
You : (1,1)
Bot : (0,0)
You : (2,2)
Bot : (0,2)
You : (2,1)
Bot : (2,0)
You : (0,1)
```
* Once you win, the flag is revealed in `base64` format<br/>
`cmdiQ1RGe2g0aDRfajR2NDJjcjFwN19ldjNuNzJfQVIzX2MwMEx9`
* Decode it to obtain the flag

## Flag

`rgbCTF{h4h4_j4v42cr1p7_ev3n72_AR3_c00L}`