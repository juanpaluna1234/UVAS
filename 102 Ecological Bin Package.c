#include <stdio.h>

int main(){
	int i, j, sum, min, n;
	char result[4], temp[4];
	unsigned long int num[3][3];
	while(scanf("%d %d %d %d %d %d %d %d %d", &num[0][0], &num[1][0], &num[2][0], &num[0][1], &num[1][1], &num[2][1], &num[0][2], &num[1][2], &num[2][2]) != EOF){
	
	
		for(i = 0; i < 6; ++i){
			if(i == 0){
				sum =  num[0][1] + num[0][2] + num[1][0] + num[1][1] + num[2][0] + num[2][2];
				result[0] = 'B';
				result[1] = 'C';
				result[2] = 'G';
				result[3] = '\0';
				min = sum;
			}
			if(i == 1){
				sum =  num[0][1] + num[0][2] + num[1][0] + num[1][2] + num[2][0] + num[2][1];
				temp[0] = 'B';
				temp[1] = 'G';
				temp[2] = 'C';
				temp[3] = '\0';
			}
			if(i == 2){
				sum =  num[0][0] + num[0][2] + num[1][0] + num[1][1] + num[2][1] + num[2][2];
				temp[0] = 'C';
				temp[1] = 'B';
				temp[2] = 'G';
				temp[3] = '\0';
			}
			if(i == 3){
				sum =  num[0][1] + num[0][0] + num[1][0] + num[1][2] + num[2][1] + num[2][2];
				temp[0] = 'C';
				temp[1] = 'G';
				temp[2] = 'B';
				temp[3] = '\0';
			}
			if(i == 4){
				sum =  num[0][0] + num[0][2] + num[1][1] + num[1][2] + num[2][0] + num[2][1];
				temp[0] = 'G';
				temp[1] = 'B';
				temp[2] = 'C';
				temp[3] = '\0';
			}
			if(i == 5){
				sum =  num[0][1] + num[0][0] + num[1][1] + num[1][2] + num[2][0] + num[2][2];
				temp[0] = 'G';
				temp[1] = 'C';
				temp[2] = 'B';
				temp[3] = '\0';
			}
			if(sum < min){
				result[0] = temp[0];
				result[1] = temp[1];
				result[2] = temp[2];
				result[3] = temp[3];
				min = sum;
			}

		}
		printf("%c%c%c %d\n", result[0], result[1], result[2], min);
	}
	return 0;		
}
