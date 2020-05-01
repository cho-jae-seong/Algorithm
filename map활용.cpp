#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<iostream>
#include<map>
#include<string>
using namespace std;

int main(void) {
	map<string, int>ch;
	map<string, int>::iterator it;
	string a;
	int n;
	cin >> n;
	for (int i = 1; i <= n; i++) {
		cin >> a;
		ch[a]++;
	}

	int max = 0;
	string res;
	for (it = ch.begin(); it != ch.end(); it++) {
		if (it->second > max) {
			max = it->second;
			res = it->first;
		}
	}
	cout << res << " : " << max << "\n";
	return 0;
}