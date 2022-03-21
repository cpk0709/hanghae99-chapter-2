import string
from pprint import pprint

# 1번째 예시

# text = "hello my name is sparta"
#
# counter = {}
# # 21 번 연산
# for char in text:
#     if not char.isalpha():
#         continue
#     if char in counter:
#         counter[char] += 1
#     else:
#         counter[char] = 1
# pprint(counter)
#
#
# counter2 = {}
# # 26 * 21 번 연산
# for lo in string.ascii_lowercase:
#     for char in text:
#         if lo == char:
#             if lo in counter2:
#                 counter2[lo] += 1
#             else:
#                 counter2[lo] = 1
# pprint(counter2)


# 2번째 예시 아래것은 내가 작성해본 코드

# numarray = [2,5,6,1,2,4,1,4,2,9,1]
#
# num = 1
#
# count = 0
#
# for n in numarray:
#     if num == n:
#         count += 1
#
# print(count)

# sArray = 'baekjoon'
# result = []
# for lo in string.ascii_lowercase:
#     result.append(sArray.find(lo))
#
# print(result)
#
# result = range(len(string.ascii_lowercase))
# print(result)
#
# for j in result:
#     print(string.ascii_lowercase[j])

def get_idx_naive(word):
    result = [-1]*len(string.ascii_lowercase)
    for i in range(len(word)):
        char = word[i]
        for j in range(len(string.ascii_lowercase)):
            lo = string.ascii_lowercase[j]
            if result[j] == -1 and char == lo:
                result[j] = i
    print(' '.join([str(num) for num in result]))


# def get_idx(word):
#     # point 1. ord
#     # point 2. O(n^2) -> O(n)
#     result = [-1]*len(string.ascii_lowercase)
#     for i in range(len(word)):
#         idx = ord(word[i]) - 97
#         if result[idx] == -1:
#             result[idx] = i
#     print(' '.join([str(num) for num in result]))
#

get_idx_naive('baekjoon')
# get_idx('baekjoon')