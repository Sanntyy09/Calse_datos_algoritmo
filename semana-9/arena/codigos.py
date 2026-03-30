
####### LCA(Lowest Common Ancestor 
def lca(root, v1, v2):
    while root:
        if v1 < root.info and v2 < root.info:
            root = root.left
        elif v1 > root.info and v2 > root.info:
            root = root.right
        else:
            return root


  ####### ALTURA DEL ÁRBOL
  def height(root):
    if root is None:
        return -1
    
    left_h = height(root.left)
    right_h = height(root.right)
    
    return 1 + max(left_h, right_h



    ###### VALIDAR BST
 def check_binary_search_tree_(root):

    def validar(nodo, minimo, maximo):
        if nodo is None:
            return True
        
        if nodo.data <= minimo or nodo.data >= maximo:
            return False
        
        return (validar(nodo.left, minimo, nodo.data) and
                validar(nodo.right, nodo.data, maximo))
    
    return validar(root, float('-inf'), float('inf'))
 
