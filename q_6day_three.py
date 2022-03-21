import itertools
from typing import List

### 직접구현
# def permute(nums:List[int]) -> List[List[int]]:
#     result = []
#     prev_elements = []
#
#     def dfs(elements):
#         if len(elements) == 0:
#             result.append(prev_elements[:])
#
#         for e in elements:
#             next_elements = elements[:]
#             next_elements.remove(e)
#
#             prev_elements.append(e)
#             dfs(next_elements)
#             prev_elements.pop()
#
#     dfs(nums)
#     return  result

### itertiools 사용
def permute(nums:List[int]) -> List[List[int]]:
    return list(itertools.permutations(nums))

result = permute([1,2,3])
print(result)
