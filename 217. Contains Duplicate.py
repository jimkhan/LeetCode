# Solution 1
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         my_set = set(nums)
#         if len(my_set) == len(nums):
#             return False
#         return True

# Solution 2
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for ind, item in enumerate(nums):
            if ind == 0:
                continue
            elif nums[ind - 1] == nums[ind]:
                return True

        return False
