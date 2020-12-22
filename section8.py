# Following program is the python implementation of
# Rabin Karp Algorithm given in CLRS book

# d is the number of characters in the input alphabet
d = 256


# pat  -> pattern
# txt  -> text
# q    -> A prime number

def search(pattern, text, primeNumber):
    lengthOfPattern = len(pattern)
    lengthOfText = len(text)
    i = 0
    j = 0
    patternHash = 0  # hash value for pattern
    textHash = 0  # hash value for txt
    h = 1

    # The value of h would be "pow(d, M-1)%q"
    for i in range(lengthOfPattern - 1):
        h = (h * d) % primeNumber

        # Calculate the hash value of pattern and first window
    # of text
    for i in range(lengthOfPattern):
        patternHash = (d * patternHash + ord(pattern[i])) % primeNumber
        textHash = (d * textHash + ord(text[i])) % primeNumber

        # Slide the pattern over text one by one
    for i in range(lengthOfText - lengthOfPattern + 1):
        # Check the hash values of current window of text and
        # pattern if the hash values match then only check
        # for characters on by one
        if patternHash == textHash:
            # Check for characters one by one
            for j in range(lengthOfPattern):
                if text[i + j] != pattern[j]:
                    break
                else:
                    j += 1

            # if patternHash == textHash and pat[0...M-1] = txt[i, i+1, ...i+M-1]
            if j == lengthOfPattern:
                print("Pattern found at index " + str(i))

                # Calculate hash value for next window of text: Remove
        # leading digit, add trailing digit
        if i < lengthOfText - lengthOfPattern:
            textHash = (d * (textHash - ord(text[i]) * h) + ord(text[i + lengthOfPattern])) % primeNumber

            # We might get negative values of textHash, converting it to
            # positive
            if textHash < 0:
                textHash = textHash + primeNumber

            # Driver Code


txt = "GEEKS FOR GEEKS"
pat = "GEEK"

# A prime number
q = 101

# Function Call
search(pat, txt, q)

# This code is contributed by Bhavya Jain
