#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
	if (argc < 3) {
		printf("Two arguments required: length of list and filename\n");
		exit(0);
	}

	int len = atoi(argv[1]);
	int numbers[len];
	FILE *fp;
	fp = fopen(argv[2], "r");

}

