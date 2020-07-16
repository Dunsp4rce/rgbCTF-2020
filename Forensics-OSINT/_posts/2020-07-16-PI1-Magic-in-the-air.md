---
layout: post
title: "PI 1: Magic in the air"
author: "AnandSaminathan"
---

We are investigating an individual we believe is connected to a group smuggling drugs into the country and selling them on social media. You have been posted on a stake out in the apartment above theirs and with the help of space-age eavesdropping technology have managed to extract some data from their computer. What is the phone number of the suspect's criminal contact?

flag format includes country code so it should be in the format: rgbCTF{+00000000000}

**Files**
- [magic_in_the_air.7z](https://ctf.rgbsec.xyz/download?file_key=2458aa8109f1ea603e2ed5f45b89d52d7842298b3d2271b1fc9a3980fb997f5b&team_key=880b40ef36c4a406429f54505951ee9e2df7f810d05918eac0d01e973acd3551)


## Solution

On extracting the given file, we got a btsnoop or bluetooth snoop file. These files can be opened using <code>Wireshark</code>. On opening using <code>Wireshark</code>, we were able to see the snooped packets:
![alt text]({{site.baseurl}}/assets/PI1-Magic-in-the-air/btsnoop.png) 
After analysing, we found that there was some conversation between the devices <code>G613</code> and <code>localhost</code>, on searching for G613 it turned out to be a Logitech wireless keyboard. 
We saw a lot of different protocols used, among which <code>ATT</code> seemed to be the important one. As shown in the image, there was a value field in the packets using ATT protocol whose 2nd byte kept changing in a series of packets from the keyboard to the localhost (packets of length 18) - we assumed that those packets contained the information about the key pressed on the keyboard. We tried converting some of the 2nd bytes to plain string assuming that it's ASCII and didn't get any meaningful string. On searching more, we found that the keyboards use something called [HID scan codes](https://gist.github.com/MightyPork/6da26e382a7ad91b5496ee55fdc73db2), were each key is mapped to some hex value. On manually decoding some of the 2nd bytes from the value packets, it resulted in some meaningful strings.
With this intel, we filtered all those packets with length 18, added the value field as a column, removed all the other columns and exported the resulting table as a CSV and removed everything other than the 2nd bytes. Then on substituting each row of the exported data with the scan codes from the above link (using sed in vim), we got the message:
```
yoo man
sorrry for thhe delay  lol

tryiinng to geet  tyithhis  keybboard workiinnnnn

yeeeaa  its  nneew wireless mang 

beeen mmovviinng  pproduct

sspeaakiinnnn  of yoou nneeded too ccoonntaact  mmy  boy right

ye

shoouldd  bbe ffiine just ssaay johnny h sent yoou

alrighht lemme geet yoouu  thee  numbeer

hhold uup imm  loookiingg forr  it


itss  hhiss  bburner gott  iit wwritttenn downn ssoommewhere


yeeahh got it

00736727859

miind it  is aa sswwwedishh nnumbeer he ggot  it  oonn hhollidaay theere ffeww  mmoonthhs  bbacck

yeahh yoouu can buuy  bburnneers ssuupper eaasiily theere

aalrighht g

yeeaah  its  donny l

rremembeer to tell hiimm i sent yoou

peeace
```

So the number of the criminal contact should be <code>736727859</code>, the question also says that we have to include the country code. From the message, we saw that the country was Sweden - country code is <code>+46</code>. 
Final number - <code>+46736727859</code>.


## Flag
```
rgbCTF{+46736727859}
```

