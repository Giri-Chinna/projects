"""Count number of occurance of each character"""
text = 'yyyyyyeeessssssssssssxxxxx'

from collections import Counter

c = Counter(text)
print(c)
print(c.most_common(1))