#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int magicNum(long long n){
	char numero[2000] = {};
	unsigned long long prueba[] = {0,0,0,0,0,0,0,0,0,0};
	unsigned long long com = 0, j = 0;
	int i = 0;
	while(n > 0){
		numero[i] = n%10 + '0';
		n = n/10;
		i++;
	}
	for(j = 0; j < strlen(numero); ++j){
		com = numero[j] - '0';
		prueba[com] = prueba[com] + 1;
	}
	for(j = 0; j < 10; ++j){
		if(prueba[j] > 1){
			return 0;
		}
	}
	return 1;
}



int main(){
	long long int num=0, s1 = 0, s2 = 0;
	int casos = 0;
	scanf("%d", &casos);
	while(casos > 0){
		scanf("%lli", &num);
		s2 = 0;
		s1 = 1;
		while(num*s1 <= 2*9876543210){
			s2 = s1*num;
			if(magicNum(s1) && magicNum(s2)){
					printf("%lli / %lli = %lli\n", s2, s1, num);
			}
			s1 = s1 + 1;
		}
		if (casos-1 != 0){
			printf("\n");
		}
		num = 0;
		casos--;
	}
		
}



