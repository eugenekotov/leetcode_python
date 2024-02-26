def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    result = ''
    symbolIndex = 0
    finished = False
    firstWord = strs[0]
    while not finished and symbolIndex < 200:
        if len(firstWord) <= symbolIndex:
            # we finished
            break

        symbol = firstWord[symbolIndex]
        wordIndex = 1
        while wordIndex < len(strs) and not finished:
            word = strs[wordIndex]
            if len(word) <= symbolIndex:
                # we finished
                finished = True
                break
            if (not word[symbolIndex] == symbol):
                # we finished
                finished = True
                break
            wordIndex += 1

        if not finished:
            result = result + symbol
            symbolIndex += 1

    return result


strs1 = ["abc", "abc", "abcd", "abcwerd", "abcwed"]
strs2 = ["", "abc", "abcd", "abcwerd", "abcwed"]
strs3 = ["d", "abc", "abcd", "abcwerd", "abcwed"]
strs3 = ["abc", "abcd", "abcwerd", "d"]
longestCommonPrefix(strs1)
longestCommonPrefix(strs2)
longestCommonPrefix(strs3)
