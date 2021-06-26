#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <numeric>
#include <cmath>
#include <cstdio>
using namespace std;

int magicNumb(int n){
	string num = to_string(n);
	string cero = "0";
	int i = 0, k = 0;
	for(i = 0; i < num.size(); i++){
		for(k = i; k < num.size()-1; k++){
			if(num[k+1] == num[i]){
				return 0;
			}
		}
	}
	if(n < 9999){
		for(i = 0; i < num.size(); i++){
			if(cero[0]==num[i]){
				return 0;
			}
		}
	}
	return 1;
}
int diferent(long int j, long int i){
	int k = 0;
	if(i < 1234 || i > 98765 || j < 1234 || j > 98765){
		return 0;
	}
	else if(i < 9999 && j < 9999){
	    return 0;
	}
	else if(i < 9999){
		string num1 = to_string(i);
		num1.append("0");
		string num2 = to_string(j);
		for(k = 0; k < num1.size(); k++){
    		if(num1[k] == num2[0] || num1[k] == num2[1] || num1[k] == num2[2] || num1[k] == num2[3] ||num1[k] == num2[4]){
    			return 0;
    		}
		}
	}
	else if(j < 9999){
		string num1 = to_string(j);
		num1.append("0");
		string num2 = to_string(i);
		for(k = 0; k < num1.size(); k++){
    		if(num1[k] == num2[0] || num1[k] == num2[1] || num1[k] == num2[2] || num1[k] == num2[3] ||num1[k] == num2[4]){
    			return 0;
    		}
		}
	}
	else if(j<9999 && i<9999){
		return 0;
	}
	else{
	    string num1 = to_string(j);
		string num2 = to_string(i);
		for(k = 0; k < num1.size(); k++){
    		if(num1[k] == num2[0] || num1[k] == num2[1] || num1[k] == num2[2] || num1[k] == num2[3] ||num1[k] == num2[4]){
    			return 0;
    		}
		}
	}
	return 1;
}


int main(){
	long long int num=1, s1 = 0, s2 = 0;
	int casos = 0, cont = 0;
	while(num > 0){
		scanf("%lli", &num);
		if(num != 0 && cont > 0){
		    printf("\n");
		}
		casos = 0;
		s2 = 0;
		s1 = 1234;
		while(s1 <= 987654){
			s2 = s1*num;
			if(s2 < 987654){
				if(magicNumb(s1) && magicNumb(s2)){
					if(diferent(s1, s2)){
						casos = casos + 1;
						if(s1 < 9999){
						    printf("%lli / 0%lli = %lli\n", s2, s1, num);
						}
						else{
						    printf("%lli / %lli = %lli\n", s2, s1, num);
						}
					}	
				}
			}
			s1 = s1 + 1;
		}
		if(casos == 0 && num != 0){
			printf("There are no solutions for %lli.\n", num);
		}
		cont = cont + 1;
	}
}
//complejidad aproximada: O(n^2)
