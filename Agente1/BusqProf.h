#include<iostream>
#include<vector>
#include<queue>
using namespace std;
typedef struct Nodo{
    Nodo *link1;
    Nodo *link2;
    Nodo *link3;
    char *pos;
}Nodo;
void func_prin(string matrix,char *pos_ini, char *pos_fin);
vector<char*>path();
void build_tree(Nodo *&raiz,string matrix,char *pos_ini, char *pos_fin);
void arbol(Nodo *&raiz);
Nodo *C_nuevo_Nodo(char *clave);
void preorden(Nodo *&R);
void elim_hoja(Nodo *&raiz);


void func_prin(string matrix,char *pos_ini, char *pos_fin){
    Nodo *Raiz=C_nuevo_Nodo(pos_ini);
    build_tree(Raiz,matrix,pos_ini,pos_fin);
}

Nodo* C_nuevo_Nodo(char *clave){
    Nodo* Raiz=new Nodo;
    Raiz->pos=clave;
    Raiz->link1=NULL;
    Raiz->link2=NULL;
    Raiz->link3=NULL;
    return Raiz;
}

void build_tree(Nodo *&raiz,string matrix,char *pos_ini, char *pos_fin){
          char *new_pos;
        //evaluar si en la posicion actual existen uno o más enlaces
        bool band[3];
        if (!raiz)
        {
            raiz=C_nuevo_Nodo(pos_ini);
        }else{
            if (raiz->link1)//construir enlaces a donde haya camino
             {
                build_tree(raiz->link1,matrix,new_pos,pos_fin);
                band[0]=true;
            }
            if (raiz->link2)
            {
                build_tree(raiz->link2,matrix,new_pos,pos_fin);
                band[1]=true;
            }
            if (raiz->link3)
            {
            build_tree(raiz->link3,matrix,new_pos,pos_fin);
            band[2]=true;
            }
        } 

        
        return;
}