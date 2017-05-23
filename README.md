# emailparser
while simple for humans, removing signature blocks is actually quite a challenging task for machines. by automatically identifying and removing signature blocks, emailparser should streamline large-scale email analysis.

## example
here is a sample email.
```
Wendy – thanks for the intro! Moving you to bcc.
 
Hi Vincent – nice to meet you over email. Apologize for the late reply, I was on PTO for a couple weeks and this is my first week back in office. As Wendy mentioned, I am leading an AR/VR taskforce at Westfield Retail Solutions. The goal of the taskforce is to better understand how AR/VR can apply to retail/commerce and if/what is the role of a shopping center in AR/VR applications for retail.
 
Wendy mentioned that you would be a great person to speak to since you are close to what is going on in this space. Would love to set up some time to chat via phone next week. What does your availability look like on Monday or Wednesday?
 
Best,
Subin
 
Subin Kim | Strategy & Business Development
835 Market St. Suite 517| San Francisco, CA 94103
M: 415.279.3933| subkim@westfield.com
```

after parsing with emailparser:
```
Wendy – thanks for the intro! Moving you to bcc.
Hi Vincent – nice to meet you over email. Apologize for the late reply, I was on PTO for a couple weeks and this is my first week back in office. As Wendy mentioned, I am leading an AR/VR taskforce at Westfield Retail Solutions. The goal of the taskforce is to better understand how AR/VR can apply to retail/commerce and if/what is the role of a shopping center in AR/VR applications for retail.

Wendy mentioned that you would be a great person to speak to since you are close to what is going on in this space. Would love to set up some time to chat via phone next week. What does your availability look like on Monday or Wednesday?
```

## getting started
```
>>> from Parser import read_email, strip, prob_block
>>> from spacy.en import English  # could use nltk
>>> pos = English()
>>> msg_raw = read_email('emails/test1.txt')
>>> msg_stripped = strip(msg_raw)
```