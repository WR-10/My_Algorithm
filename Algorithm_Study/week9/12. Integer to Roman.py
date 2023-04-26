class Solution:
    def intToRoman(self, num: int) -> str:
        rom = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        val = [1, 5, 10, 50, 100, 500, 1000]

        result =''
        for i in range(len(val) -1, -1, -1):
            if num >= 900 and num < 1000:
                result += 'CM'
                num -= 900
            elif num >= 400 and num < 500:
                result += 'CD'
                num -= 400
            elif num >= 90 and num < 100:
                result += 'XC'
                num -= 90
            elif num >= 40 and num < 50:
                result += 'XL'
                num -= 40
            elif num == 9:
                result += 'IX'
                num -= 9
            elif num == 4:
                result += 'IV'
                num -= 4
            else:
                quo = num // val[i]
                for k in range(quo):
                    result += rom[i]
                num -= quo * val[i]

        return result


a = Solution()

re = a.intToRoman(2450)
print(re)
            


"""
https://leetcode.com/problems/integer-to-roman/

문제:숫자 로마자로 바꾸기

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

-예외
I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.



"""