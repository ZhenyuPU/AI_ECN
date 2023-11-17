# include <stdio.h>
# include <stdlib.h>
int main(){
int *a = calloc(12, sizeof(int));

printf("%d", a[111]);

return 0;
}