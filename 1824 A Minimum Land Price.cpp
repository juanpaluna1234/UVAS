#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <numeric>
#include <cmath>

using namespace std;


int main(){
	long long unsigned int casos= 0, i = 0, temp= 1, total = 0;
	vector<long long unsigned int>	num;
	scanf("%d",&casos);
	while(casos--){
		temp = 1;
		while(temp != 0){
			scanf("%d",&temp);
			num.push_back(temp);
		}
		num.pop_back();
		
		sort(num.begin(),num.end());
		
		for(i = 0; i < num.size(); i++){
			temp = num.at(i);
			temp = pow(temp,num.size()-i)*2;
			num.at(i) = temp;
		}
		total = accumulate(num.begin(), num.end(), 0);
		if(total <= 5000000){
			printf("%d", total);
		}
		else{
			printf("Too expensive");
		}
		num.clear();
		printf("\n");
	}
}
//complejidad aproximada; O(nlogn)
