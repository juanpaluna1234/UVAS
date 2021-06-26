#include <stdio.h>
#include <string.h>
int main(){
	long unsigned int casos = 1, tam = 0;
	char valor[5001], num = '0', num2 = '0';
	scanf("%d",&casos);
	while(casos){
		scanf("%s", valor);
		tam = strlen(valor);
		num = valor[tam-1];
		if(num == '1' && tam == 1){
			printf("66\n");
		}
		else if(num == '0' && tam == 1){
			printf("1\n");
		}
		else if(num == '0' || num == '5'){
			printf("76\n");
		}
		else if(num == '1' || num == '6'){
			printf("16\n");
		}
		else if(num == '2' || num == '7'){
			printf("56\n");
		}
		else if(num == '3' || num == '8'){
			printf("96\n");
		}
		else if(num == '4' || num == '9'){
			printf("36\n");
		}
		casos = casos - 1;
	}
	return 0;
}
