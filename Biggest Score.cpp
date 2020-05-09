#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<algorithm>
#include<vector>
using namespace std;

int main(void) {
	int n, m, score, time;
	scanf("%d%d", &n, &m);
	vector<int>dp(m + 1);
	for (int i = 0; i < n; i++) {
		scanf("%d%d", &score, &time);
		for (int j = m; j >= time; j--) {
			dp[j] = max(dp[j], dp[j - time] + score);
		}
	}
	printf("%d\n",dp[m]);
	return 0;
}