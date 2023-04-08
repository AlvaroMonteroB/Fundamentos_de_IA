from anytree import RenderTree
import Busq_prof
def print_tree( raiz:Busq_prof.Node):
    for pre, _, raiz in RenderTree(raiz):
        print("%s%s" % (pre,node))
    
    
