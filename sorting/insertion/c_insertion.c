#include <stdio.h>

void insertion_sort(int A[], int a_length);
void print_array(int A[], int a_length);

int main() {
	
	int array[] = {5,2,6,0,1};
	print_array(array, 5);
	insertion_sort(array, 5);
	print_array(array, 5);
	
	

}

void insertion_sort(int A[], int a_length) {
	signed int val;
	for (unsigned int indx = 1; indx < a_length; indx++) {
		val = A[indx];
		int lft_indx = indx - 1;
		
		for (; lft_indx >= 0 && A[lft_indx] > val; lft_indx--)
			A[lft_indx + 1] = A[lft_indx];
		A[lft_indx + 1] = val;
	}
}

void print_array(int A[], int a_length) {
	printf("\n");

	for (int i = 0; i < a_length; i++)
		printf("%d, ",A[i]);
	
	printf("\n");
}
