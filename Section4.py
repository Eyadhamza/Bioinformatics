import matplotlib.pyplot as plt


def readFastQ(filename):
    sequences = []
    qualities = []
    with open(filename) as fo:
        while True:
            # notice that in fastaq we have four lines for each read
            # we only care about the sequence and the qualities score

            fo.readline()  # we don't care about it

            seq = fo.readline().rstrip()  # this is the second line ( the sequence

            fo.readline()  # the third line is of no importance to us in the function

            qual = fo.readline().rstrip()  # the qualities score

            if len(seq) == 0:  # means we reached the end of the file
                break
            sequences.append(seq)
            qualities.append(qual)

        return sequences, qualities  # in python it's ok to return multiple value


# now we should call the function
seq, qual = readFastQ('sample.fastq')

# test the values ..
print(seq[:5])
print(qual[:5])


# those quality values doesn't look good ..
# we should make a function to transform it
def phred33ToQ(qual):
    # ord Return the Unicode code point for a one-character string.
    return ord(qual) - 33


# shall we try it to make sure ?
print(phred33ToQ('@'))


# it's time we viualize these stuff

def createHist(qualities):
    hist = [0] * 50
    for qual in qualities:
        for phred in qual:
            q = phred33ToQ(phred)
            hist[q] += 1
    return hist


# we construct a new plot using matplot
# we need to pass the y and x values
# y values are the values of the histogram
# x is just from 0 to length of the histogram

h = createHist(qual)
plt.bar(range(len(h)), h)
plt.show()
