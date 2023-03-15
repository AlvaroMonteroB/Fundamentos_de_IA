#include "busqProf.h"
#include <iostream>
#include<stdio.h>
#include<vector>
using namespace std;
string matrix(char *filename);
void print_maze(string laberinto);
int main(){
    char ini[2],fin[2];
    char name[11]="matriz.txt";
    string laberinto=matrix(name);
    if (laberinto.empty())
    {
        cout<<"Couldnt store maze"<<endl;
        return 0;
    }
    func_prin(laberinto,ini,fin);
    print_maze(laberinto);

    return 0;
}


string matrix(char *filename){
    FILE *f=fopen(filename, "r");
    if (!f)
    {
        cout<<"There's no file"<<endl;
        return 0;
     }
     cout<<"File read"<<endl;
     vector<char> data;
     char c;
     c=fgetc(f);
     int data_header[2];
     data_header[0]=(int)c;
     c=fgetc(f);
     c=fgetc(f);
     data_header[1]=(int)c;
     c=fgetc(f);
     c=fgetc(f);
     for (int i = 0; i < data_header[0]*data_header[1]-1; i++)
     {
        data.push_back(c);
        c=fgetc(f);
     }
     data.push_back('\n');    
    string output=data.data();
     while (output.size()!=36)
     {
        output.pop_back();
     }
     
    return output;
    
}

void print_maze(string laberinto){
    cout<<laberinto<<endl; 
}