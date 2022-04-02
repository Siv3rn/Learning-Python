
class BST:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

    def add_child(self,data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BST(data)

        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BST(data)

    def in_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.in_order_traversal()
        
        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal() 

        return elements


    def post_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.post_order_traversal()
        
        if self.right:
            elements += self.right.post_order_traversal() 
        
        elements.append(self.data)

        return elements

    def pre_order_traversal(self):
        elements = []
        elements.append(self.data)

        if self.left:
            elements += self.left.pre_order_traversal()
        
        if self.right:
            elements += self.right.pre_order_traversal() 

        return elements
        

    def search(self,data):
        if self.data == data:
            return True

        elif data < self.data:
            if self.left:
                return self.left.search(data)
            else:
                return False
            
        elif data > self.data:
            if self.right:
                return self.right.search(data)
            else:
                return False
    def findmin(self):
        current = self
        while current.left:
            current = current.left
        return current.data


    def findmax(self):
        current = self
        while current.right:
            current = current.right
        return current.data
    

def build_tree(elemen):
    root = BST(elemen[0])

    for i in range(1,len(elemen)):
        root.add_child(elemen[i])
    
    return root

def main():
    number = [5,3,1,4,8,9,10]
    number_tree = build_tree(number)

    print(number_tree.in_order_traversal())


if __name__ == '__main__':
    main()
