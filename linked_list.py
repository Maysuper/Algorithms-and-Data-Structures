class Node: 
    def _inti_(self, book_id): 
       self.book_id = book_id
       self.next = None


class LinkedList:
    def _init_(self):
        self.head = None
        self.tail = None

    def enqueue (self, book_id):
        new_node = Node(book_id)
        if self.tail:
            self.tail.next = new_node
        self.tail = new_node
        if not self.head:
            self . head = new_node

    def dequeue(self):
        if not self.head:
            return None
        removed = self.head.book_id
        self.head = self.head.next
        if not self.head:
            self.tail = None
        return removed
    
    def display(self):
        current = self.head
        while current:
            print(f"Book ID: {current.book_id}")
            current = current.next


