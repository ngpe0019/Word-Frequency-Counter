# -*- coding: utf-8 -*-
"""
Created on Sun Oct 19 17:23:29 2025

@author: joeyj
"""

file=input('insert your txt file title:')
files=open(file)
#this is for punctuation removal
import re
lst=[]
dct=dict()

#breaking down characters in the text into individual variable in a list.
for fh in files:
    fh=fh.strip()
    fh=fh.lower()
    #print(fh)
    #this line below removes the punctuations in the txt
    #[^\w\s] means "anything that is not a word character or whitespace."
    clean_text = re.sub(r'[^\w\s]', '', fh)
    ct=clean_text.split()
    for c in ct:
        lst.append(c)
        

for d in lst:
    dct[d]=dct.get(d,0)+1

word_c=[]
for k,v in dct.items():
    wf=(v,k)
    word_c.append(wf)
    word_d=sorted(word_c,reverse=True)
    word_e=word_d[:10]

print('ten most common words:')
for vv,kk in word_e:
    print(kk,vv)