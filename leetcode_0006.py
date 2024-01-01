class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        result = ""
        line = 0
        while line < numRows:
            i = 0
            while True:
                firstIndex = i * 2 * (numRows - 1) + line
                print(firstIndex)
                if firstIndex >= len(s):
                    print("break")
                    break
                # print(firstIndex)
                result = result + s[firstIndex]
                if line != 0 and line != numRows - 1:
                    secondIndex = i * 2 * (numRows - 1) + \
                        (numRows - 1) + (numRows - 1 - line)
                    if secondIndex < len(s):
                        # print(secondIndex)
                        result = result + s[secondIndex]
                i += 1
            line += 1

        # print(result)
        return result

# 3
#   0) -> 0,    4,    8,     12
#   1) -> 1, 3, 5, 7, 9, 11, 13
#   2) -> 2,    6,    10,    14

# 4
#   0) -> 0, 6, 12
#   1) -> 1, 5, 7, 11, 13
#   2) -> 2, 4, 8, 10, 14
#   3) -> 3, 9, 15


# 0 -> i*2*(n-1), i = 0,1,2,...
# 1 -> two parts 1): i*2*(n-1) + 1, 2) i*2*(n-1) + (n - 1) + (n - 1 - line)
# 2 -> two parts 1): i*2*(n-1) + 2, 2)
# ...
# (n - 1) ->  two parts 1): i*2*(n-1) + (n - 2), 2): i*2*(n-1) + (n - 1) + 1
# n -> i*2*(n-1) + (n - 1)

solution = Solution()

# 1
arg1 = "PAYPALISHIRING"
arg2 = 3
res1 = "PAHNAPLSIIGYIR"

if res1 != solution.convert(arg1, arg2):
    print("error")
else:
    print("Ok")

# 2
# arg1 = "PAYPALISHIRING"
# arg2 = 4
# res1 = "PINALSIGYAHRPI"

# if res1 != solution.convert(arg1, arg2):
#     print("error")
# else:
#     print("Ok")

# 3
# arg1 = "A"
# arg2 = 4
# res1 = "A"

# if res1 != solution.convert(arg1, arg2):
#     print("error")
# else:
#     print("Ok")
