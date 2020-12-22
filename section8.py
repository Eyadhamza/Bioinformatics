
alphabetSize = 256


def karp(pattern, text, primeNumber):

    patternLength = len(pattern)
    textLength = len(text)
    patternHash = 0 # Hash value for the pattern
    textHash = 0 # hash value for the text
    for i in range(patternLength):
        # 256^0*ascii+s56^1*ascii.........
        # we calculate each hash value in the first loop
        patternHash = (alphabetSize * patternHash + ord(pattern[i])) % primeNumber
        textHash = (alphabetSize * textHash + ord(text[i])) % primeNumber
    # the second loop we loop over all alignments
    for i in range(textLength - patternLength + 1):
        # if the two hashes are equal it means they are similar
        if patternHash == textHash:
            # if they are similar we make sure that the characters are equal
            for j in range(patternLength):
                if text[i + j] != pattern[j]:
                    break
            # each time we find a match we increment the value of j
            j += 1
            if j == patternLength: # if the number of j = the length
                print("pattern is found at index " + str(i))

        # if the previous window didn't match the text we will calculate the next
        # window using the formula :
        if i < textLength - patternLength:
            textHash = (alphabetSize * (textHash - pow(alphabetSize, patternLength - 1) * ord(text[i])) + ord(text[i + patternLength])) % primeNumber

            # sometimes we can get negative values so this fixes it ..
            if textHash < 0:
                textHash = textHash + primeNumber


text = "THERE WOULD HAVE BEEN A TIME FOR SUCH A WORLD"
pattern = "WORLD"
q = 101
karp(pattern, text, q)
