#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<algorithm>
using namespace std;

int map[21][21], dp[21][21];
int main(void) {
	int n,cnt=0;
	scanf("%d", &n);
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= n; j++) {
			scanf("%d", &map[i][j]);
		}
	}
	dp[1][1] = map[1][1];
	for (int i = 1; i <= n; i++) {
		dp[1][i] = dp[1][i - 1] + map[1][i];
		dp[i][1] = dp[i - 1][1] + map[i][1];
	}
	for (int i = 2; i <= n; i++) {
		for (int j = 2; j <= n; j++) {
			dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + map[i][j];
		}
	}
	printf("%d\n", dp[n][n]);
	return 0;
}