---
layout: post
title: "Robin's Reddit Password"
author: "AnandSaminathan"
---

I'm Batman!
Lately Robin's been acting suspicious... I need to see what he's been up to. Can you get me his reddit password? Just don't try to break into reddit's server...

Tip : Wrap the Password in flag format


## Solution

Tired searching online and found almost nothing, and then the mod gave a clue asking "to focus on the reddit server and Robin might show up later". Because of one of the beginner challenges, where we extracted the password hashes (something similar to /etc/passwd file), we tried the URL [https://www.reddit.com/etc/passwd](https://www.reddit.com/etc/passwd) and luckily there were some username:password lines. Then on searching for this URL, we found multiple sources which had already cracked those hashes ([Hacker news](https://news.ycombinator.com/item?id=15596253)), the password of <code>robin</code> was <code>bird</code>


## Flag

```
rgbCTF{bird}
```


