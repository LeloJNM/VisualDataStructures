class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def insert_at_position(self, value, position):
        new_node = Node(value)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            if self.tail is None:
                self.tail = new_node
        else:
            current = self.head
            for _ in range(position - 1):
                if current is None:
                    return False
                current = current.next
            if current is None:
                return False
            new_node.next = current.next
            current.next = new_node
            if new_node.next is None:
                self.tail = new_node

    def remove(self, value):
        if self.head is None:
            return
        if self.head.value == value:
            self.head = self.head.next
            if self.head is None or self.head.next is None:
                self.tail = self.head
            return
        current = self.head
        while current.next and current.next.value != value:
            current = current.next
        if current.next is not None:
            current.next = current.next.next
            if current.next is None:
                self.tail = current

    def remove_at_position(self, position):
        if position == 0 and self.head is not None:
            removed_value = self.head.value
            self.head = self.head.next
            if self.head is None or self.head.next is None:
                self.tail = self.head
            return removed_value
        else:
            current = self.head
            for _ in range(position - 1):
                if current is None:
                    return None
                current = current.next
            if current is None or current.next is None:
                return None
            removed_value = current.next.value
            current.next = current.next.next
            if current.next is None:
                self.tail = current

    def search(self, value):
        current = self.head
        position = 0
        while current:
            if current.value == value:
                return position
            position += 1
            current = current.next
        return -1

