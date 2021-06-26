#include <iostream>
#include <vector>
#include <string>
#include <list>

using namespace std;

int main(){
	list <string> phrase;
	string cad;
	string aux;
	int cont, i;
	while(getline(cin, cad)){
		cont = 0;
		aux = "";
		phrase.clear();
		for(i = 0; i < cad.size(); i++){
			if(cad[i] == '['){
				if(cont == 0){
					phrase.insert(phrase.begin(), aux);
				}
				else if(cont = 1){
					phrase.push_back(aux);
				}
				aux = "";
				cont = 0;
			}
			else if(cad[i] == ']'){
				if(cont == 0){
					phrase.insert(phrase.begin(), aux);
				}
				else if(cont = 1){
					phrase.push_back(aux);
				}
				aux = "";
				cont = 1;
			}
			else{
				aux.push_back(cad[i]);
			}
		}
		if(cont == 0){
			phrase.insert(phrase.begin(), aux);
		}
		else if(cont = 1){
			phrase.push_back(aux);
		}

		list<string> :: iterator it;
		for(it = phrase.begin(); it != phrase.end(); it++){
			cout << *it;
		}
		printf("\n");
	}
	return 0;
	
}

