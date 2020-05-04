#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<algorithm>
#include<vector>
using namespace std;

struct Brick {
	int s, h, w;
	Brick(int a, int b, int c) {
		s = a;
		h = b;
		w = c;
	}
	bool operator<(const Brick& b)const {
		return s > b.s;
	}
};

int main(void) {
	int n, a, b, c, max_h = 0, res = 0;
	scanf("%d", &n);
	vector<Brick>Bricks;
	vector<int>dp(n, 0);
	for (int i = 0; i < n; i++) {
		scanf("%d%d%d", &a, &b, &c);
		Bricks.push_back(Brick(a, b, c));
	}
	sort(Bricks.begin(), Bricks.end());
	dp[0] = Bricks[0].h;
	res = dp[0];
	for (int i = 1; i < n; i++) {
		max_h=0;
		for (int j = i - 1; j >= 0; j--) {
			if (Bricks[j].w > Bricks[i].w&& dp[j] > max_h) {
				max_h = dp[j];
			}
		}
		dp[i] = max_h + Bricks[i].h;
		res = max(res, dp[i]);
	}
	printf("%d\n", res);
	return 0;
}