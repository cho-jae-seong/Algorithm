#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<algorithm>
using namespace std;

int main(void) {
	int test_case;
	int T, n, cnt = 0,maximum;
	int arr[1001];
	scanf("%d", &T);
	for (test_case = 1; test_case <= T; ++test_case) {
		cnt = 0;
		scanf("%d", &n);
		for (int i = 0; i < n; i++) {
			scanf("%d", &arr[i]);
		}
		for (int i = 2; i < n-2; i++) {
			maximum = -1;
			maximum = max(arr[i + 2], max(arr[i + 1], max(arr[i - 2], arr[i - 1])));
			if (arr[i] > maximum) {
				cnt += (arr[i] - maximum);
			}
		}
		printf("%d\n", cnt);
	}
	return 0;
}