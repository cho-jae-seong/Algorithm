#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<algorithm>
using namespace std;
int map[21][21], dp[21][21];

int dfs(int x, int y) {
	if (dp[x][y] > 0)return dp[x][y];
	if (x == 0 && y == 0)return map[0][0];
	else {
		if (y == 0)return dp[x][y]=dfs(x - 1, y) + map[x][y];
		else if (x == 0)return dp[x][y]=dfs(x, y - 1) + map[x][y];
		else return dp[x][y]=min(dfs(x - 1, y), dfs(x, y - 1)) + map[x][y];
	}
}

int main(void) {
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			scanf("%d", &map[i][j]);
		}
	}
	printf("%d\n", dfs(n - 1, n - 1));
	return 0;
}