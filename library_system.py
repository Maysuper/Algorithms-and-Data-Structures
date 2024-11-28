from hash_table import HashTable
from min_heap import MinHeap
from linked_list import LinkedList


class LibrarySystem:
    def _init_(self):
        # combines HashTable, MinHeap and LinkedList
        self.catalog = HashTable()
        self.loan_manager = MinHeap()
        self.return_queue = LinkedList()

    def add_book(self, book_id, book_title):
        self.catalog.insert(book_id, book_title)
        print(f"Added book: {book_title} (ID: {book_id})")

    def search_book(self, book_id):
        book = self.catalog.search(book_id)
        print(f"Book found: {book}" if book else "Book not found")
        return book
    
    def loan_book(self, book_id, due_date):
        self.loan_manager.insert(due_date, book_id)
        print(f"Loaned book (ID: {book_id}) added to return queue")

    def process_return(self):
        book_id = self.return_queue.dequeue()
        if book_id:
            print(f"Processed return for book (ID: {book_id})")
        else:
            print("No books to process")

    def display_loans(self):
        print("Loans:")
        self.loan_manager.display()