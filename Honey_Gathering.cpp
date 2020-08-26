#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<memory.h>
#include<algorithm>
using namespace std;
int n, m, c;
int honey[10][10];
int visit[10][10];
int res;

void get_score(int x, int y, int cnt, int sum_h, int sum_c) {
	if (sum_h > c)return;
	res = max(res, sum_c);
	if (cnt == m)return;
	get_score(x, y + 1, cnt + 1, sum_h + honey[x][y], sum_c + pow(honey[x][y], 2));
	get_score(x, y + 1, cnt + 1, sum_h, sum_c);
}

int solve(int x, int y) {
	for (int i = 0; i < m; i++) {
		visit[x][y + i] = 1;
	}
	res = 0;
	get_score(x, y, 0, 0, 0);
	int cost_a = res;
	int cost_b = 0;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n - m + 1; j++) {
			if (!visit[i][j]) {
				res = 0;
				get_score(i, j, 0, 0, 0);
				cost_b = max(cost_b, res);
			}
		}
	}
	return cost_a + cost_b;
}

int main(void) {
	int test_case;
	int T;
	scanf("%d", &T);
	for (test_case = 1; test_case <= T; test_case++) {
		scanf("%d%d%d", &n, &m, &c);
		memset(visit, 0, sizeof(visit));
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				scanf("%d", &honey[i][j]);
			}
		}
		int ans = 0;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n - m + 1; j++) {
				ans = max(ans, solve(i, j));
			}
		}
		printf("#%d %d\n", test_case, ans);
	}
	return 0;
}