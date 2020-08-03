#include<stdio.h>
#include<math.h>
#include<algorithm>
using namespace std;

int n, m, ans;
int map[21][21];

int getMax(int r, int c, int k) {
	int house = 0;
	for (int i = r - k + 1; i <= r + k - 1; i++) {
		for (int j = c - k + 1; j <= c + k - 1; j++) {
			if (i < 0 || j<0 || i >= n || j >= n)continue;
			int distance = abs(r - i) + abs(c - j);
			if (distance <= k - 1 && map[i][j] == 1)house++;
		}
	}
	int cost = house * m - ((k * k) + (k - 1) * (k - 1));
	if (cost >= 0)return house;
	else return -1;
}

void solve(int k) {
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			ans = max(ans,getMax(i, j, k));
		}
	}
}

int main(void) {
	int test_case;
	int T;
	scanf("%d", &T);
	for (test_case = 1; test_case <= T; ++test_case) {
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				scanf("%d", &map[i][j]);
			}
		}
		ans = 0;
		for (int k = 1; k <= n + 2; k++) {
			solve(k);
		}
		printf("#%d %d\n", test_case, ans);
	}
	return 0;
}