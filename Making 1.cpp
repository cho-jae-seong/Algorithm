#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<algorithm>
#include<vector>
using namespace std;

int main(void) {
	int n;
	scanf("%d", &n);
	vector<int>dp(n + 1, 987654321);
	dp[1] = 0;
	for (int i = 2; i <= n; i++) {
		if (i % 3 == 0)dp[i] = min(dp[i], dp[i / 3] + 1);
		if (i % 2 == 0)dp[i] = min(dp[i], dp[i / 2] + 1);
		dp[i] = min(dp[i], dp[i - 1] + 1);
	}
	printf("%d\n", dp[n]);
	return 0;
}