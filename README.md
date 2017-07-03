# emailparser
while simple for humans, identifying and removing signature blocks is actually quite a challenging task for machines. by automatically identifying and removing signature blocks, emailparser streamlines large-scale email analysis.

## example
here is a sample email.
```
Wendy – thanks for the intro! Moving you to bcc.
 
Hi Vincent – nice to meet you over email. Apologize for the late reply, I was on PTO for a couple weeks and this is my first week back in office. As Wendy mentioned, I am leading an AR/VR taskforce at Foobar Retail Solutions. The goal of the taskforce is to better understand how AR/VR can apply to retail/commerce and if/what is the role of a shopping center in AR/VR applications for retail.
 
Wendy mentioned that you would be a great person to speak to since you are close to what is going on in this space. Would love to set up some time to chat via phone next week. What does your availability look like on Monday or Wednesday?
 
Best,
Joe Smith
 
Joe Smith | Strategy & Business Development
111 Market St. Suite 111| San Francisco, CA 94103
M: 111.111.1111| joe@foobar.com
```

after parsing with emailparser:
```
Wendy – thanks for the intro! Moving you to bcc.
 
Hi Vincent – nice to meet you over email. Apologize for the late reply, I was on PTO for a couple weeks and this is my first week back in office. As Wendy mentioned, I am leading an AR/VR taskforce at Foobar Retail Solutions. The goal of the taskforce is to better understand how AR/VR can apply to retail/commerce and if/what is the role of a shopping center in AR/VR applications for retail.
 
Wendy mentioned that you would be a great person to speak to since you are close to what is going on in this space. Would love to set up some time to chat via phone next week. What does your availability look like on Monday or Wednesday?
```

## getting started
```python
>>> from Parser import read_email, corpus2sentences, generate_text
>>> from spacy.en import English 

>>> pos_tagger = English()  # part-of-speech tagger
>>> msg_raw = read_email('emails/test1.txt')
>>> sentences = corpus2sentences(msg_raw)  # convert corpus into sentences

# iterate through lines, write to file if not signature block
>>> generate_text(sentences, pos, 'emails/test1_clean.txt', threshold=.9)
```