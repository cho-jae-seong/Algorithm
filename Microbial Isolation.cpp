#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<algorithm>
#include<vector>
#include<memory.h>
using namespace std;

int n, m, k,ans;
int map[100][100];
int dx[] = { 0,-1,1,0,0 };
int dy[] = { 0,0,0,-1,1 };

struct state {
	int sero, garo, m_num, dir, sum;
	state(int a, int b, int c, int d, int e) {
		sero = a;
		garo = b;
		m_num = c;
		dir = d;
		sum = e;
	}
};

vector<state>st;

int main(void) {
	int test_case;
	int T;
	int s, g, nn, d;
	scanf("%d", &T);
	for (test_case = 1; test_case <= T; test_case++) {
		ans = 0;
		st.clear();
		scanf("%d%d%d", &n, &m, &k);
		for (int i = 0; i < k; i++) {
			scanf("%d%d%d%d", &s, &g, &nn, &d);
			st.push_back(state(s, g, nn, d, nn));
		}
		int time = 0;
		while (time++ < m) {
			int x, y, cnt, dir;
			memset(map, -1, sizeof(map));
			for (int i = 0; i < k; i++) {
				if (st[i].m_num == 0)continue;
				x = st[i].sero;
				y = st[i].garo;
				cnt = st[i].m_num;
				dir = st[i].dir;
				x += dx[dir];
				y += dy[dir];
				st[i].sero = x;
				st[i].garo = y;
				if (x == 0 || y == 0 || x == n - 1 || y == n - 1) {
					st[i].m_num /= 2;
					st[i].sum /= 2;
					if (dir == 1 || dir == 3) {
						st[i].dir += 1;
					}
					else {
						st[i].dir -= 1;
					}
				}
				else {
					if (map[x][y] == -1) {
						map[x][y] = i;
					}
					else {
						if (cnt < st[map[x][y]].m_num) {
							st[map[x][y]].sum += st[i].sum;
							st[i].m_num = 0;
							st[i].sum = 0;
						}
						else {
							st[i].sum += st[map[x][y]].sum;
							st[map[x][y]].m_num = 0;
							st[map[x][y]].sum = 0;
							map[x][y] = i;
						}
					}
				}
			}
			for (int i = 0; i < k; i++) {
				st[i].m_num = st[i].sum;
			}
		}
		for (int i = 0; i < k; i++) {
			ans += st[i].m_num;
		}
		printf("#%d %d\n", test_case, ans);
	}
	return 0;
}