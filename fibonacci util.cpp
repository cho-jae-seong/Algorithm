#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>

int main(void) {
	int t;
	int a;
	int dp0[41], dp1[41];
	scanf("%d", &t);
	dp0[0] = 1; dp1[0] = 0; dp0[1] = 0; dp1[1] = 1; dp0[2] = 1; dp1[2] = 1;
	for (int i = 3; i < 41; i++) {
		dp0[i] = dp1[i - 1];
		dp1[i] = (dp1[i - 1] + dp1[i - 2]);
	}
	for (int i = 0; i < t; i++) {
		scanf("%d", &a);
		printf("%d %d\n", dp0[a], dp1[a]);
	}
	return 0;
}