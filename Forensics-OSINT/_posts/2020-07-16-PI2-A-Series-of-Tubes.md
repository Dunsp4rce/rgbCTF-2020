---
layout: post
title: "PI 2: A Series of Tubes"
author: "AnandSaminathan"
---


Use the personal information uncovered from PI 1 to find out where our suspect's contact lives, his full name and the next flight he is taking.

The flag for this challenge is in the following format: rgbCTF{firstnamelastname:homecity:countrycode:flightnumber}
where countrycode is the ISO 3166-1 Alpha 2 code

all lowercase, no whitespace or symbols


## Solution

In the first version of this problem, we found the phone number of the criminal contact - +46736727859 (some burner number). We tried searching for this tool online but couldn't find anything, also tried using the tool [PhoneInfoga](https://github.com/sundowndev/PhoneInfoga) - which also didn't produce anything useful. On asking the mod, he asked an interesting question "do people still send SMSs these days?", we then realised that this had something to do with WhatsApp. On checking the WhatsApp about of that phone number, we found this:
![alt text]({{site.baseurl}}/assets/PI2-A-Series-of-Tubes/whatsapp.jpeg) 

sc with a ghost emoji looked like snapchat. Then we searched snapchat for this number and we found a profile:
![alt text]({{site.baseurl}}/assets/PI2-A-Series-of-Tubes/sc.jpg) 
We got his full name - "donnylockheart"
The Snapchat account had a story with this persons instagram profile:
![alt text]({{site.baseurl}}/assets/PI2-A-Series-of-Tubes/story.jpg) 
On opening that instagram account - there was a flight ticket highlights:
![alt text]({{site.baseurl}}/assets/PI2-A-Series-of-Tubes/insta.jpg) 
But the important details were hidden (and first name is actually Donovan).
He also had another story which said "Digbeth. Got this crazy town right on the doorstep". So Digbeth had to be his home town - therefore, his home city had to be Birmingham and country had to be England - ISO 3166-1 Alpha 2 code is "GB".
Then we searched for flights with the visible information in his flight ticket and ended up with this:
![alt text]({{site.baseurl}}/assets/PI2-A-Series-of-Tubes/flight.jpg) 
With this we found the flight number - KL1426.

Putting it all together:
* First name: Donovan
* Last name: Lockheart
* Homecity: Birmingham 
* Country code: GB
* Flight number: KL1426
(Everything in the flag should be lowercase and no spaces) - donovanlockheart:birmingham:gb:kl1426


## Flag
```
rgbCTF{donovanlockheart:birmingham:gb:kl1426}
```





