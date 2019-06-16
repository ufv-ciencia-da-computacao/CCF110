#include <stdio.h>

int max(int, int);
int min(int, int);
int GCD(int, int);

int main() {
  printf("GCD = %d\n", GCD(10,5));
 return 0;
}

int GCD(int a, int b) {
  if (a == b) {
    return a;
  } else {
    GCD(max(a-b, b), min(a-b, b)); 
  }
}

int max(int a, int b) {
  return a > b ? a : b;
}

int min(int a, int b) {
  return a < b ? a : b;  
}
