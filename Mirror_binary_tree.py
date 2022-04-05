#pertama tama buat class untuk binary tree
class BST:
    #init sebuah class dan data
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None
    #dalam fungsi digunakan untuk menambah data kedalam binary tree
    def add_child(self,data):
        #jika ada data yang sama tidak usah di masukkan lagi
        if data == self.data:
            return
        #jika data lebih besar dari data sebelumnya taruh di kiri
        if data > self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BST(data)
        # jika lebih kecil taruh di kanan
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BST(data)

    def in_order_traversal(self):
        elements = []
        #kunjungi dulu node yang berada di kiri sampai mentok
        if self.left:
            elements += self.left.in_order_traversal()
        #append data ke elements
        elements.append(self.data)
        #setelah itu baru append node yang ada di kanan
        if self.right:
            elements += self.right.in_order_traversal() 
        #outputkan element yang sudah di append barusan
        return elements


    def post_order_traversal(self):
        elements = []
        #kunjungi dulu node yang berada di kiri dan kanan
        if self.left:
            elements += self.left.post_order_traversal()
        
        if self.right:
            elements += self.right.post_order_traversal() 
        #append data ke elements
        elements.append(self.data)
        #outputkan element yang sudah di append barusan
        return elements

    def pre_order_traversal(self):
        elements = []
        #outputkan element yang sudah di append barusan
        elements.append(self.data)
        #setelah itu baru kunjungi node kiri dan kanan
        if self.left:
            elements += self.left.pre_order_traversal()
        
        if self.right:
            elements += self.right.pre_order_traversal() 
        #outputkan element yang sudah di append barusan
        return elements


        

    

def build_tree(elemen,Jumlah_input):
    #root adalah elemen pertama yang dimasukkan dalam tree
    root = BST(elemen[0])
    #sisanya gunakan add_child untuk menambahkan data ke dalam tree
    for i in range(1,Jumlah_input):
        root.add_child(elemen[i])
    #outputkan rootnya
    return root

def main():
    n = int(input('masukkan jumlah angka :'))
    number = input('masukkan angka :').split()
    number_tree = build_tree(number,n)
    print("Pre-order:")
    print(number_tree.pre_order_traversal())
    print("In-order:")
    print(number_tree.in_order_traversal())
    print("Post-order:")
    print(number_tree.post_order_traversal())
    a = list(number_tree.in_order_traversal())

    if len(a) < 2:
        print('Tidak ada')
        
    else:    
        print("Angka Terbesar ke 2:")
        print(a[1])



if __name__ == '__main__':
    main()
