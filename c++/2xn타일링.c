#include<stdio.h>
#define SZ 1001
int ans[SZ];

void solution(int n) {
  ans[1] = 1;
  ans[2] = 2;
  for(int i=3; i<=n; i++){
    ans[i] = (ans[i-1] + ans[i-2])%10007;
  }
  printf("%d", ans[n]);
}
int main(){
  int n;
  scanf("%d", &n);
  solution(n);
}
  
