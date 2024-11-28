import heapq

class MinHeap:
    def _int_(self):
        self.heap = []

     
    def insert(self, due_date, book_id):
        # Adds a due_book date and ID into the heap
        heapq.heappush(self.heap, (due_date, book_id))

    def get_earliest_due(self):
        return self.heap[0] if self.heap else None
    
    def remove_earliest_due(self):
        #removes the book with earliest due date
        return heapq.heappop(self.heap) if self.heap else None
    
    def display(self):
        for due_date, book_id in sorted(self.heap):
            print(f"Book ID: {book_id}, Due Date: {due_date}")