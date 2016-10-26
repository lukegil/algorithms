#include <stdio.h>
#include <time.h>

float wrapper(long A[], size_t a_length);
void shellsort(long A[], size_t a_length);

int main() {

	long A[] = {2, 3, 1, 11, 18, 12, 9, 22, 11, 2};
	size_t a_length = 10;
	shellsort(A, a_length);

	for (int i = 0; i < a_length; i++)
		printf("%lu, ", A[i]);
	printf("\n");
}

float wrapper(long A[], size_t a_length) {
    clock_t start = clock();
    shellsort(A, a_length);
    clock_t end = clock();
    float time_spent = (float)(end - start) / CLOCKS_PER_SEC;
    return time_spent;
}

void shellsort(long A[], size_t a_length) {
	int gap, gi, i;
	long top_el;

	/* For every gap interval */
	for (gap = a_length/2; gap > 0; gap/=2) {
		
		/* for ever group */
		for (gi = gap; gi < a_length; gi++) {
			
			/* sink the top element */
			top_el = A[gi];
			for (i = gi; i >= gap && top_el < A[i - gap]; i -= gap)
				A[i] = A[i - gap];
			
			A[i] = top_el;			

		}
	}
}
