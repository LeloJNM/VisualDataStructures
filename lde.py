class DoublyNode:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, value):
        new_node = DoublyNode(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def remove(self, value):
        current = self.head
        while current:
            if current.value == value:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                return
            current = current.next

    def search(self, value):
        current = self.head
        position = 0
        while current:
            if current.value == value:
                return position
            position += 1
            current = current.next
        return -1

    def insert_at(self, index, value):
        if index < 0:
            return "Índice inválido"
        new_node = DoublyNode(value)
        if index == 0:
            if not self.head:
                self.head = new_node
                self.tail = new_node
            else:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
        else:
            current = self.head
            position = 0
            while position < index and current is not None:
                position += 1
                previous_node = current
                current = current.next

            if position == index and previous_node is not None:
                previous_node.next = new_node
                new_node.prev = previous_node
                new_node.next = current

                if current is not None:
                    current.prev = new_node

                if new_node.next is None:
                    self.tail = new_node

    def remove_at(self, index):
        if index < 0 or not self.head:
            return "Índice inválido"
        
        if index == 0:
            if not self.head.next:
                self.head = None
                self.tail = None
            else:
                next_node = self.head.next
                next_node.prev = None
                self.head.next = None 
                self.head= next_node 
                
        else: 
            current= self.head 
            position= 0 
            while position < index and current is not None: 
                position += 1 
                previous_node= current 
                current= current.next 

            if position == index and previous_node is not None: 
                next_node= previous_node.next.next 

                if next_node is not None: 
                    next_node.prev= previous_node 

                previous_node.next= next_node 

                if next_node is None: 
                    tail= previous_node 
