class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        index = 0
        while index <= len(haystack) - len(needle):
            if haystack[index] == needle[0]:
                # try to check word
                j = 1
                found = True
                while j < len(needle):
                    if haystack[index + j] != needle[j]:
                        found = False
                        break
                    j += 1
                if found:
                    return index
            index += 1
        return -1


solution = Solution()
print(solution.strStr("sadbutsad", "sad"))
print(solution.strStr("leetcode", "leeto"))
