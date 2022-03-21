from typing import List

# def dailyTemperatures(T:List[int]) -> List[int]:
#     stack = []
#     answer = [0] * len(T)
#     for i in range(len(T)):
#         while stack and T[i] > T[stack[-1]]:
#             last = stack.pop()
#             answer[last] = i - last
#         stack.append(i)
#     return answer
#
# result = dailyTemperatures([73,74,75,71,69,72,76,73])
# print(result)

def dailyTemperatures(T:List[int]) -> List[int]:
    stack = []
    answer = [0] * len(T)
    for i in range(len(T)):
        while stack and T[i] > T[stack[-1]]:
            last = stack.pop()
            answer[last] = i - last
        stack.append(i)
    return answer

result = dailyTemperatures([73,74,75,71,69,72,76,73])

print(result)