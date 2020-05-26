#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<algorithm>
#include<memory.h>
using namespace std;
int n, cnt = 0, maximum = -1;
int des[21][21];
int dx[] = { 1,1,-1,-1 };
int dy[] = { -1,1,1,-1 };
int ch[101];
int tempx, tempy;
int nx, ny;
void dfs(int x, int y, int cur, int go) {
	cnt = 0;
	ch[des[x][y]]++;
	cnt++;
	nx = x;
	ny = y;
	for (int i = 0; i < cur; i++) {
		tempx = nx;
		tempy = ny;
		nx = nx + dx[0];
		ny = ny + dy[0];
		if (nx >= 0 && ny >= 0 && nx < n && ny < n) {
			ch[des[nx][ny]]++;
			if (ch[des[nx][ny]] > 1) {
				cnt = 0; return;
			}
			cnt++;
		}
		else {
			cnt = 0; return;
		}
	}
	for (int i = 0; i < go; i++) {
		tempx = nx;
		tempy = ny;
		nx = nx + dx[1];
		ny = ny + dy[1];
		if (nx >= 0 && ny >= 0 && nx < n && ny < n) {
			ch[des[nx][ny]]++;
			if (ch[des[nx][ny]] > 1) {
				cnt = 0; return;
			}
			cnt++;
		}
		else {
			cnt = 0; return;
		}
	}
	for (int i = 0; i < cur; i++) {
		tempx = nx;
		tempy = ny;
		nx = nx + dx[2];
		ny = ny + dy[2];
		if (nx >= 0 && ny >= 0 && nx < n && ny < n) {
			ch[des[nx][ny]]++;
			if (ch[des[nx][ny]] > 1) {
				cnt = 0; return;
			}
			cnt++;
		}
		else {
			cnt = 0; return;
		}
	}
	for (int i = 0; i < go - 1; i++) {
		tempx = nx;
		tempy = ny;
		nx = nx + dx[3];
		ny = ny + dy[3];
		if (nx >= 0 && ny >= 0 && nx < n && ny < n) {
			ch[des[nx][ny]]++;
			if (ch[des[nx][ny]] > 1) {
				cnt = 0; return;
			}
			cnt++;
		}
		else {
			cnt = 0; return;
		}
	}
}

int main(void) {
	int test_case;
	scanf("%d", &test_case);
	for (int i = 1; i <= test_case; i++) {
		maximum = -1;
		memset(des, 0, sizeof(des));
		scanf("%d", &n);
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				scanf("%d", &des[i][j]);
			}
		}
		for (int i = 0; i < n - 2; i++) {
			for (int j = 1; j <= n - 2; j++) {
				for (int c = 1; c <= n - 2; c++) {
					for (int g = 1; g <= n - 2; g++) {
						memset(ch, 0, sizeof(ch));
						dfs(i, j, c, g);
						maximum = max(maximum, cnt);
					}
				}
			}
		}
		printf("#%d ", i);
		if (maximum == 0)printf("-1\n");
		else printf("%d\n", maximum);
	}
	return 0;
}