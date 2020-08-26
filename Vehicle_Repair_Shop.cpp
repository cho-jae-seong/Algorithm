#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<vector>
#include<queue>
#include<functional>
#include<algorithm>
using namespace std;

int n, m, k, a, b;

int main(void) {
	int test_case;
	int T;
	scanf("%d", &T);
	for (test_case = 1; test_case <= T; test_case++) {
		vector<int>ans;
		scanf("%d%d%d%d%d", &n, &m, &k, &a, &b);
		int rc[21] = { 0 };
		int ma[21] = { 0 };
		int pt[1001] = { 0 };
		for (int i = 1; i <= n; i++) {
			scanf("%d", &rc[i]);
		}
		for (int i = 1; i <= m; i++) {
			scanf("%d", &ma[i]);
		}
		for (int i = 1; i <= k; i++) {
			scanf("%d", &pt[i]);
		}
		priority_queue<int, vector<int>, greater<int>> q1;
		queue<pair<int, int>>q2;
		vector<pair<int, int>> v1(21, { 0,0 });
		vector<pair<int, int>> v2(21, { 0,0 });
		int t = 0;
		int finish = 0;
		while (finish < k) {
			for (int i = 1; i <= k; i++) {
				if (pt[i] <= t) {
					q1.push(i);
					pt[i] = 10000;
				}
			}
			for (int i = 1; i <= n; i++) {
				if (v1[i].first == 0) {
					if (!q1.empty()) {
						v1[i].first = q1.top();
						v1[i].second = rc[i];
						q1.pop();
					}
				}
				else {
					v1[i].second--;
					if (v1[i].second == 0) {
						q2.push({ v1[i].first,i });
						v1[i].first = 0;
						if (!q1.empty()) {
							v1[i].first = q1.top();
							v1[i].second = rc[i];
							q1.pop();
						}
					}
				}
			}
			for (int i = 1; i <= m; i++) {
				if (v2[i].first == 0) {
					if (!q2.empty()) {
						v2[i].first = q2.front().first;
						v2[i].second = ma[i];
						if (a == q2.front().second && b == i) {
							ans.push_back(q2.front().first);
						}
						q2.pop();
					}
				}
				else {
					v2[i].second--;
					if (v2[i].second == 0) {
						finish++;
						v2[i].first = 0;
						if (!q2.empty()) {
							v2[i].first = q2.front().first;
							v2[i].second = ma[i];
							if (a == q2.front().second && b == i) {
								ans.push_back(q2.front().first);
							}
							q2.pop();
						}
					}
				}
			}
			t++;
		}
		int sum = 0;
		if (ans.size() == 0)
			sum -= 1;
		for (int i = 0; i < ans.size(); i++) {
			sum += ans[i];
		}
		printf("#%d %d\n", test_case, sum);
	}
	return 0;
}