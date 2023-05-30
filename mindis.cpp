#include <iostream>
#include<vector>
#include<cmath>
using namespace std;
double dist_manh(vector<double>clase,vector<double>muestra);

class neighbor{
    public:
    vector<double>caracteristicas;
    string nombre;
    neighbor(vector<double>caract,string nom){
        caracteristicas=caract;
        nombre=nom;

    }
};

int main(){
    vector<neighbor*>vecinos;
    vecinos.push_back( new neighbor({5.1,3.5,1.4,.2},"setosa"));
    vecinos.push_back(new neighbor({4.9,3,1.4,.2},"setosa"));
    vecinos.push_back(new neighbor({4.7,3.2,1.3,0.2},"setosa"));
    vecinos.push_back(new neighbor({4.6,3.1,1.5,.2},"setosa"));
    vecinos.push_back(new neighbor({5,3.6,1.4,.2},"setosa"));
    vecinos.push_back(new neighbor({7,3.2,4.7,1.4},"versicolor"));
    vecinos.push_back(new neighbor({6.4,3.2,4.5,1.5},"versicolor"));
    vecinos.push_back(new neighbor({6.9,3.1,4.9,1.5},"versicolor"));
    vecinos.push_back(new neighbor({5.5,2.3,4,1.3},"versicolor"));
    vecinos.push_back(new neighbor({6.5,2.8,4.6,1.5},"versicolor"));
    vecinos.push_back(new neighbor({6.3,3.3,6,2.5},"virginica"));
    vecinos.push_back(new neighbor({5.8,2.7,5.1,1.9},"virginica"));
    vecinos.push_back(new neighbor({7.1,3,5.9,2.1},"virginica"));
    vecinos.push_back(new neighbor({6.3,2.9,5.6,1.8},"virginica"));
    vecinos.push_back(new neighbor({6.5,3,5.8,2.2},"virginica"));
    neighbor* iris_set=new neighbor({4.86,3.28,1.4,.2},"setosa");
    neighbor* iris_vers=new neighbor({6.46,2.92,5.4,1.44},"versicolor");
    neighbor* iris_virg=new neighbor({6.4,2.98,5.68,2.1},"virginica");
    vector<neighbor*>Vectores={iris_set,iris_vers,iris_virg};
    vector<double>p1={5.4,3.9,1.7,0.04};
    vector<double>p2={5.7,2.8,4.5,1.3};
    vector<double>p3={7.6,3,6.6,2.1};

    for(auto &vecino:vecinos){
        cout<<"\nMuestra de tipo "+vecino->nombre+'\n';
        for (auto &muestras:Vectores)
        {
            double sum=dist_manh(muestras->caracteristicas,vecino->caracteristicas);
            cout<<"Distancia con "+muestras->nombre+": "<<sum<<"\n";
        }

    }




    return 0;
}

double dist_manh(const vector<double>clase,const vector<double>muestra){
    double suma=0;
    for (int i = 0; i < clase.size(); i++)
    {
        suma+=abs(clase[i]-muestra[i]);
    }
    return suma;
    
}







