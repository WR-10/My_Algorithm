# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# nums에 있는 숫자를 더해 타겟과 같으면 배열에서 그 숫자 꺼내오기


class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]