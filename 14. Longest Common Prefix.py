# Solution 1
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         result = ""
#         first_item = strs[0]
#         for i in range(len(first_item)):
#             for item in strs:
#                 if len(item) == i or item[i] != first_item[i]:
#                     return result
#             result += first_item[i]
#
#         return result



def longestCommonPrefix(strs):
    result = strs[0]
    first_item = strs[0]
    for i in range(1, len(strs)):
        print(i)
        print(strs[i])
        # for item in strs:
        #     if len(item) == i or item[i] != first_item[i]:
        #         return result
        # result += first_item[i]

    return result


print(longestCommonPrefix(['Hello', 'Hela', 'He']))
