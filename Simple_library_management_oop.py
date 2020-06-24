"""
 LIBRARY MANAGEMENT SYSTEM - 2 classes & main class
"""


class Library:
    def __init__(self,books_available):
        self.books_available = books_available
        
    def display_books_available(self):
        print('The books available in library are')
        for book in self.books_available:
            print(book)

    def issue_book(self,book_requested):
        if book_requested in self.books_available:
            print('The copy of book is available.You can now issue the book')
        else:
            print('The copy of this book is not available at the moment.')
            
    def add_book(self,book_return):
        self.books_available.append(book_return)
        print('The book has been returned back.Thank You.')
        
    def sys_exit(self):
        print('Logged Out.Thank you for visiting.')
    
class student:
    def book_request(self):
        print('Enter the book title you would like to check out')
        self.book = input()
        return self.book
    
    def book_return(self):
        print('Enter the book title you would like to return back')
        self.book = input()
        return self.book
    
def main():
    li = Library(['Microprocessor_godse','Verilog_palnitkar','Cmos_kang'])
    student1 = student()
    #OK = False
    while True:
        print("""
              __WELCOME TO CENTRAL LIBRARY__
              
              Select the required:
                  
                  1. List of available books.
                  2. Issue a book.
                  3. Return a book.
                  4. EXIT.
                  """)
        break
        continue
    choice = int(input('Enter your choice.     '))
    if choice == 1:
        li.display_books_available()
    elif choice == 2:
        li.issue_book(student1.book_request())
    elif choice == 3:
        li.add_book(student1.book_return())
    elif choice == 4:
        li.sys_exit()
                  
    
main()
    
    
    
    
    
    
    
    
    
    
