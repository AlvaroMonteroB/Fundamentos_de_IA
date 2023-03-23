import Agentes as Ag
import various_methods as V_M
class Nodo:
    def __init__(self,clave) -> None:
        self.clave=clave
        self.hijo=[]
    def C_nodo(self,clave,hijo):
        self.hijo.append(Nodo(clave))