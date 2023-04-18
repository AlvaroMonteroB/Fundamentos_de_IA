import Busq_prof as bp
from anytree import PostOrderIter
from anytree import PreOrderIter

def list_tree(raiz:bp.Nodo):
    Lista=[]
    for node in PreOrderIter(raiz):
        Lista.append(node.point)
        
    return Lista


