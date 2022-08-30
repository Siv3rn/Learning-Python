class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
        

    def addtail(self,data):
        dataBaru  = node(data)
        dataBaru.next = None
        if self.head == None:
            self.head = dataBaru
            self.tail = dataBaru
        else:
            self.tail.next = dataBaru
            self.tail = dataBaru

    def addhead(self, data):
        dataBaru  = node(data)
        if self.head == None:
            self.head = dataBaru
            self.tail = dataBaru
        else:
            dataBaru.next = self.head
            self.head = dataBaru

    def removehead(self):
        if self.head == None:
            print("error")
        elif self.head == self.tail or  self.head.next==None:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next


    def display(self):
        p = self.head
        while p != None:
            print(p.data)            
            p = p.next
        
    def length(self):
        p = self.head
        n = 0
        while p != None:
            n += 1
            p = p.next
        print(n)

    def isthere(self, data):
        p = self.head
        while p != None:
            if p.data == data:
                return True
            p = p.next
        return False
    def insertKe2(self,data):
        dataBaru = node(data)
        dataBaru.next = self.head.next
        self.head.next = dataBaru

    def reverse(self):
        p = self.head
        prev = p.prev
        while p != None:
            next = p.next
            p.next = prev
            prev = p
            p = next
        self.head = prev
    
    def removeTail(self):
        if self.head == None:
            return None
        elif self.head.next == None:
            self.head = None
            return None
        second_last = self.head
        while(second_last.next.next != None):
            second_last = second_last.next
        second_last.next = None
    




linked = linkedlist()

linked.display()
print("-------------")
linked.removeLastNode()
linked.display()
