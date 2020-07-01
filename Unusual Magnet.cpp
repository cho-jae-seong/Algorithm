#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>

int magnet[4][8];

int main(void) {
    int T;
    scanf("%d", &T);
    for (int tc = 1; tc <= T; tc++) {

        int k;
        scanf("%d", &k);

        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 8; j++) {
                scanf("%d", &magnet[i][j]);
            }
        }

        while (k-- > 0) {
            int num;
            int dir;
            scanf("%d%d", &num, &dir);
            num -= 1;

            int dirArr[4] = { 0, };
            dirArr[num] = dir;

            for (int i = num; i < 3; i++) {
                if (magnet[i][2] != magnet[i + 1][6]) {
                    dirArr[i + 1] = dirArr[i] * -1;
                }
                else {
                    break;
                }
            }

            for (int i = num; i > 0; i--) {
                if (magnet[i][6] != magnet[i - 1][2]) {
                    dirArr[i - 1] = dirArr[i] * -1;
                }
                else {
                    break;
                }
            }

            for (int i = 0; i < 4; i++) {

                if (dirArr[i] == 1) {
                    int tmp = magnet[i][7];
                    for (int j = 7; j > 0; j--) {
                        magnet[i][j] = magnet[i][j - 1];
                    }
                    magnet[i][0] = tmp;
                }
                else if (dirArr[i] == -1) {
                    int tmp = magnet[i][0];
                    for (int j = 0; j < 7; j++) {
                        magnet[i][j] = magnet[i][j + 1];
                    }
                    magnet[i][7] = tmp;
                }
            }

        }

        int ans = 0;
        for (int i = 0; i < 4; i++) {
            if (magnet[i][0] == 1) {
                ans += (1 << i);
            }
        }

        printf("#%d %d\n", tc, ans);
    }
    return 0;
}
