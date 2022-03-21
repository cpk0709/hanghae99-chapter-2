# import collections
# from typing import List
#
#
# def groupAnagrams(strs:List[str]) -> List[List[str]]:
#     anagrams = collections.defaultdict(list)
#
#     for word in strs:
#         anagrams[''.join(sorted(word))].append(word)
#         print(anagrams)
#     return  list(anagrams.values())
#
# result = groupAnagrams(["eat","tea","tan","ate","nat","bat"])
# print(result)
#
# # test = collections.defaultdict(list)
# # print(test)
# # test['abc'].append('ab')
# # test['abc'].append('rt')
# # test['def'].append('cd')
# # print(test.values())
# # print(list(test.values()))

######
#
# test = 'abc'
#
# print(test[::-1])

######
# a = [1,2,3]
# b = ['a','b','c','d']
#
# for i,s in zip(a,b):
#     print(i,s)
#     print(i)
#     print(s)
#     print("@@")

# a = [1,2,3]
# print(a[:])

