#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
int dp[11];
int main(void) {
	int n;
	int a;
	dp[1] = 1; dp[2] = 2; dp[3] = 4;
	for (int i = 4; i <= 10; i++) {
		dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]);
	}
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d", &a);
		printf("%d\n", dp[a]);
	}
	return 0;
}