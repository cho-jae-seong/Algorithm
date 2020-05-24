#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<algorithm>
using namespace std;

int main(void) {
	int test_case;
	int dump, maximum = -1, minimum = 101, check1, check2, result;
	int box[101];
	for (test_case = 1; test_case <= 10; test_case++) {
		scanf("%d", &dump);
		for (int i = 1; i <= 100; i++) {
			scanf("%d", &box[i]);
		}
		for (int i = 1; i <= dump; i++) {
			maximum = -1; minimum = 101;
			for (int j = 1; j <= 100; j++) {
				if (maximum < box[j]) {
					maximum = box[j];
					check1 = j;
				}
				if (minimum > box[j]) {
					minimum = box[j];
					check2 = j;
				}
			}
			if (maximum - minimum == 0 || maximum - minimum == 1) {
				result = maximum - minimum;
				break;
			}
			else {
				box[check1] -= 1;
				box[check2] += 1;
				maximum = -1; minimum = 101;
				for (int k = 1; k <= 100; k++) {
					maximum = max(maximum, box[k]);
					minimum = min(minimum, box[k]);
					result = maximum - minimum;
				}
			}
		}
		printf("#%d %d\n", test_case, result);
	}
	return 0;
}