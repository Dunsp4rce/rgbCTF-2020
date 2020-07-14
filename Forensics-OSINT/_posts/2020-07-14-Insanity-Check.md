---
layout: post
title: "Insanity Check"
author: "vishalananth"
tags: ['Forensics-OSINT']
---

There's a flag in our Discord server. Can you get it?
Server Link: [https://discord.gg/CfhfYPQ](https://discord.gg/CfhfYPQ)

## Solution

After reading all channels, extracting random images/videos posted by mods and going nearly insane, I thought I will download the discord server's display pic and check if it had the flag. So open developer tools in the browser with ```Ctrl+Shift+i``` and use the object finder to click and download the image:

![alt text]({{site.baseurl}}/assets/Insanity-Check/i2.png)

Running zsteg on the image gave the flag:

```
zsteg i2.png
```