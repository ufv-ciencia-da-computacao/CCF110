#include <stdio.h>

int revertInt(int);

int main() {
  int num;
  scanf("%d", &num);
  printf("%d\n", revertInt(num));
  return 0;
}

int revertInt(int num) {
  static int reverse = 0;
  if (num == 0) return 0;
  reverse *=  10;
  reverse += num % 10;
  revertInt(num/10);
  return reverse;
}