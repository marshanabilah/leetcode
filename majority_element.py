from typing import List

def majorityElement(self, nums: List[int]) -> int:
        seen = {}
        majority = len(nums)/2
        flag = False
        major_element = 0

        for i in nums:
            if i in seen:
                value = seen[i]
                seen[i] = value + 1
            else:
                seen[i] = 1
            
            for key, value in seen.items():
                if value > majority:
                    major_element = key
                    flag = True
                    break
            
            if flag:
                return major_element