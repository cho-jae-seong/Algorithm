#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<algorithm>
#include<memory.h>
using namespace std;
int n, k;
int ans;
int arr[8][8];
int visit[8][8];
int dx[] = {-1,0,1,0};
int dy[] = {0,1,0,-1};

void dfs(int x, int y, int cnt, int cut) {
	ans = max(ans, cnt);
	for (int i = 0; i < 4; i++) {
		int nx = x + dx[i];
		int ny = y + dy[i];
		if (nx >= 0 && ny >= 0 && nx < n && ny < n && visit[nx][ny] == 0) {
			if (arr[x][y] <= arr[nx][ny]) {
				if (cut == 0) {
					for (int d = 1; d <= k; d++) {
						int tmp = arr[nx][ny];
						int land = arr[nx][ny] - d;
						if (arr[x][y] > land) {
							visit[nx][ny] = 1;
							arr[nx][ny] = land;
							dfs(nx, ny, cnt + 1, cut + 1);
							arr[nx][ny] = tmp;
							visit[nx][ny] = 0;
						}
					}
				}
			}
			else {
				visit[nx][ny] = 1;
				dfs(nx, ny, cnt + 1, cut);
				visit[nx][ny] = 1;
			}
		}
	}
}

int main(void) {
	int test_case;
	scanf("%d", &test_case);
	for (int i = 1; i <= test_case; i++) {
		int high = 0;
		scanf("%d%d", &n, &k);
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				scanf("%d", &arr[i][j]);
				high = max(high, arr[i][j]);
			}
		}
		memset(visit, 0, sizeof(visit));
		ans = 0;
		for (int k = 0; k < n; k++) {
			for (int l = 0; l < n; l++) {
				if (arr[k][l] == high && visit[k][l] == 0) {
					visit[k][l] = 1;
					dfs(k, l, 1, 0);
					visit[k][l] = 0;
				}
			}
		}
		printf("#%d %d\n", i, ans);
	}
}