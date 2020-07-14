---
layout: post
title: "Countdown"
author: "anishbadhri"
tags: ['Web']
---

This challenge is simple. All you have to do is wait for the countdown to end to get the flag. The countdown ends one second before the end of the CTF, but you have fast fingers right?

[http://challenge.rgbsec.xyz:5000/](http://challenge.rgbsec.xyz:5000/)

## Solution

The webpage sets a cookie named session which looks like a flask cookie.

Flask cookies can be decoded with the tool in [https://github.com/noraj/flask-session-cookie-manager](https://github.com/noraj/flask-session-cookie-manager).

This requires the cookie key to be known. The webpage gives a clever hint saying "**Time** is key.". On running the below command, a time in UTC is obtained which is just one second before contest end. 
```
python3 flask_session_cookie_manager3.py decode -c eyJlbmQiOiIyMDIwLTA3LTEzIDE
2OjU5OjU5KzAwMDAifQ.Xw0_6w.ncXEyMhtRm-_AdkiXkk7byTX-Cw -s Time
```
By changing endtime to a much earlier time, and running the below command, a new cookie is obtained.
```
python3 flask_session_cookie_manager3.py encode -s Time -t '{"end": "2020-07-10 16:59:59+0000"}'
```
On setting replacing the session cookie with the new cookie, the flag is obtained.

## Flag
```
rgbCTF{t1m3_1s_k3y_g00d_j0k3_r1ght}
```
