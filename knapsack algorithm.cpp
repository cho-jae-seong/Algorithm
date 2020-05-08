#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
int main(void) {
	int n, m, w, v;
	scanf("%d%d", &n, &m);
	vector<int>dp(m + 1, 0);
	for (int i = 0; i < n; i++) {
		scanf("%d%d", &w, &v);
		for (int j = w; j <= m; j++) {
			dp[j] = max(dp[j], dp[j - w]+v);
		}
	}
	printf("%d\n", dp[m]);
	return 0;
}