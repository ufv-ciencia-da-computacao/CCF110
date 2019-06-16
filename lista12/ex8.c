#include <stdio.h>
#include <stdlib.h>

int DIV(int a, int b);

int main () {
  printf("DIV(%d, %d) = %d\n", 10, 5, DIV(abs(10), abs(5)));
  return 0;
}

int DIV(int a, int b) {
  if (a < b) {
    return 0;
  } else if (a == b) {
    return 1;
  }
  return 1+DIV(abs(a)-abs(b), abs(b));
  
  
}