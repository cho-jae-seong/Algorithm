#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<algorithm>
#include<queue>
#include<memory.h>
using namespace std;

struct Loc {
	int x, y;
	Loc(int a, int b) {
		x = a;
		y = b;
	}
};

int n, m, r, c, l, cnt = 0;
int map[51][51];
int dx[] = { 0, 0, 1, -1 };
int dy[] = { 1, -1, 0, 0 };
int visit[51][51];
queue<Loc>q;

int main(void) {
	int test_case;
	scanf("%d", &test_case);
	for (int i = 1; i <= test_case; i++) {
		cnt = 0;
		memset(visit, 0, sizeof(visit));
		q = queue<Loc>();
		scanf("%d%d%d%d%d", &n, &m, &r, &c, &l);
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				scanf("%d", &map[i][j]);
			}
		}
		visit[r][c] = 1;
		q.push(Loc(c, r));
		int time = 0;
		while (true) {
			time++;
			if (time == l)break;
			int size = q.size();
			for (int x = 0; x < size; x++) {
				Loc tmp = q.front();
				q.pop();
				int curpipe = map[tmp.y][tmp.x];
				for (int k = 0; k < 4; k++) {
					if (curpipe == 2 && (k == 2 || k == 3))continue;
					else if (curpipe == 3 && (k == 0 || k == 1))continue;
					else if (curpipe == 4 && (k == 0 || k == 3))continue;
					else if (curpipe == 5 && (k == 1 || k == 3))continue;
					else if (curpipe == 6 && (k == 1 || k == 2))continue;
					else if (curpipe == 7 && (k == 0 || k == 2))continue;

					int nx = tmp.x + dx[k];;
					int ny = tmp.y + dy[k];

					if (nx >= 0 && ny >= 0 && nx < m && ny < n) {
						int npipe = map[ny][nx];
						if (npipe != 0 && !visit[ny][nx]) {
							if (k == 0) {
								if (npipe == 1 || npipe == 2 || npipe == 4 || npipe == 7) {
									visit[ny][nx] = 1;
									q.push(Loc(nx, ny));
								}
							}
							else if (k == 1) {
								if (npipe == 1 || npipe == 2 || npipe == 5 || npipe == 6) {
									visit[ny][nx] = 1;
									q.push(Loc(nx, ny));
								}
							}
							else if (k == 2) {
								if (npipe == 1 || npipe == 3 || npipe == 6 || npipe == 7) {
									visit[ny][nx] = 1;
									q.push(Loc(nx, ny));
								}
							}
							else if (k == 3) {
								if (npipe == 1 || npipe == 3 || npipe == 4 || npipe == 5) {
									visit[ny][nx] = 1;
									q.push(Loc(nx, ny));
								}
							}
						}
					}
				}
			}
		}
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (visit[i][j] == 1) {
					cnt++;
				}
			}
		}
		printf("#%d %d\n", i, cnt);
	}
	return 0;
}