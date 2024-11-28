from library_system import LibrarySystem

def main():
    library = LibrarySystem()

    # Add books from University Library
    library.add_book(1, "Phython Fundamentals")
    library.add_book(2, "Data Structures")
    library.add_book(3, "AI for Beginners")

    #Loan books
    library.loan_book(1,"2024-11-02")
    library.loan_book(2,"2024-11-29")

    #Return books
    library.return_book(1)
    library.process_return()

    #Search
    library.search_book(2)

    #Display Loans
    library.display_loans()
    
    if __name__ == "__main__":  
        main()