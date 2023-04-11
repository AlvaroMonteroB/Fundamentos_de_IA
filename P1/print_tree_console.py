from anytree import RenderTree
import sys
import Busq_prof

def print_tree(raiz:Busq_prof.Nodo):
    for pre, fill, node in RenderTree(raiz):
        print("%s%s" % (pre, node))

def print_tre_pre(raiz:Busq_prof.Nodo):#Impresion en preorden para ver si si se genrraba el arbol
    print(str(raiz.point.Xcoordinate)+','+str(raiz.point.Ycoordinate))
    for node in raiz.children:
        print_tre_pre(node)
    return

"""
def print_tree(raiz: Busq_prof.Node, nivel=0):
    print('    ' * nivel, end='')
    print(raiz)
    for hijo in raiz.hijo:
        print_tree(hijo, nivel + 1)
"""

def tree_to_file(raiz:Busq_prof.Nodo):
    with open("tree.txt",'w',encoding="utf-8") as f:
        sys.stdout=f
        print_tree(raiz)
        sys.stdout = sys.__stdout__