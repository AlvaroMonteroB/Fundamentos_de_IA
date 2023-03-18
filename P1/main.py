import ctypes         #g++ -fPIC -shared -o Data_read.so data_read.cpp
Open_file = ctypes.CDLL("D:/Repositorios/Fundamentos_de_IA/P1/Data_read.so")#matrix read in c++ with headers                                                         #to calculate the size

Matrix=Open_file.matrix("matriz.txt")
