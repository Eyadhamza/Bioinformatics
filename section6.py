#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 16:46:22 2020

"""

# Python3 Program for Bad Character Heuristic
# of Boyer Moore String Matching Algorithm

NO_OF_CHARS = 256


def badCharHeuristic(patt, size):
    """
    The preprocessing function for
    Boyer Moore's bad character heuristic
    """

    # Initialize all occurrence as -1
    badChar = [-1] * NO_OF_CHARS

    # Fill the actual value of last occurrence
    for i in range(size):
        # print((string[i]))
        badChar[ord(patt[i])] = i

        # return initialized list
    return badChar


def search(txt, pattern):
    """
    A pattern searching function that uses Bad Character
    Heuristic of Boyer Moore Algorithm
    """
    lengthOfPattern = len(pattern)  # length of the pattern
    lengthOfText = len(txt)  # length of the text

    badChar = badCharHeuristic(pattern, lengthOfPattern)  # we construct the bad character table

    indexOfText = 0
    while indexOfText <= lengthOfText - lengthOfPattern:  # we will loop until the latest alignment option
        indexOfPattern = lengthOfPattern - 1  # this line means that we are getting the value of the
        # latest element in the pattern, why ?
        # because in bad character rule we want to fine the bad character
        # that doesn't match with the character in the text

        # so we will start from the end then we will see if the char is good
        # we will see the next character
        # until we catch the bad character that caused the mismatch
        while indexOfPattern >= 0 and pattern[indexOfPattern] == txt[indexOfText + indexOfPattern]:  # this checks if its good (it matches)
            indexOfPattern -= 1

        if indexOfPattern < 0:  # if you reached here it means that every character passed
            # the previous loop right ?
            # if not? you are not lucky go to the else please
            print("Pattern occur at index = {}".format(indexOfText))

            # congrats !!!
            # now we found an occurrence find the next one now ..
            # using the bad character table constructed with the badCharHeuristic
            # method we can calculate how many shifts we will make
            indexOfText += (lengthOfPattern - badChar[ord(txt[indexOfText + lengthOfPattern])] if indexOfText + lengthOfPattern < lengthOfText else 1)
            print(indexOfText)
        else:  # you know why you are here ?
            # you are a bad character :((
            # we need to shift you so we can start over aren't we ?
            # notice that indexOfPattern is the index of the pattern
            # indexOfText is the index of the text
            # using the bad character table constructed with the badCharHeuristic
            # method we can calculate how many shifts we will make
            indexOfText += max(1, indexOfPattern - badChar[ord(txt[indexOfText + indexOfPattern])])
            print(indexOfText)


# Driver program to test above function
def main():
    txt = "AACCGACGGAATGTTACGGA"
    pat = "ACGGA"
    search(txt, pat)


if __name__ == '__main__':
    main()

# This code is contributed by Atul Kumar
# (www.facebook.com/atul.kr.007)
