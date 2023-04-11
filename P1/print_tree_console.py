from anytree import RenderTree
import sys
import Busq_prof

def print_tree(raiz:Busq_prof.Nodo):
    for pre, fill, node in RenderTree(raiz):
        print("%s%s" % (pre, node))



def tree_to_file(raiz:Busq_prof.Nodo):
    with open("tree.txt",'w',encoding="utf-8") as f:
        sys.stdout=f
        print_tree(raiz)
        sys.stdout = sys.__stdout__