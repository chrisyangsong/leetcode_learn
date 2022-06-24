#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length = len(digits)
        length -= 1
        sum_value = 0
        for element in digits:
           sum_value  += element * 10**length
           length -= 1
        sum_value += 1
        sum_value = str(sum_value)
        list_sum = list(sum_value)
        list_sum_int = [int(element) for element in list_sum]
        # print(list(sum_value))
        return list_sum_int
# @lc code=end

