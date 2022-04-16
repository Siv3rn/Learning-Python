class Heap:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.storage = [0]*capacity

    def getparent(self,idx):
        return (idx-1)//2
        

    def getleftchild(self,idx):
        return (idx*2)+1

    
    def getrightchild(self,idx):
        return (idx*2)+2

    def hasparent(self,idx):
        return self.getparent(idx) >= 0

    
    def hasleft(self,idx):
        return self.getleftparent(idx) < self.size


    def hasright(self,idx):
        return self.getrightparent(idx) < self.size


    def isfull(self):
        return self.size >= self.capacity
    

    def swap(self, idx,idy):
        temp = self.storage[idx]
        self.storage[idx] = self.storage[idy]
        self.storage[idy] = temp


    def heapifyup(self,index):
        if self.hasparent(index) and self.storage[index] < self.storage[self.getparent(index)]:
            self.swap(index, self.getparent(index))
            self.heapifyup(self.getparent(index))

    def insert(self, data):
        if self.isfull():
            raise ("the heap is full")
        for i in range(self.size):
            if self.storage[i] == data:
                return
        self.storage[self.size] = data
        self.size += 1
        self.heapifyup(self.size - 1)
    
    def print(self):
        print(self.storage)


def build_tree(elemen):
    root = Heap(len(elemen))
    for i in range(len(elemen)):
        root.insert(elemen[i])
    return root

def main():
    heap = [4,8,0,4,0,2]
    heap_tree = build_tree(heap)
    niu = [1,9,6,2,9]
    niu_tree = build_tree(niu)
    heap_tree.print()
    niu_tree.print()

if __name__ == '__main__':
    main()


