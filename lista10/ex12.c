#include <stdio.h>

int seg(int, int, int);

int main() {
  int h, m, s;
  scanf("%d %d %d", &h, &m, &s);

  printf("Segundos: %d\n", seg(h, m, s));
  return 0;
}

int seg(int h, int m, int s) {
  return h*3600+m*60+s;
}