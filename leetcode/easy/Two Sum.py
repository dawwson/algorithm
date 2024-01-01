# 풀이 날짜 : 2024.01.01
# 문제 유형 : Array, Hash Table
# 문제 제목 : Two Sum
# 문제 링크 : https://leetcode.com/problems/two-sum/

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i, n1 in enumerate(nums):
            for j, n2 in enumerate(nums):
                if i == j:
                    continue
                if n1 + n2 == target:
                    return [i, j]
