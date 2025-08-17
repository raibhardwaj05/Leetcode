class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums):
                if i != j and (num1 + num2) == target:
                    return [i, j]
        return []


obj = Solution()

nums = list(map(int, input().split(',')))
tar = int(input())

positions = obj.twoSum(nums, tar)
print(positions)