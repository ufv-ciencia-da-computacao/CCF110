#include <stdio.h>
#include <stdlib.h>

void tabuada(long long, long long); 

int main() {
  tabuada(1, 7);
  return 0;
}

void tabuada(long long begin, long long end) {
  if (begin > end) {
    return;
  } else {
    printf("%lld x %lld = %lld\n", begin, end, begin*end);
    return tabuada(begin+1, end);
  }
  
  
}