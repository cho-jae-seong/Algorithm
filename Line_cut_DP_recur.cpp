#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
int dy[50];

int dfs(int n) {
	if (dy[n] > 0)return dy[n];
	if (n == 1 || n == 2)return n;
	else return dy[n] = dfs(n - 1) + dfs(n - 2);
}

int main(void) {
	int n;
	scanf("%d", &n);
	printf("%d\n", dfs(n));
	return 0;
}