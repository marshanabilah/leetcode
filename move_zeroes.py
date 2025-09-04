from typing import List

def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero_position = 0
      
        for current_index, current_value in enumerate(nums):
            if current_value != 0:
                nums[non_zero_position], nums[current_index] = nums[current_index], nums[non_zero_position]
                non_zero_position += 1