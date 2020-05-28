#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
using namespace std;

int d, w, k,ans;

bool check(int film[13][20]) {
	for (int j = 0; j < w; j++) {
		bool chk = false;
		for (int i = 0; i <= d-k; i++) {
			bool flag = true;
			for (int l = i + 1; l < i + k; l++) {
				if (film[i][j] != film[l][j]) {
					flag = false;
					break;
				}
			}
			if (flag) {
				chk = true;
				break;
			}
		}
		if (!chk) {
			return false;
		}
	}
	return true;
}

void f_copy(int film[13][20], int n_film[13][20]) {
	for (int i = 0; i < d; i++) {
		for (int j = 0; j < w; j++) {
			n_film[i][j] = film[i][j];
		}
	}
}

void solve(int cnt, int index, int film[13][20]) {
	if (cnt >= ans)return;
	if (check(film)) {
		ans = cnt;
		return;
	}
	if (index == d)return;

	int n_film[13][20];
	f_copy(film, n_film);

	solve(cnt, index + 1, n_film);

	for (int j = 0; j < w; j++) {
		n_film[index][j] = 0;
	}
	solve(cnt + 1, index + 1, n_film);

	for (int j = 0; j < w; j++) {
		n_film[index][j] = 1;
	}
	solve(cnt + 1, index + 1, n_film);
}

int main(void) {
	int test_case;
	scanf("%d", &test_case);
	for (int i = 1; i <= test_case; i++) {
		ans = 20;
		scanf("%d%d%d", &d, &w, &k);
		int film[13][20];
		for (int i = 0; i < d; i++) {
			for (int j = 0; j < w; j++) {
				scanf("%d", &film[i][j]);
			}
		}
		if (k == 1) {
			printf("#%d 0\n", i);
			continue;
		}
		solve(0, 0, film);
		printf("#%d %d\n", i, ans);
	}
	return 0;
}