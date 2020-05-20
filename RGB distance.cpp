#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<algorithm>
using namespace std;
int rgb[1001][3];
int dp[1001][3];
int main(void) {
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < 3; j++) {
			scanf("%d", &rgb[i][j]);
		}
	}
	dp[0][0] = rgb[0][0]; dp[0][1] = rgb[0][1]; dp[0][2] = rgb[0][2];
	for (int i = 1; i < n; i++) {
		dp[i][0] = min(dp[i - 1][1] + rgb[i][0], dp[i - 1][2] + rgb[i][0]);
		dp[i][1] = min(dp[i - 1][0] + rgb[i][1], dp[i - 1][2] + rgb[i][1]);
		dp[i][2] = min(dp[i - 1][1] + rgb[i][2], dp[i - 1][0] + rgb[i][2]);
	}
	printf("%d\n", min(dp[n - 1][2], min(dp[n - 1][0], dp[n - 1][1])));
	return 0;
}