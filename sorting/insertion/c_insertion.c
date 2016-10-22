#include <stdio.h>
#include <time.h>

float wrapper(long A[], size_t a_length);
void insertion_sort(long A[], size_t a_length);

int main() {}

float wrapper(long A[], size_t a_length) {
    clock_t start = clock();
    insertion_sort(A, a_length);
    clock_t end = clock();
    float time_spent = (float)(end - start) / CLOCKS_PER_SEC;
    return time_spent;
}

void insertion_sort(long A[], size_t a_length) {
	signed int val;
	for (unsigned int indx = 1; indx < a_length; indx++) {
		val = A[indx];
		int lft_indx = indx - 1;

		for (; lft_indx >= 0 && A[lft_indx] > val; lft_indx--)
			A[lft_indx + 1] = A[lft_indx];
		A[lft_indx + 1] = val;
	}
}
