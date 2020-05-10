#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<algorithm>
#include<vector>
using namespace std;

int main(void) {
	int n, m, a, b, c;
	scanf("%d%d", &n, &m);
	vector<vector<int>>dis(n + 1, vector<int>(n + 1, 5000));
	for (int i = 1; i <= n; i++)dis[i][i] = 0;
	for (int i = 1; i <= m; i++) {
		scanf("%d%d%d", &a, &b, &c);
		dis[a][b] = c;
	}
	for (int k = 1; k <= n; k++) {
		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= n; j++) {
				dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j]);
			}
		}
	}
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= n; j++) {
			if (dis[i][j] == 5000) {
				printf("M ");
			}
			else {
				printf("%d ", dis[i][j]);
			}
		}
		printf("\n");
	}
	return 0;
}