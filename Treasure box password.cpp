#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<string>
#include<vector>
#include<ctype.h>
#include<queue>
#include<math.h>
using namespace std;
int n, k,cut,sum1=0,sum2=0,sum3=0,sum4=0;
vector<int>v;
string s;
bool compare(int i, int j) {
	return j < i;
}
int main(void) {
	int test_case;
	scanf("%d", &test_case);
	for (int i = 1; i <= test_case; i++) {
		v.clear();
		scanf("%d%d", &n, &k);
		cin >> s;
		cut = n / 4;
		for (int j = 0; j < cut; j++) {
			sum1 = sum2 = sum3 = sum4 = 0;
			for (int p = 0; p < s.length(); p++) {
				if (p < cut) {
					if (isalpha(s[p])) {
						sum1 += (s[p] - 55)*pow(16,cut-p-1);
					}
					else {
						sum1 += (s[p] - 48)*pow(16,cut-p-1);
					}
				}
				else if (cut <= p && p < cut * 2) {
					if (isalpha(s[p])) {
						sum2 += (s[p] - 55)*pow(16,cut*2-p-1);
					}
					else {
						sum2 += (s[p] - 48)*pow(16,cut*2-p-1);
					}
				}
				else if (cut * 2 <= p && p < cut * 3) {
					if (isalpha(s[p])) {
						sum3 += (s[p] - 55)*pow(16,cut*3-p-1);
					}
					else {
						sum3 += (s[p] - 48)*pow(16,cut*3-p-1);
					}
				}
				else if (cut * 3 <= p && p < cut * 4) {
					if (isalpha(s[p])) {
						sum4 += (s[p] - 55)*pow(16,cut*4-p-1);
					}
					else {
						sum4 += (s[p] - 48)*pow(16,cut*4-p-1);
					}
				}
			}
			v.push_back(sum1); v.push_back(sum2); v.push_back(sum3); v.push_back(sum4);
			rotate(s.rbegin(), s.rbegin() + 1, s.rend());
		}
		sort(v.begin(), v.end(),compare);
		v.erase(unique(v.begin(), v.end()), v.end());
		printf("#%d %d\n", i, v[k-1]);
	}
	return 0;
}
