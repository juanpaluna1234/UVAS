#include <stdio.h>

int permuta( int x, int y, int z, int num){
	int perm = 0;
	if(x == z && z == y && x == y){
		perm = perm + 1;
	}
	else if(x != y && y == z && z != x){
		perm = perm + 3;
	}
	else if(y != z && z == x && x != y){
		perm = perm + 3;
	}
	else if(z != x && x == y && y != z){
		perm = perm + 3;
	}
	else if(x != z && z != y && x != y){
		perm = perm + 6;
	}
	return perm;
}
int main(){
	
  	int num, i, j, k, com, per;
	while(scanf("%d", &num) > 0 && num > 0){
		com = 0;
		per = 0;
		if(num <=180){
			for(i = 0; i < 61; ++i){
				for(j = i; j < 61; ++j){
					for(k = j; k < 61; ++k){
						if((i > 20 && i <41) && (i%2 ==0 || i%3 == 0)){
							if((j > 20 && j <41) && (j%2 ==0 || j%3 == 0)){
								if((k > 20 && k <41) && (k%2 ==0 || k%3 == 0)){
									if(i+j+k == num){
										com = com + 1;
										per = permuta(i, j, k, num) + per;
									}
								}
								if((k > 40 && k < 61) && k%3 == 0 || k == 50){	
									if(i+j+k == num){
										com = com + 1;
										per = permuta( i, j, k, num) + per;
									}
								}
								if(k >= 0 && k <= 20){
									if(i+j+k == num){
										com = com + 1;
										per = permuta( i, j, k, num) + per;
									}	
								}
							}
							if((j > 40 && j < 61) && (j%3 == 0 || j == 50)){
								if((k > 20 && k <41) && (k%2 ==0 || k%3 == 0)){
									if(i+j+k == num){
										com = com + 1;
										per = permuta( i, j, k, num) + per;
									}
								}
								if((k > 40 && k < 61) && (k%3 == 0 || k == 50)){	
									if(i+j+k == num){
										com = com + 1;
										per = permuta( i, j, k, num) + per;
									}
								}
								if(k >= 0 && k <= 20){
									if(i+j+k == num){
										com = com + 1;
										per = permuta( i, j, k, num) + per;
									}
								}
							}
							if(j >= 0 && j <= 20){
								if((k > 20 && k <41) && (k%2 ==0 || k%3 == 0)){
									if(i+j+k == num){
										com = com + 1;
										per = permuta( i, j, k, num) + per;
									}
								}
								if((k > 40 && k < 61) && (k%3 == 0 || k == 50)){	
									if(i+j+k == num){
										com = com + 1;
										per = permuta( i, j, k, num) + per;
									}
								}
								if(k >= 0 && k <= 20){
									if(i+j+k == num){
										com = com + 1;
										per = permuta( i, j, k, num) + per;
									};
								}
							}
						
						}
						if((i > 40 && i < 61) && (i%3 == 0 || i == 50)){
							if((j > 20 && j <41) && (j%2 ==0 || j%3 == 0)){
								if((k > 20 && k <41) && (k%2 ==0 || k%3 == 0)){
									if(i+j+k == num){
										com = com + 1;
										per = permuta( i, j, k, num) + per;
									}
								}
								if((k > 40 && k < 61) && (k%3 == 0 || k == 50)){	
									if(i+j+k == num){
										com = com + 1;
										per = permuta( i, j, k, num) + per;
									}
								}
								if(k >= 0 && k <= 20){
									if(i+j+k == num){
										com = com + 1;
										per = permuta( i, j, k, num) + per;
									}
								}
							}
							if((j > 40 && j < 61) && (j%3 == 0 || j == 50)){
								if((k > 20 && k <41) && (k%2 ==0 || k%3 == 0)){
									if(i+j+k == num){
										com = com + 1;
										per = permuta(i, j, k, num) + per;
									}
								}
								if((k > 40 && k < 61) && (k%3 == 0 || k == 50)){	
									if(i+j+k == num){
										com = com + 1;
										per = permuta(i, j, k, num) + per;
									}
								}
								if(k >= 0 && k <= 20){
									if(i+j+k == num){
										com = com + 1;
										per = permuta( i, j, k, num) + per;
									}
								}
							}
							if(j >= 0 && j <= 20){
								if((k > 20 && k <41) && (k%2 ==0 || k%3 == 0)){
									if(i+j+k == num){
										com = com + 1;
										per = permuta( i, j, k, num) + per;
									}
								}
								if((k > 40 && k < 61) && (k%3 == 0 || k == 50)){	
									if(i+j+k == num){
										com = com + 1;
										per = permuta( i, j, k, num) + per;
									}
								}
								if(k >= 0 && k <= 20){
									if(i+j+k == num){
										com = com + 1;
										per = permuta( i, j, k, num) + per;
									}
								}
							}	
						}
						if(i >= 0 && i <= 20){
							
							if((j > 20 && j <41) && (j%2 ==0 || j%3 == 0)){
								if((k > 20 && k <41) && (k%2 ==0 || k%3 == 0)){
									if(i+j+k == num){
										com = com + 1;
										per = permuta( i, j, k, num) + per;
									}
								}
								if((k > 40 && k < 61) && (k%3 == 0 || k == 50)){	
									if(i+j+k == num){
										com = com + 1;
										per = permuta( i, j, k, num) + per;
									}
								}
								if(k >= 0 && k <= 20){
									if(i+j+k == num){
										com = com + 1;
										per = permuta( i, j, k, num) + per;
									}
								}
							}
							if((j > 40 && j < 61) && (j%3 == 0 || j == 50)){	
								if((k > 20 && k <41) && (k%2 ==0 || k%3 == 0)){
									if(i+j+k == num){
										com = com + 1;
										per = permuta( i, j, k, num) + per;
									}
								}
								if((k > 40 && k < 61) && (k%3 == 0 || k == 50)){	
									if(i+j+k == num){
										com = com + 1;
										per = permuta( i, j, k, num) + per;
									}
								}
								if(k >= 0 && k <= 20){
									if(i+j+k == num){
										com = com + 1;
										per = permuta( i, j, k, num) + per;
									}
								}
							}
							if(j >= 0 && j <= 20){
								if((k > 20 && k <41) && (k%2 ==0 || k%3 == 0)){
									if(i+j+k == num){
										com = com + 1;
										per = permuta( i, j, k, num) + per;
									}
								}
								if((k > 40 && k < 61) && (k%3 == 0 || k == 50)){	
									if(i+j+k == num){
										com = com + 1;
										per = permuta( i, j, k, num) + per;
									}
								}
								if(k >= 0 && k <= 20){
									if(i+j+k == num){
										com = com + 1;
										per = permuta( i, j, k, num) + per;
									}
								}
							}	
						}
					}
				}
			}
			if(com != 0){
				printf("NUMBER OF COMBINATIONS THAT SCORES %d IS %d.\n", num, com);
				printf("NUMBER OF PERMUTATIONS THAT SCORES %d IS %d.\n", num, per);
				printf("**********************************************************************\n");
			}
			else {
				printf("THE SCORE OF %d CANNOT BE MADE WITH THREE DARTS.\n", num);
				printf("**********************************************************************\n");
			}
		}
		else{
			printf("THE SCORE OF %d CANNOT BE MADE WITH THREE DARTS.\n", num);
			printf("**********************************************************************\n");
		}	
	}
	printf("END OF OUTPUT\n");
	return 0;
}

