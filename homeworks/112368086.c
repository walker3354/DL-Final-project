#include <stdio.h>
#include <string.h>

int main(){
    int inverse=0;
    char str1[100];
    printf("please input the sequence: ");
    scanf("%s", str1);
    for (int i=0; i< strlen(str1); i++){
        for (int j=i+1; j<strlen(str1); j++){
            if (str1[i]>str1[j]){
                inverse++;
            }
        }
    }
    printf("inverse= %d", inverse);
    return 0;
}      