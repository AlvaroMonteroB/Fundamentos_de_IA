#include<iostream>
#include<vector>
#include<queue>
using namespace std;
typedef struct Nodo{
    Nodo *link;
    char *pos;
}Nodo;
void func_prin(char*matrix,char *pos_ini, char *pos_fin);
vector<char*>path();
void arbol(Nodo *&raiz);
Nodo *  C_nuevo_Nodo(char *clave);
void preorden(Nodo *&R);
void elim_hoja(Nodo *&raiz);


void func_prin(char*matrix,char *pos_ini, char *pos_fin){
    Nodo *Raiz=C_nuevo_Nodo(pos_ini);
}

Nodo* C_nuevo_Nodo(char *clave){
    Nodo* Raiz=new Nodo;
    Raiz->pos=clave;
    return Raiz;
}