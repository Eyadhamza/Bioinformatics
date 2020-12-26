# Python program for KMP Algorithm
def KMPSearch(pattern, txt):
    lengthOfPattern = len(pattern)
    lengthOfText = len(txt)

    # create longestProperPrefix[] that will hold the longest prefix suffix
    # values for pattern
    longestProperPrefix = [0] * lengthOfPattern
    patternIndex = 0  # index for pat[]

    # Preprocess the pattern (calculate longestProperPrefix[] array)
    computeLPSArray(pattern, lengthOfPattern, longestProperPrefix)

    textIndex = 0  # index for txt[]
    while textIndex < lengthOfText:
        if pattern[patternIndex] == txt[textIndex]:
            textIndex += 1
            patternIndex += 1

        if patternIndex == lengthOfPattern:
            print("Found pattern at index " + str(textIndex - patternIndex))
            patternIndex = longestProperPrefix[patternIndex - 1]  # reset the value of the pattern index

            # mismatch after patternIndex matches
        elif textIndex < lengthOfText and pattern[patternIndex] != txt[textIndex]:
            # Do not match longestProperPrefix[0..longestProperPrefix[patternIndex-1]] characters,
            # they will match anyway
            if patternIndex != 0: # if they are not matched we will reset the value
                # of the pattern index to be lps[index-1]
                # because remember that we want to make the new value is the value after
                # the already matched characters in the pattern because they will be matched anyway

                patternIndex = longestProperPrefix[patternIndex - 1]
            else:
                textIndex += 1


def computeLPSArray(pattern, lengthOfPattern, longestProperPrefix):
    len = 0  # length of the previous longest prefix suffix

    longestProperPrefix[0]  # longestProperPrefix[0] is always 0
    patternIndex = 1

    # AAACAAAA
    # [0,1,2,0  ] this is the LPS array

    # the loop calculates longestProperPrefix[i] for i = 1 to lengthOfPattern-1
    while patternIndex < lengthOfPattern:  # please dont forget that lengthOfPattern is the length of the pattern
        if pattern[patternIndex] == pattern[len]:
            len += 1
            longestProperPrefix[patternIndex] = len  # why ? remember the longest proper prefix

            patternIndex += 1  # to process the next char in the pattern
        else:  # why we are here ?
            # because the characters didn't match so we need to caluclate
            # if there are simmilarties in the whole pattern

            # This is tricky. Consider the example.
            # AAACAAAA and i = 7. The idea is similar
            # to search step.
            if len != 0:
                len = longestProperPrefix[len - 1]

                # Also, note that we do not increment i here
            else:
                longestProperPrefix[patternIndex] = 0
                patternIndex += 1


txt = "ABABDABACDABABCABAB"
pat = "ABABCABAB"
KMPSearch(pat, txt)
