#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<vector>
#include<queue>
#include<algorithm>
using namespace std;
int n;
int map[10][10];
int s[10];
int ans;
int sizee;
vector<pair<int, int >> p;
vector<pair<int, int >> st;

int solve() {
	int time = 0;
	int ch = 0;
	queue<int>c[2];
	int d[10];
	for (int i = 0; i < sizee; i++) {
		d[i] = abs(p[i].first - st[s[i]].first) + abs(p[i].second - st[s[i]].second);
	}
	while (1) {
		if (time >= ans)return time;
		if (ch == sizee)return time;
		for (int i = 0; i < 2; i++) {
			int sp = c[i].size();
			for (int j = 0; j < sp; j++) {
				int top = c[i].front();
				c[i].pop();
				top--;
				if (top != 0) {
					c[i].push(top);
				}
				else {
					ch++;
				}
			}
		}
		for (int i = 0; i < sizee; i++) {
			if (time == d[i]) {
				if (c[s[i]].size() < 3) {
					c[s[i]].push(map[st[s[i]].first][st[s[i]].second]);
				}
				else {
					c[s[i]].push(map[st[s[i]].first][st[s[i]].second] + c[s[i]].front());
				}
			}
		}
		time++;
	}
}

void dfs(int cnt) {
	if (cnt == p.size()) {
		int tmp = solve();
		if (ans > tmp)ans = tmp;
		return;
	}
	s[cnt] = 0;
	dfs(cnt + 1);
	s[cnt] = 1;
	dfs(cnt + 1);
}

int main(void) {
	int test_case;
	scanf("%d", &test_case);
	for (int i = 1; i <= test_case; i++) {
		scanf("%d", &n);
		p.clear();
		st.clear();
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				scanf("%d", &map[i][j]);
				if (map[i][j] == 1)p.push_back({ i,j });
				else if (map[i][j] > 1)st.push_back({ i,j });
			}
		}
		sizee = p.size();
		ans = 2147000000;
		dfs(0);
		printf("#%d %d\n", i, ans);
	}
	return 0;
}