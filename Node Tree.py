

class node:
    def __init__(self,value = None):
        self.value=value
        self.left = None
        self.right = None


    def get_value(self):
        return self.value

    def set_value(self,value):
        self.value = value

    def set_right_child(self,node):
        self.right = node

    def set_left_child(self,node):
        self.left = node

    def get_right_child(self):
        return self.right

    def get_left_child(self):
        return self.left
        
    def has_left_child(self):
        return self.left != None

    def has_right_child(self):
        return self.right != None

class tree_node:
    def __init__(self,node):
        self.root = node
    
    def get_root(self):
        return self.root



    
def preorder(startnode, visit_order):
  if startnode:
    #cetak node karena pre-order maka mencetak dilakukan diawal
    visit_order = visit_order + startnode.get_value() + " "
    #jika node punya anak di kiri maka akan mengunjungi dari yang dikiri terlebih dahulu
    if startnode.has_left_child():
      visit_order = preorder(startnode.get_left_child(), visit_order) # terjadi rekursi
    #jika node yang berada dikiri sudah dikunjungi dan node mempunyai anak di kanan maka mengunjungi node yang berada di kanan
    if startnode.has_right_child():
      visit_order = preorder(startnode.get_right_child(), visit_order) # terjadi rekursi
  return visit_order
  
  
def inorder(startnode, visit_order):
  if startnode:
    #jika node punya anak di kiri maka akan mengunjungi dari yang dikiri terlebih dahulu
    if startnode.has_left_child():
      visit_order = inorder(startnode.get_left_child(), visit_order) # terjadi rekursi
    #cetak node karena in-order maka mencetak dilakukan setelah semua node yang ada dikiri telah dikunjungi
    visit_order = visit_order + startnode.get_value() + " "
    #jika node yang berada dikiri sudah dikunjungi semua selanjutnya akan mengunjungi node yang berada di kanan
    if startnode.has_right_child():
      visit_order = inorder(startnode.get_right_child(), visit_order) # terjadi rekursi
  return visit_order
  
def postorder(startnode, visit_order):
  if startnode:
    #jika node punya anak di kiri maka akan mengunjungi dari yang dikiri terlebih dahulu
    if startnode.has_left_child():
      visit_order = postorder(startnode.get_left_child(), visit_order) # terjadi rekursi
    #jika node yang berada dikiri sudah dikunjungi semua selanjutnya akan mengunjungi node yang berada di kanan
    if startnode.has_right_child():
      visit_order = postorder(startnode.get_right_child(), visit_order) # terjadi rekursi
    #cetak node apabila node adalah daun/tidak punya anak lagi
    visit_order = visit_order + startnode.get_value() + " "
  return visit_order


tree_saya = tree_node(node("Lima"))
# level 1
tree_saya.get_root().set_left_child(node("Empat"))
tree_saya.get_root().set_right_child(node("Enam"))
# level 2
tree_saya.get_root().get_left_child().set_left_child(node("Tiga"))
print("inOrder:")
print(inorder(tree_saya.get_root(), ""))
print("postOrder:")
print(postorder(tree_saya.get_root(), ""))
print("preOrder:")
print(preorder(tree_saya.get_root(), ""))