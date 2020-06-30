#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>

int main(void) {
	int test_case;
	int T;
	scanf("%d", &T);
	for (test_case = 1; test_case <= T; test_case++) {
		int n, x;
		int map[20][20];	
		scanf("%d%d", &n, &x);
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				scanf("%d", &map[i][j]);
			}
		}
		int ans = 0;
		for (int i = 0; i < n; i++) {
			int cnt = 1;
			for (int j = 1; j < n; j++) {
				int prev = map[i][j - 1];
				int cur = map[i][j];
				if (prev == cur)	
					cnt++;
				else if (prev - cur == 1 && cnt >= 0) 
					cnt = (-x + 1);
				else if (prev - cur == -1 && cnt >= x) 
					cnt = 1;
				else {
					cnt = -1;
					break;
				}
			}
			if (cnt >= 0)ans++;

			cnt = 1;
			for (int j = 1; j < n; j++) {
				int prev = map[j-1][i];
				int cur = map[j][i];
				if (prev == cur)
					cnt++;
				else if (prev - cur == 1 && cnt >= 0)
					cnt = (-x + 1);
				else if (prev - cur == -1 && cnt >= x)
					cnt = 1;
				else {
					cnt = -1;
					break;
				}
			}
			if (cnt >= 0)ans++;
		}
		printf("#%d %d\n", test_case, ans);
	}
	return 0;
}