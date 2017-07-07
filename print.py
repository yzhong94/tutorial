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


# #print(count_anagram_len(wordclean))
import numpy as np

import matplotlib.pyplot as pp

a = np.array([1,2,3,4,5])

a