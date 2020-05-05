#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<queue>
#include<vector>
#include<algorithm>
using namespace std;
struct Loc {
	int x;
	int y;
	Loc(int a, int b) {
		x = a;
		y = b;
	}
};
int dx[] = { 0,1 };
int dy[] = { 1,0 };
int map[21][21],dp[21][21];
int main(void) {
	int n;
	queue<Loc>q;
	scanf("%d", &n);
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= n; j++) {
			scanf("%d", &map[i][j]);
			dp[i][j] = 987654321;
		}
	}
	q.push(Loc(1, 1));
	dp[1][1] = map[1][1];
	while (!q.empty()) {
		Loc tmp = q.front();
		q.pop();
		for (int i = 0; i < 2; i++) {
			int nx = tmp.x + dx[i];
			int ny = tmp.y + dy[i];
			if (nx >= 1 && ny >= 1 && nx <= n && ny <= n) {
				if ((dp[tmp.x][tmp.y] + map[nx][ny]) < dp[nx][ny]) {
					q.push(Loc(nx, ny));
					dp[nx][ny] = (dp[tmp.x][tmp.y] + map[nx][ny]);
				}
			}
		}
	}
	printf("%d\n", dp[n][n]);
}