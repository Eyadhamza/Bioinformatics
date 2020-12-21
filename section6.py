#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 16:46:22 2020

"""

# Python3 Program for Bad Character Heuristic
# of Boyer Moore String Matching Algorithm

NO_OF_CHARS = 256


def badCharHeuristic(patt, size):
    '''
    The preprocessing function for
    Boyer Moore's bad character heuristic
    '''

    # Initialize all occurrence as -1
    badChar = [-1] * NO_OF_CHARS

    # Fill the actual value of last occurrence
    for i in range(size):
        # print((string[i]))
        badChar[ord(patt[i])] = i

        # return initialized list
    return badChar


def search(txt, pat):
    '''
    A pattern searching function that uses Bad Character
    Heuristic of Boyer Moore Algorithm
    '''
    n = len(pat)
    m = len(txt)

    badChar = badCharHeuristic(pat, n)

    s = 0
    while s <= m - n:  # we will loop until the latest alignment option
        j = n - 1  # this line means that we are getting the value of the
        # latest element in the pattern, why ?
        # because in bad character rule we want to fine the bad character
        # that doesn't match with the character in the text

        # so we will start from the end then we will see if the char is good
        # we will see the next character
        # until we catch the bad character that caused the mismatch
        while j >= 0 and pat[j] == txt[s + j]: # this checks if its good (it matches)
            j -= 1

        if j < 0: # if you reached here it means that every character passed
            # the previous loop right ?
            # if not? you are not lucky go to the else please
            print("Pattern occur at index = {}".format(s))

            s += (n - badChar[ord(txt[s + n])] if s + n < m else 1)
            print(s)
        else:
            s += max(1, j - badChar[ord(txt[s + j])])
            print(s)


# Driver program to test above function
def main():
    txt = "AACCGACGGAATGTTACGGA"
    pat = "ACGGA"
    search(txt, pat)


if __name__ == '__main__':
    main()

# This code is contributed by Atul Kumar
# (www.facebook.com/atul.kr.007)
