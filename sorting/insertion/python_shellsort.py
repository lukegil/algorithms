#!/usr/bin/python
import time

def wrapper(A, a_length):
    start = time.clock()
    shellsort(A)
    end = time.clock()

    return end - start


def shellsort(A):
    gap = len(A)
    # For n/2, n/4 ... n/n
    while (gap > 0):
        gap /= 2

        # for N/gap'th element through Nth element
        for gi in range(gap, len(A)):
            lower_i = gi
            top_el = A[lower_i] # Item to sink

            # Until we get to the bottom-most slot, if the top el is
            # smaller than the one `gap` spaces below, swap them
            while (lower_i >= gap and top_el < A[lower_i - gap]):
                lower_i -= gap
                A[lower_i + gap] = A[lower_i]

            # set the sinking el in the last place
            # we moved an element out of
            A[lower_i] = top_el

    return A
