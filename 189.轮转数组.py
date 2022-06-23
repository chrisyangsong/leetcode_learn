#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 轮转数组
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums) #fix the length
        k = k % length # avoid too large k value
        nums_1 = len(nums) * [0]

        nums_1[:k+1] = nums[-1*k:]
        nums_1[k:] = nums[:len(nums)-k]
        print(nums_1[k:])
        nums[:]=nums_1[:] 
# @lc code=end

