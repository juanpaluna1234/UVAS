#include <iostream>
#include <string>
#include <vector>
#include <stack>


using namespace std;

int main(){
	string letters;
	int i, j, cont, casos = 0;
	stack<char> nuevo;
	vector<stack<char>> containers;
	getline(cin, letters);
	while (letters != "end")
	{
		containers.clear();
		
		for(i = 0; i < letters.size(); i++){
			while(!nuevo.empty()){
				nuevo.pop();
			}
			if(containers.empty()){
				nuevo.push(letters[i]);
				containers.push_back(nuevo);
			}
			else{
				for(j = 0; j < containers.size() ; j++){
					cont = 0;
					if(containers[j].top() >= letters[i]){
						containers[j].push(letters[i]);	
						cont = 1;
						break;	
					}
				}
				if(cont == 0){
					nuevo.push(letters[i]);
					containers.push_back(nuevo);
				}
			}
				
		}
		casos += 1;
		printf("Case %d: %d\n",casos,containers.size());
		getline(cin, letters);
	}
	return 0;
}
