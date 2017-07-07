# wordclean=sorted(list(set([word.strip().lower() for word in open('words','r')])))
# print(wordclean[:10])

# def signature(word):
#     return ''.join(sorted(word))


# def anagram(myword):
#     return [word for word in wordclean if signature(word)==signature(myword)]

# #print(anagram('dictionary'))

# import collections

# words_bysig = collections.defaultdict(list)
# for word in wordclean:
#     words_bysig[signature(word)].append(word)

# def anagram_fast(myword):
#     return words_bysig[signature(myword)]

# #print(anagram_fast('dictionary'))

# def words_by_len(wordlist):
#     words_by_len = collections.defaultdict(list)
#     for word in wordlist:
#         words_by_len[len(word)].append(word)
#     return words_by_len



# def anagram_all(myword):
#     return [anagram_fast(word) for word in myword if len(anagram_fast(word))>1]

# def count_anagram_len(wordlist):
#     anagram_count = {}
#     wordlist=words_by_len(wordlist)
#     for key,value in wordlist.items():
#         anagram_count[key] = len(anagram_all(value))
#     return anagram_count
#http://courses.csail.mit.edu/6.867/wiki/images/3/3f/Plot-python.pdf
#https://help.github.com/articles/adding-a-file-to-a-repository-using-the-command-line/

# #print(count_anagram_len(wordclean))
import numpy as np

import matplotlib.pyplot as pp

a = np.array([1,2,3,4,5])

print(a)

np.save('example.npy',a)
#print(np.linspace(0,10,5))

x=np.linspace(0,10,40)
sinx = np.sin(x)

pp.plot(x,sinx)
pp.show()