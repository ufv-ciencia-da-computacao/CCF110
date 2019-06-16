#include <stdio.h>

void multiplo5(int, int);

int main() {
  multiplo5(10, 20);
  return 0;
}

void multiplo5(int begin, int end) {
  if (begin > end) {
    return;
  } else {
    if (begin % 5 == 0) {
      printf("%d eh multiplo\n", begin);
    }
    multiplo5(begin+1, end);
  }
  
}