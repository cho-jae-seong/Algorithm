#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<memory.h>
#include<vector>
using namespace std;
int dx[] = { -1,1,0,0 };
int dy[] = { 0,0,-1,1 };
int n;
int map[101][101];
int res = 0;
vector<pair<int, int>> start;
vector<pair<int, int>> hole[5];
int start_x, start_y;

int checkDir(int x, int y, int block, int dir) {
	if (block == 1) {
		if (dir == 0)return 1;
		if (dir == 1)return 3;
		if (dir == 2)return 0;
		if (dir == 3)return 2;
	}
	else if (block == 2) {
		if (dir == 0)return 3;
		if (dir == 1)return 0;
		if (dir == 2)return 1;
		if (dir == 3)return 2;
	}
	else if (block == 3) {
		if (dir == 0)return 2;
		if (dir == 1)return 0;
		if (dir == 2)return 3;
		if (dir == 3)return 1;
	}
	else if (block == 4) {
		if (dir == 0)return 1;
		if (dir == 1)return 2;
		if (dir == 2)return 3;
		if (dir == 3)return 0;
	}
	else if (block == 5) {
		if (dir == 0)return 1;
		if (dir == 1)return 0;
		if (dir == 2)return 3;
		if (dir == 3)return 2;
	}
	return dir;
}

void dfs(int x,int y,int dir,int score) {
	int nx = x + dx[dir];
	int ny = y + dy[dir];
	if (nx < 0 || ny < 0 || nx >= n || ny >= n) {
		int s = (score * 2) + 1;
		if (res < s)res = s;
		return;
	}
	else if (nx == start_x && ny == start_y) {
		if (res < score)res = score;
		return;
	}
	else if (map[nx][ny] == 0) {
		dfs(nx, ny, dir, score);
	}
	else if (map[nx][ny] > 0 && map[nx][ny] < 6) {
		dir = checkDir(nx, ny, map[nx][ny], dir);
		dfs(nx, ny, dir, score + 1);
	}
	else if (map[nx][ny] > 5 && map[nx][ny] < 11) {
		int xx = hole[map[nx][ny] - 6].at(0).first;
		int yy = hole[map[nx][ny] - 6].at(0).second;
		if (xx == nx && yy == ny) {
			xx = hole[map[nx][ny] - 6].at(1).first;
			yy = hole[map[nx][ny] - 6].at(1).second;
		}
		dfs(xx, yy, dir, score);
	}
	else if (map[nx][ny] == -1) {
		if (res < score)res = score;
		return;
	}
}
int main(void) {
	int test_case;
	int T;
	scanf("%d", &T);
	for (test_case = 1; test_case <= T; test_case++) {
		memset(map, 0, sizeof(map));
		res = 0;
		for (int i = 0; i < 5; i++) {
			hole[i].clear();
		}
		start.clear();
		scanf("%d", &n);
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				scanf("%d", &map[i][j]);
				if (map[i][j] >= 6 && map[i][j] <= 10) {
					int num = map[i][j] - 6;
					hole[num].push_back(make_pair(i, j));
				}
				else if (map[i][j] == 0) {
					start.push_back(make_pair(i, j));
				}
			}
		}
		for (int i = 0; i < start.size(); i++) {
			for (int j = 0; j < 4; j++) {
				start_x = start[i].first;
				start_y = start[i].second;
				dfs(start_x, start_y, j, 0);
			}
		}
		printf("#%d %d\n", test_case, res);
	}
	return 0;
}