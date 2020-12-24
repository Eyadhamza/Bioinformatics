import numpy as np

# here we are setting the values for the match score matrix
match = 1
mismatch = -1
gap = -1


def match_score(char1, char2):
    # here we are implementing the match score matrix so we
    # can compare every two characters
    if char1 == char2:
        return match
    elif char1 == "-" or char2 == "-":  # if any of the two characters are - return gap
        return gap
    else:
        return mismatch


def needle(firstSequence, secondSequence):
    # we set each sequence length
    firstSequenceLength = len(firstSequence)
    secondSequenceLength= len(secondSequence)

    # using numpy we initialize a matrix of size firstSequenceLength+1 * secondSequenceLength +1
    # all zeros at start then we fill it one by one according to the values of the
    # two sequences
    # remember how we put the first row as -1 ,-2 ...  and the columns as -1,-2 ..?
    # remember we had zero cell at first ?
    # that's why we put the + 1
    scores = np.zeros((firstSequenceLength + 1, secondSequenceLength + 1), dtype=int)
    for i in range(0, firstSequenceLength + 1):
        scores[i][0] = gap * i
    for j in range(0, secondSequenceLength + 1):
        scores[0][j] = gap * j
    # we would have this matrix (المثال الي في المحاضرة )
    # 0 | -1 | -2 | -3 | -4 | -5 | -6 | -7
    # -1
    # -2
    # -3
    # -4
    # -5
    # -6
    # -7
    # now we must calculate the rest of the values
    # we loop over each element in a nested loop
    # we loop from 1 because we know that the first cell is 0
    # we loop until the latest index which is the length + 1
    for i in range(1, firstSequenceLength + 1):
        for j in range(1, secondSequenceLength + 1):

            diagonal = scores[i - 1][j - 1] + match_score(firstSequence[i - 1], secondSequence[j - 1])
            up = scores[i - 1][j] + gap
            left = scores[i][j - 1] + gap
            scores[i][j] = max(diagonal, up, left)

    align1, align2 = '', ''
    i, j = firstSequenceLength, secondSequenceLength
    while i > 0 or j > 0:
        score_current = scores[i][j]
        score_diagonal = scores[i - 1][j - 1]
        score_left = scores[i][j - 1]
        score_up = scores[i - 1][j]

        if score_current == score_diagonal + match_score(firstSequence[i - 1], secondSequence[j - 1]):
            a1, a2 = firstSequence[i - 1], secondSequence[j - 1]
            i, j = i - 1, j - 1
        elif score_current == score_up + gap:
            a1, a2 = firstSequence[i - 1], "-"
            i -= 1
        elif score_current == score_left + gap:
            a1, a2 = "-", secondSequence[j - 1]
            j -= 1

        align1 += a1
        align2 += a2
    align1 = align1[::-1]
    align2 = align2[::-1]

    print(scores)
    print("scores= " + str(scores[firstSequenceLength, secondSequenceLength]))
    print(align1)
    print(align2)


seq1 = "GATTACA"
seq2 = "GCATGCT"
needle(seq1, seq2)
