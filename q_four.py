from typing import List

# 배열 파티션

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()

        answer = 0

        for el in range(0,len(nums),2):
            answer += nums[el]

        print(answer)


sol = Solution()

sol.arrayPairSum([1,4,3,2])