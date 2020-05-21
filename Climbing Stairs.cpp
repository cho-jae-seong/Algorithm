#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<algorithm>
using namespace std;
int st[301];
int dp[301][3];
int main(void) {
	int n;
	scanf("%d", &n);
	for (int i = 1; i <= n; i++) {
		scanf("%d", &st[i]);
	}
	dp[1][1] = st[1];
	for (int i = 2; i <= n; i++) {
		dp[i][2] = dp[i - 1][1] + st[i];
		dp[i][1] = max(dp[i - 2][1], dp[i - 2][2]) + st[i];
	}
	printf("%d\n", max(dp[n][1], dp[n][2]));
	return 0;
}