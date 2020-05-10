#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<algorithm>
#include<vector>
using namespace std;

int main(void) {
	int n, a, b, score;
	scanf("%d", &n);
	vector<vector<int>>dis(n + 1, vector<int>(n + 1, 100));
	vector<int>res(n + 1);
	for (int i = 1; i <= n; i++) dis[i][i] = 0;
	while (true) {
		scanf("%d%d", &a, &b);
		if (a == -1 && b == -1)break;
		dis[a][b] = 1;
		dis[b][a] = 1;
	}
	for (int k = 1; k <= n; k++) {
		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= n; j++) {
				dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j]);
			}
		}
	}
	score = 100;
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= n; j++) {
			res[i] = max(res[i], dis[i][j]);
		}
		score = min(score, res[i]);
	}
	int cnt = 0;
	for (int i = 1; i <= n; i++) {
		if (res[i] == score)cnt++;
	}
	printf("%d %d\n", score, cnt);
	for (int i = 1; i <= n; i++) {
		if (res[i] == score)printf("%d ", i);
	}
	return 0;
}