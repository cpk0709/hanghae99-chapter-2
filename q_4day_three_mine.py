class Card:
    def __init__(self,num,next):
        self.num = num
        self.next = next



#################
# 정답 뜬 코드

# from collections import deque
#
# n = int(input())
# q = deque([i for i in range(1, n+1)])
#
# while len(q) != 1:
#     q.popleft()
#     q.append(q.popleft())
# print(q.pop())

#################
# 두 번째로 정답 뜬 코드. 좀 더 빠름

a1 = CardStack()
a1.push(6)
# for _ in range(5):
#     next = a1.last
#     string = ""
