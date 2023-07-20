# Given an integer array nums, return the number of subarrays filled with 0.
# A subarray is a continuous, non-empty sequence of elements within an array.
from ast import List


def zeroFilledSubarray(self, nums: List[int]) -> int:
    total_zero_subarrays = current_zero_subarrays = 0
                
    for num in nums:
        if num == 0:
            current_zero_subarrays += 1
            total_zero_subarrays += current_zero_subarrays
        else:
            current_zero_subarrays = 0
    return total_zero_subarrays
