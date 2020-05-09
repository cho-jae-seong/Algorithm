#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<algorithm>
#include<vector>
using namespace std;

int main(void) {
	int n,m;
	scanf("%d", &n);
	vector<int>coin(n);
	for (int i = 0; i < n; i++) {
		scanf("%d", &coin[i]);
	}
	scanf("%d", &m);
	vector<int>dp(m + 1, 1000);
	dp[0] = 0;
	for (int i = 0; i < n; i++) {
		for (int j = coin[i]; j <= m; j++) {
			dp[j] = min(dp[j], dp[j - coin[i]] + 1);
		}
	}
	printf("%d\n", dp[m]);
	return 0;
}