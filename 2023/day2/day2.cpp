

#include <string>
#include <iostream>
#include <fstream>
#include <vector>


int main(){

    std::ifstream input {"input.txt"};

    if (!input.good()){
        std::cerr << "Error opening file : input.txt";
        return 1;
    }
    
    std::vector<std::string> games{};
    std::string word{};
    while (input.good()){
        input >> word;
        if (word[0]=='G'){

        }

    }


    //12 red cubes, 13 green cubes, and 14 blue cubes
    

    return 0;
}


