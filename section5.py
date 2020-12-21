# the function takes a pattern and a text
# p is the pattern we are looking for in a sample text

def naive(p, t):
    occurrences = []  # keep track of the indices of each match we had
    # now we will loop for each possible alignment
    # loop to the last position we can compare t and p
    for i in range(len(t) - len(p) + 1):
        # we will initialize a variable with true value and we make it false
        # if we encountered mismatch
        match = True
        for j in range(len(p)):
            if not t[i + j] == p[j]:
                match = False
                break
        if match:
            occurrences.append(i)
    return occurrences


t = 'AGCTTAGTAGC'

p = 'AG'

print(naive(p,t))
