---
layout: post
title: "Alien Transmission 1"
author: "INXS_JOY"
tags: ['Forensics-OSINT']
---

I was listening to my radio the other day and received this strange message... I think it came from an alien?

**Files**
- [squeakymusic.wav]({{site.baseurl}}/assets/Alien-Transmission-1/squeakymusic.wav)

## Solution
>People who have solved m00walk problem from picoCTF 2019 would immediately recognize this audo file.

The audio is a SSTV signal which are generally used to transmit images from space to earth. I used the program from this, [http://users.belgacom.net/hamradio/rxsstv.htm](http://users.belgacom.net/hamradio/rxsstv.htm) to decode the signal to give an image. The program would be listening for a signal and we just need to play the audio sample to it. The RX would be automatically identified. The signal gives us the following image:
![alt text]({{site.baseurl}}/assets/Alien-Transmission-1/Alien-Transmission-1.jpg) 

## Flag
```
rgbCTF{s10w_2c4n_1s_7h3_W4V3}
```
