#include <stdio.h>

int main (){
	long long int n = 0, i = 0, buenas = 0;
	long double cent = 0, temp = 0;
	while(scanf("%d", &n) != EOF){
		cent = 0;
		temp = 0;
		buenas = 0;
		temp = n%100;
		n = n/100;
		cent = (temp) + cent;
		temp = n%100;
		n = n/100;
		cent = (temp*100) + cent;
		temp = n%100;
		n = n/100;
		cent = (temp*6000) + cent;	
		temp = n%100;
		n = n/100;
		cent = (temp*360000) + cent;
		cent = (cent*10000000)/8640000;
		buenas = (int)cent;
		printf("%07d\n",buenas);
	}
	return 0;
}
