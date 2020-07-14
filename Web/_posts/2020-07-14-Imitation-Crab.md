---
layout: post
title: "Imitation-Crab"
author: "shreyas-sriram"
tags: ['Web']
---

Flag should be modified to fit the rgbCTF format (rgbCTF{flag}, underscores between words) 

Site: `http://challenge.rgbsec.xyz:7939/`

## Solution

* Going through the source code, there is an `EventListener` for `keyup`
* This listener has a `fetch` call to `/search` as seen below<br/>
```
fetch('/search', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ 'char': e.keyCode }),
            })
```
* Visit `/robots.txt`, find a path to a `har` file<br/>
```
/static/export.har
```
* Download the `har` file from `http://challenge.rgbsec.xyz:7939/static/export.har`
```
Google : The HTTP Archive format, or HAR, is a JSON-formatted archive file format for logging of a web browser's interaction with a site.
```
* It is known that there is a `POST` request to `/search` as shown above
* Thus searching for `post` in `export.har` reveals the following<br/>
```
"postData": {
            "mimeType": "application/json",
            "text": "{\"char\":<char-code>}"
          }
```
* Parsing all the `<char-code>` data and converting to string reveals the flag

[solution script]({{site.baseurl}}/assets/Imitation-Crab/parse.py)

## Flag

`rgbCTF{H4R_F1L3S_4R3_2UP3R_US3FU1}`