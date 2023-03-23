class Nodo:
    def __init__(self,clave) -> None:
        self.clave=clave
        self.hijo=[]
    def C_nodo(self,clave,hijo):
        self.hijo.append(Nodo(clave))