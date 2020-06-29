#define CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include <algorithm>
#include <queue>
using namespace std;

int T, N, W, H, answer;
int d[4][2] = { {0, -1}, {1, 0}, {0, 1}, {-1, 0} };
int map[5][16][13];

void nthBead(int bead);
void copyMap(int bead);
void breaking(int x, int y, int bead);
void dropBlock(int bead);

int main(void) {
	scanf("%d", &T);

	for (int i = 1; i <= T; i++) {
		scanf("%d%d%d", &N, &W, &H);
		answer = 987654321;

		for (int j = 0; j < H; j++) {
			for (int k = 0; k < W; k++) {
				scanf("%d", &map[0][j][k]);
			}
		}

		nthBead(1);
		if (answer == 987654321)
			answer = 0;
		printf("#%d %d\n", i, answer);
	}

	return 0;
}

void nthBead(int bead) {
	if (bead > N) {
		int temp = 0;
		for (int i = 0; i < H; i++)
			for (int j = 0; j < W; j++)
				if (map[bead - 1][i][j] >= 1)
					temp++;

		answer = min(answer, temp);
		return;
	}
	for (int i = 0; i < W; i++) {
		copyMap(bead); 
		int j = 0;
		for (j; j < H; j++) {
			if (map[bead][j][i]) {
				breaking(i, j, bead);
				break;
			}
		}
		if (j == H) continue;
		dropBlock(bead);
		nthBead(bead + 1);
	}
}

void copyMap(int bead) {
	for (int i = 0; i < H; i++)
		for (int j = 0; j < W; j++)
			map[bead][i][j] = map[bead - 1][i][j];
}

void breaking(int x, int y, int bead) {
	int block = map[bead][y][x];
	map[bead][y][x] = 0;

	for (int i = 0; i < block; i++) {
		for (int j = 0; j < 4; j++) {
			int nx = x + i * d[j][0];
			int ny = y + i * d[j][1];
			if (nx < 0 || ny < 0 || nx >= W || ny >= H || map[bead][ny][nx] == 0) continue;
			breaking(nx, ny, bead);
		}
	}
}

void dropBlock(int bead) {
	queue <int> q;
	for (int i = 0; i < W; i++) {
		for (int j = H - 1; j >= 0; j--) {
			if (map[bead][j][i]) {
				q.push(map[bead][j][i]);
				map[bead][j][i] = 0;
			}
		}
		int j = H - 1;
		while (!q.empty()) {
			map[bead][j][i] = q.front();
			j--;
			q.pop();
		}
	}
}


