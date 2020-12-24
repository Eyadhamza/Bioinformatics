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
    secondSequenceLength = len(secondSequence)

    # using numpy we initialize a matrix of size firstSequenceLength+1 * secondSequenceLength +1
    # all zeros at start then we fill it one by one according to the values of the
    # two sequences
    # remember how we put the first row as -1 ,-2 ...  and the columns as -1,-2 ..?
    # remember we had zero cell at first ?
    # that's why we put the + 1
    scoresMatrix = np.zeros((firstSequenceLength + 1, secondSequenceLength + 1), dtype=int)
    for i in range(0, firstSequenceLength + 1):
        scoresMatrix[i][0] = gap * i
    for j in range(0, secondSequenceLength + 1):
        scoresMatrix[0][j] = gap * j
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
            # we calculate three values and then we choose the maximum among them

            # the value of the diagonal + the match score value of the two characters
            diagonal = scoresMatrix[i - 1][j - 1] + match_score(firstSequence[i - 1], secondSequence[j - 1])
            # the up value + the gap value
            up = scoresMatrix[i - 1][j] + gap
            # the left value + the gap value
            left = scoresMatrix[i][j - 1] + gap
            # now getting the maximum
            scoresMatrix[i][j] = max(diagonal, up, left)
    # the nested for loop is finished

    align1, align2 = '', ''
    i, j = firstSequenceLength, secondSequenceLength
    while i > 0 or j > 0:  # as long as we don't reach zero
        # (يعني احنا لو وصلنا للصفر معناها ان التتابع خلص)

        # لاحظ هنا اني بحط قيم المصفوفة جوا متغيرات عشان اعرف اتعامل معاها بشكل سهل شوية
        # ولاحظ معايا الاهم ان ديه اخر قيمة ..
        # احنا حاليا بنعمل ال trace
        score_current = scoresMatrix[i][j]
        score_diagonal = scoresMatrix[i - 1][j - 1]
        score_left = scoresMatrix[i][j - 1]
        score_up = scoresMatrix[i - 1][j]
        # عشان اعرف ال trace لازم اعرف كل قيمة جاية منين من فوق ولا من ال diagonal  ولا من الشمال
        # so we create if and elif statement to figure this out

        # يعني لو ده طلع جاي من ال diagonal
        if score_current == score_diagonal + match_score(firstSequence[i - 1], secondSequence[j - 1]):

            a1 = firstSequence[i - 1]  # we put the value of the latest character in the first sequence
            a2 = secondSequence[j - 1]  # we put the value of the latest character in the second sequence

            i -= 1  # so we can process the next character
            j -= 1  # so we can process the next character

        elif score_current == score_up + gap:
            a1 = firstSequence[i - 1]
            a2 = "-"
            i -= 1  # so we can process the next character
            # why only i ?
            # because we processed the character in the first sequence only !!
        elif score_current == score_left + gap:
            a1 = "-"
            a2 = secondSequence[j - 1]
            j -= 1
            # why only j ?
            # because we processed the character in the second sequence only !!
        # عايزين نجمع الحروف بقي في سترينج علي بعضه
        align1 += a1
        align2 += a2
    align1 = align1[::-1]  # عشان نعرض من الاخر
    align2 = align2[::-1]  # عشان نعرض من الاخر

    print(scoresMatrix)
    print("scoresMatrix= " + str(scoresMatrix[firstSequenceLength, secondSequenceLength]))
    print(align1)
    print(align2)


# define the two sequences
seq1 = "GATTACA"
seq2 = "GCATGCT"
# call the method
needle(seq1, seq2)
