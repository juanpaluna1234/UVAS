#include <stdio.h>

int cycleLenght(long long unsigned int num){
	long unsigned int contador = 1;
	while (num != 1){
		if (num%2 == 0){
			num = num/2;
			contador = contador + 1;
		}
		else if(num%2 != 0){
			num = 3*num + 1;
			contador = contador + 1;
		}
	}
	return contador;	
}

int main(){
	long long unsigned int i = 0, j = 0, n = 0, max = 0, temp = 0;
	while(scanf("%d %d", &i, &j) != EOF){
		max = 0;
		if(i <= j){
			for(n = i; n <= j; n++){
				temp = cycleLenght(n);
				if(temp > max){
					max = temp;
				}
			}
		}
		else if(j < i){
			for(n = j; n <= i; n++){
				temp = cycleLenght(n);
				if(temp > max){
					max = temp;
				}
			}
		}
		printf("%d %d %d\n", i, j, max);
	}
	return 0;
}
