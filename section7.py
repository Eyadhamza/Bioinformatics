
# Python program for KMP Algorithm
def KMPSearch(pat, txt):
    lengthOfPattern = len(pat)
    lengthOfText = len(txt)

    # create lps[] that will hold the longest prefix suffix
    # values for pattern
    lps = [0] * lengthOfPattern
    patternIndex = 0  # index for pat[]

    # Preprocess the pattern (calculate lps[] array)
    computeLPSArray(pat, lengthOfPattern, lps)

    textIndex = 0  # index for txt[]
    while textIndex < lengthOfText:
        if pat[patternIndex] == txt[textIndex]:
            textIndex += 1
            patternIndex += 1

        if patternIndex == lengthOfPattern:
            print("Found pattern at index " + str(textIndex - patternIndex))
            patternIndex = lps[patternIndex - 1]

            # mismatch after patternIndex matches
        elif textIndex < lengthOfText and pat[patternIndex] != txt[textIndex]:
            # Do not match lps[0..lps[patternIndex-1]] characters,
            # they will match anyway
            if patternIndex != 0:
                patternIndex = lps[patternIndex - 1]
            else:
                textIndex += 1


def computeLPSArray(pat, lengthOfPattern, lps):
    len = 0  # length of the previous longest prefix suffix

    lps[0]  # lps[0] is always 0
    patternIndex = 1

    # the loop calculates lps[i] for i = 1 to lengthOfPattern-1
    while patternIndex < lengthOfPattern:  # please dont forget that lengthOfPattern is the length of the pattern
        if pat[patternIndex] == pat[len]:
            len += 1
            lps[patternIndex] = len  # why ? remember the longest proper prefix

            patternIndex += 1  # to process the next char in the pattern
        else:  # why we are here ?
            # because the characters didn't match so we need to caluclate
            # if there are simmilarties in the whole pattern

            # This is tricky. Consider the example.
            # AAACAAAA and i = 7. The idea is similar
            # to search step.
            if len != 0:
                len = lps[len - 1]

                # Also, note that we do not increment i here
            else:
                lps[patternIndex] = 0
                patternIndex += 1


txt = "ABABDABACDABABCABAB"
pat = "ABABCABAB"
KMPSearch(pat, txt)

# This code is contributed by Bhavya Jain
