#include <stdio.h>
#include <stdlib.h>

int MOD(int, int);

int main() {
  printf("MOD(%d, %d) = %d\n", 10, 7, MOD(abs(10), abs(7)));

  return 0;
}

int MOD(int a, int b) {
  if (a < b) {
    return b;
  } else if (a == b) {
    return 0;
  }
  return MOD(abs(a)-abs(b), abs(b));  
}

