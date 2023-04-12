# class Solution:
#     def romanToInt(self, s: str) -> int:

def romanToInt(s: str) -> int:
    mydict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
        'IV': -2,
        'IX': -2,
        'XL': -20,
        'XC': -20,
        'CD': -200,
        'CM': -200
    }
    value = 0
    for i in range(len(s)):
        value += mydict[s[i]]
        if i != 0 and s[i - 1] + s[i] in mydict:
            value += mydict[s[i - 1] + s[i]]

    return value


print(romanToInt("IIX"))
