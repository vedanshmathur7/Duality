#include <stdio.h>

void palindromic_pattern(int n) {
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n - i; j++) {
            printf(" ");
        }

        for (int j = 0; j < i; j++) {
            printf("%c", 'A' + j);
        }

        for (int j = i - 2; j >= 0; j--) {
            printf("%c", 'A' + j);
        }

        printf("\n");
    }
}

int main() {
    int rows;

    printf("Enter the number of rows: ");
    scanf("%d", &rows);

    palindromic_pattern(rows);

    return 0;
}
