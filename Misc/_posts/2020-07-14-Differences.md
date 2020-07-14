
---
layout: post
title: "Differences"
author: "INXS_JOY"
tags: ['Misc']
---

If a difference could difference differences from differences to calculate differences, would the difference differently difference differences to difference the difference from different differences differencing?

## Solution
Well, its pretty evident that the solution has something to do with difference xD.
I inspected the java file given and found some special characters in the places of normal characters. For example, instead of import, the file has impor? where ? is some special character. I had an intuition that a difference should be taken between the hex values of special characters and the intended character.

Like, in "impor?" we know that t should occur instead of ? . Looking through the hex dump of the java file we see that the hex code of the special character is E6. Hex value of 't' is 74. Now we hex subtract E6-74 which gives 72 whose ASCII equivalent is 'r' which is the first letter of the flag. Doing this for all the special letters strings together the flag.

## Flag
>rgbCTF{tr1pl3_m34n1Ng}
