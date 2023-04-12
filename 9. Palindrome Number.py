# Solution 1

# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#             num_to_str = str(x)
#             reversed_num = num_to_str[::-1]
#             print(reversed_num)
#             if num_to_str == reversed_num:
#                 return True
#             return False

# Solution 2
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        reverse_number = 0
        stored_x = x
        while x != 0:
            reverse_number = reverse_number * 10 + x % 10
            x //= 10
        if reverse_number == stored_x:
            return True
        return False
