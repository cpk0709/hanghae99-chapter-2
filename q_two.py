# 가장 긴 팰린드롬 부분 문자열

# 해설하나 안 보고 저의 의식의 흐름대로 작성한 부끄러운코드입니다.
# 이 사람은 이렇게 생각하는구나.. 하면서 흥미롭게 봐주세요

# 우선 팰린드롬의 규칙성이 뭐가있을까 하면서 패턴을 관찰했습니다.
# abccccdd 의 경우 dccaccd 혹은 dccbccd 이렇게 2가지 경우가 나올 수 있습니다.
# 여기서 제가 생각한 패턴은, 정 가운데 홀수 1개, 그리고 나머지는 짝수이며 정 가운데를 기준으로 양쪽에 펼쳐진다고 생각했습니다.
# 그럼 짝수인 알파벳의 수량에 1개인 알파벳을 더하면 문제가 해결될거같다고 생각했습니다.
# 문제는 1개인 알파벳이 여러개일 수 있기에 한 번만 더해야하는 처리도 해줘야한다고 생각했습니다.

# 설명이 많이 부족하겠지만 최대한 자세히 주석으로 설명하겠습니다

class Solution:
    def longestPalindrome(self, s: str) -> int:
        # 최종 답안을 저장할 변수입니다.
        answer = 0
        # 각 알파벳이 몇개씩 있는지 저장하기위해 딕셔너리하나 만들었습니다.
        dic = {}
        # 알파벳이 하나 있을경우 1을 저장할 변수입니다.
        one = 0

        # 우선 문자열이 들어있는 s를 list로 변환하면서 for in 으로 돌립니다. 알파벳 하나하나 el에 들어갑니다.
        for el in list(s):
            # dic에 key가 el이 있는 경우 28번 줄을 실행합니다. 없으면 31번 줄을 실행합니다.
            if el in dic.keys():
                # dic에서 key가 el인 곳에 el을 추가해줍니다.
                dic[el].append(el)
            else:
                # dic에 key가 el인 값을 넣어줍니다.
                dic[el] = [el]

        print(dic) # {'a': ['a'], 'b': ['b'], 'c': ['c', 'c', 'c', 'c'], 'd': ['d', 'd']}

        # 이제 카운트를 할겁니다. for문을 돌립니다. dic의 key 들을 for문의 key에 넣고있습니다.
        for key in dic.keys():
            # one 이 1이 아니라면, 아직 알파벳이 하나인놈이 안나온겁니다. one이 아직 0일경우 계속 저 if문을 거쳐야해서 비효율적입니다.
            if one != 1:
                # dic[key]의 길이가 1이면 one에 카운트 1을 올려줍니다. one이 1이되면 이제 여기로 들어올 일은 없습니다.
                if len(dic[key]) == 1:
                    one += 1

            # dic[key]의 길이를 2로 나누었을때 나머지가 0이면 짝수이기에 answer 에 짝수의 길이를 더해줍니다.
            if len(dic[key]) % 2 == 0:
                answer += len(dic[key])

        # 이제 마무리로 answer의 길이에 1을 더해주고 리턴합니다.
        answer += one

        return answer

sol = Solution()

result = sol.longestPalindrome('abccccdd')

print(result)


########개선코드

def longestPalindromeAnswer(s:str) -> str:
    #팬린드롬 판별 및 투 포인터 확장
    def expand(left:int,right:int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    # 해당 사항이 없을 때 빠르게 리턴
    if len(s) < 2 or s == s[::-1]:
        return s

    result = ''
    # 술라이딩 윈도우 우측으로 이동
    for i in range(len(s)-1):
        result = max(result,
                     expand(i, i+1),
                     expand(i, i+2),
                     key=len)
    return result


result2 = longestPalindromeAnswer("babad")
print(result2)

