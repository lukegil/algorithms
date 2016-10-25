#!/usr/bin/python
import time

def wrapper(A, a_length):
    start = time.clock()
    binary_insertion(A)
    end = time.clock()

    return end - start


def binary_insertion(A):

    for indx in range(1, len(A)):

        high = indx - 1
        low = 0
        found = False

        while (not found):
            val = A[indx]
            mid = (high + low) / 2

            if (val < A[low]):
                found = True
                insert_at = 0

            elif (val <= A[low]):
                found = True
                insert_at = low

            elif (high - low <= 1 and A[low] < val <= A[high]):
                found = True
                insert_at = low + 1

            elif (A[low] < val < A[mid]):
                found = False
                high = mid

            elif (A[mid] == val):
                found = True
                insert_at = mid

            elif (A[mid] < val < A[high]):
                found = False
                low = mid

            elif (A[high] <= val):
                found = True
                insert_at = indx


        A = A[:insert_at] + [val] + A[insert_at:indx] + A[indx+1:]

    return A
