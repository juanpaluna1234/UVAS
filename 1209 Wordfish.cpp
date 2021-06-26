#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <numeric>
#include <cmath>

using namespace std;
struct Datos{
	string password;
	int dist;
};
typedef struct Datos Datos;

bool orgDatos(Datos d1, Datos d2){
	if(d1.dist == d2.dist){
		return d1.password < d2.password;
	}
	return d1.dist > d2.dist;
}

int main(){
	int i = 0, dife = 0, j = 0, min = 0;	
	string clave;
	Datos temp;
	Datos guard;
	vector<Datos> claves;
	while(getline(cin,clave)){
		claves.clear();
		min = 0;
		temp.password = clave;
		temp.dist = 0;
		guard = temp;
		claves.push_back(temp);
		for(i = 0; i < 10; i++){
			next_permutation(temp.password.begin(),temp.password.end());
			claves.push_back(temp);
		}
		for(i = 0; i < 10; i++){
			prev_permutation(guard.password.begin(),guard.password.end());
			claves.push_back(guard);
		}
		for(i = 0; i < claves.size(); i++){
			for(j = 0; j+1 < claves.at(i).password.size(); j++){
				dife = abs(claves.at(i).password[j]-claves.at(i).password[j+1]);
				if(j == 0){
					min = dife;
				}
				if(dife < min){
					min = dife;
				}
			}
			claves.at(i).dist = min;
		}
		sort(claves.begin(),claves.end(),orgDatos);
		cout  << claves.at(0).password << claves.at(0).dist <<"\n";
	}
	return 0;
}
//complejidad aproximada: O(n)
