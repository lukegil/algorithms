#include <stdio.h>
#include <time.h>

float wrapper(long A[], size_t a_length);
void binary_insertion_sort(long A[], size_t a_length);

int main() {

	long A[] = {2, 3, 1, 11, 18, 12, 9, 22, 11, 2};
	size_t a_length = 10;
	binary_insertion_sort(A, a_length);
	
	for (int i = 0; i < a_length; i++) 
		printf("%lu, ", A[i]);
	printf("\n");
}

float wrapper(long A[], size_t a_length) {
    clock_t start = clock();
    binary_insertion_sort(A, a_length);
    clock_t end = clock();
    float time_spent = (float)(end - start) / CLOCKS_PER_SEC;
    return time_spent;
}


void binary_insertion_sort(long A[], size_t a_length) {
	long val;
	int low, high, mid, insert_at;
	
	for (int i = 1; i < a_length; i++) {
		short found = 0;

		high = i - 1;
		low = 0;
		val = A[i];

		while (!found) {
			mid = (high + low) / 2;

			if ((high - low) <= 1 && A[low] <= val) {
				found = 1;
				insert_at = low + 1;
			} else if (val == A[mid]) {
				found = 1;
				insert_at = mid + 1;
			} else if (val >= A[high]) {
				found = 1;
				insert_at = i;
			} else if (A[low] > val) {
				found = 1;
				insert_at = 0;
			} else if (A[low] < val && val < A[mid]) {
				high = mid;
			} else if (A[mid] < val && val < A[high]) {
				low = mid;
			}
		   
		}	

		int j = i;
		for (; j > insert_at; j--)
			A[j] = A[j - 1];
		A[j] = val;
	}
}
