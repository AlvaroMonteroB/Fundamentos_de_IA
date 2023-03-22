import threading
import display_graphics
import Read_data


C_ini,C_fin=list()
Matrix=Read_data.read_matrix()#arreglo de puntos AKA objetos
Coo1=input("Enter begin coordinate (x,y)\n")
Coo2=input("Enter end coordinate (x,y)\n")
Coo1.replace(',','')
Coo2.replace(',','')
C_ini.append(int(Coo1[0]))
C_ini.append(int(Coo1[1]))
C_fin.append(int(Coo2[0]))
C_fin.append(int(Coo2[1]))

#===========================================================================
#===================================MENÚ====================================
#===========================================================================
print("Choose a character\n")
opt=input("Options  1.-   2   3   4   5")
if opt==1:
    elif opt==2:
        
    elif opt==3:
    
    elif opt==4:




