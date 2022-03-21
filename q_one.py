from typing import List

# 애너그램

# strA = 'dared'
# strB = 'bread'

# def anagrams(a,b):
#     # 받은 문자를 변수에 담아줌
#     strA = a
#     strB = b
#
#     # 받은 문자열 길이만큼의 배열
#     strAarray = range(len(strA))
#
#     sameCount = 0
#
#     for i in strAarray:
#         char = strA[i]
#         for j in strAarray:
#             if char == strB[j]:
#                 sameCount += 1
#
#     result = (len(strA) + len(strB)) - sameCount
#
#     print(result)
#
# anagrams('aabbcc','xxyybb')



#######

# def funName(x: str, y: float = 6.5) -> int:
#     return x + y
#
#
# value = funName(3,2.5)
# print(value)

#######

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #최종 답안을 리턴할 빈 배열
        answer = []
        #키별로 동일한 알파벳 보유한 단어들 모아둘 목적
        dic = {}

        # 입력받은 배열의 요소 하나하나 for문으로 돌림
        for el in strs:
            # strs의 각 요소를 배열로 만들고, sorted로 오름차순으로만든 후 공백없이 다시 join(붙이는)작업
            temp = "".join(sorted(list(el)))
            # Anagrams_dic의 key로 temp가 있다면 58번째 줄, 아니면 61번째줄
            if temp in dic.keys():
                # Anagrams_dic에서 key가 temp에 el을 추가해줌
                dic[temp].append(el)
            else:
                # Anagrams_dic에 el이 키로 없어서, 여기서 추가
                dic[temp] = [el]
        print(dic)
        for key in dic.keys():
            answer.append(dic[key])

        return answer


sol = Solution()

result = sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"])

print(result)
