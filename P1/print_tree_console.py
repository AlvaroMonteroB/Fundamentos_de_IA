from anytree import RenderTree

import Busq_prof

def print_tree(raiz:Busq_prof.Nodo):
    for pre, fill, node in RenderTree(raiz):
        print("%s%s" % (pre, node))

def print_tre_pre(raiz:Busq_prof.Nodo):#Impresion en preorden para ver si si se genrraba el arbol
    print(str(raiz.point.Xcoordinate)+','+str(raiz.point.Ycoordinate))
    for node in raiz.hijo:
        print_tre_pre(node)
    return

"""
def print_tree(raiz: Busq_prof.Node, nivel=0):
    print('    ' * nivel, end='')
    print(raiz)
    for hijo in raiz.hijo:
        print_tree(hijo, nivel + 1)
"""