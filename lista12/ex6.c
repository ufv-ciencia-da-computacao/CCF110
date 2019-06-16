#include <stdio.h>

long long int fat(long long int);

int main() {
  printf("fat = %lld\n", fat(20));
  return 0;
}

long long int fat(long long int num) {
  if (num == 0 || num == 1) {
    return 1;
  } else if (num < 0){
    return -1;
  }
  return num*fat(num-1);
}
