print("=================================================================")
print("=================Heramienta de edicion de mapas==================")
print("=================================================================")
read_matrix=list()
matrix_rows1=list()
with open("matriz.txt","r+") as write_matrix:
    leer=write_matrix.readline
    for line in write_matrix:
        read_matrix.append(line)
    read_matrix.close()

 