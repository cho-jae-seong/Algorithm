#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<algorithm>
#include<vector>
#include<queue>
using namespace std;

int main(void) {
	int n, m, a, b, score;
	scanf("%d%d", &n, &m);
	vector<vector<int>>graph(n + 1, vector<int>(n + 1, 0));
	vector<int>degree(n + 1);
	queue<int>q;
	for (int i = 0; i < m; i++) {
		scanf("%d%d", &a, &b);
		graph[a][b] = 1;
		degree[b]++;
	}
	for (int i = 1; i <= n; i++) {
		if (degree[i] == 0)q.push(i);
	}
	while (!q.empty()) {
		int now = q.front();
		q.pop();
		printf("%d ", now);
		for (int i = 1; i <= n; i++) {
			if (graph[now][i] == 1) {
				degree[i] --;
				if (degree[i] == 0)q.push(i);
			}
		}
	}
	return 0;
}