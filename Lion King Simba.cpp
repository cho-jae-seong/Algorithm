#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<algorithm>
#include<vector>
#include<queue>
using namespace std;
int map[21][21], ch[21][21];
int dx[] = { -1,0,1,0 };
int dy[] = { 0,1,0,-1 };
struct state {
	int x, y, dis;
	state(int a, int b, int c) {
		x = a;
		y = b;
		dis = c;
	}
	bool operator<(const state& bb)const {
		if (dis == bb.dis) {
			if (x == bb.x)return y > bb.y;
			else return x > bb.x;
		}
		else return dis > bb.dis;
	}
};

struct Lion {
	int x, y, s, ate;
	void sizeup() {
		ate = 0;
		s++;
	}
};

int main(void) {
	int n, i, j, res = 0;
	priority_queue<state>q;
	Lion simba;
	scanf("%d", &n);
	for (i = 1; i <= n; i++) {
		for (j = 1; j <= n; j++) {
			scanf("%d", &map[i][j]);
			if (map[i][j] == 9) {
				simba.x = i;
				simba.y = j;
				map[i][j] = 0;
			}
		}
	}
	q.push(state(simba.x, simba.y, 0));
	simba.s = 2;
	simba.ate = 0;
	while (!q.empty()) {
		state tmp = q.top();
		q.pop();
		int x = tmp.x;
		int y = tmp.y;
		int z = tmp.dis;
		if (map[x][y] != 0 && map[x][y] < simba.s) {
			simba.x = x;
			simba.y = y;
			simba.ate++;
			if (simba.ate >= simba.s)simba.sizeup();
			map[x][y] = 0;
			for (i = 1; i <= n; i++) {
				for (j = 1; j <= n; j++) {
					ch[i][j] = 0;
				}
			}
			while (!q.empty())q.pop();
			res = tmp.dis;
		}
		for (i = 0; i < 4; i++) {
			int xx = x + dx[i];
			int yy = y + dy[i];
			if (xx<1 || xx>n || yy<1 || y>n || map[xx][yy] > simba.s || ch[xx][yy] > 0)continue;
			q.push(state(xx, yy, z + 1));
			ch[xx][yy] = 1;
		}
	}
	printf("%d\n", res);
	return 0;
}