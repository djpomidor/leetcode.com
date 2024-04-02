from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for x in range(len(nums)):
            for y in range(x+1, len(nums)):
                if (nums[x] + nums[y]) == target:
                    print(x, y)
                    return [x, y]

class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]] 


nums = [3,2,4]
target = 6
s = Solution2()
print(s.twoSum(nums,target))

                