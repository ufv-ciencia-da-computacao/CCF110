#include <stdio.h>

int min(int a, int b, int c);

int main() {
  int a, b, c;
  scanf("%d %d %d", &a, &b, &c);
  
  return 0;
}

int min(int a, int b, int c) {
  int smallest = b;
  if (a >= b) {
    smallest = a;
  } 

  if (c >= smallest) {
    smallest = c;
  }

  return smallest;  
}