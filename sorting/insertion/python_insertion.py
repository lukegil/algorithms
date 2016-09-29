#!/usr/bin/python
import time

def wrapper(A, a_length):
    start = time.clock()
    insertion_sort(A)
    end = time.clock()

    return end - start

def insertion_sort(A):

    for indx in range(1, len(A)):
        val = A[indx]
        lft_indx = indx - 1

        while lft_indx >= 0 and A[lft_indx] > val:
            A[lft_indx + 1] = A[lft_indx]
            lft_indx -= 1
        A[lft_indx + 1] = val

    return A

if __name__ == '__main__':
    ''' quick test '''
    A = [1,4,2,7,4,45,23]
    print insertion_sort(A)
