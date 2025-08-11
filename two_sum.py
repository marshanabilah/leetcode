from typing import List

def twoSum(self, nums: List[int], target: int) -> List[int]:
    seen = {}
    for i in range(len(nums)):
        y = target - nums[i]
        if y in seen:
            return [seen[y], i]
        else:
            seen[nums[i]] = i