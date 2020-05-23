#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<iostream>
#include<string>
#include<algorithm>
using namespace std;
string s;
int num;
int maximum;
void dfs(int cur, int cnt) {
	if (cnt == num) {
		if (num == 1) {
			int maxi = stoi(s);
			maximum = max(maximum, maxi);
			return;
		}
		else {
			int maxii = stoi(s);
			maximum = max(maximum, maxii);
			return;
		}
	}
	else {
		if (num == 1) {
			for (int i = cur; i < s.length(); i++) {
				for (int j = i + 1; j < s.length(); j++) {
						swap(s[i], s[j]);
						dfs(i, cnt + 1);
						swap(s[i], s[j]);
				}
			}

		}
		else {
			for (int i = cur; i < s.length(); i++) {
				for (int j = i + 1; j < s.length(); j++) {
					if (s[i] <= s[j]) {
						swap(s[i], s[j]);
						dfs(i, cnt + 1);
						swap(s[i], s[j]);
					}
				}
			}
		}
	}
}

int main(void) {
	int test_case;
	int T;
	scanf("%d", &T);
	for (test_case = 1; test_case <= T; ++test_case) {
		cin >> s >> num;
		if (num == 1)maximum = -1;
		else {
			maximum = stoi(s);
		}
		dfs(0, 0);
		printf("#%d %d\n", test_case, maximum);
	}
	return 0;
}