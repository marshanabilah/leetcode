from typing import List

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    while n:
        if m and nums1[m-1] >= nums2[n-1]:
            nums1[m+n-1] = nums1[m-1]
            m -= 1
        else:
            nums1[m+n-1] = nums2[n-1]
            n -= 1
        