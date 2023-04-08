from anytree import RenderTree
import Busq_prof
def print_tree( raiz:Busq_prof.Node):
    for pre, _, nodo in RenderTree(raiz):
        print("%s%s" % (pre,nodo.__str__()))
    
