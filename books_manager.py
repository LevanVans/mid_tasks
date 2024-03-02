
import datetime

class Book:
    
    def __init__(self, title, author, year) -> None:
        
        self.title = title
        self.author = author
        self.year = year
        
        
    
class BookManager:
    
    def __init__(self) -> None:
        self.books = []



    def add_book(self, title, author, year):
        
        book = Book(title, author, year)
        self.books.append(book)
        
    def get_all_books(self):
        
        for book in self.books:
            print(f"\n Title: {book.title}, Author: {book.author}, Year: {book.year} \n ")
            
    def search_book(self, title):
        
        
        for book in self.books:
            if book.title.lower() == title.lower():
                
                print(f"\n Title: {book.title}, Author: {book.author}, Year: {book.year} \n")
               
                return
            
            print("No Such Book Found ")
               
  
book_manager = BookManager()

while True:
    
    print("1 - To Add a book")
    print("2 - Get all books")
    print("3 - Search book by title")
    print("0 to Exit")

    try: 
        
        choise = int(input("Choise 1-3 : "))
        
    except:
        
        print("Wrong Input , Try Again")
        continue
        
    if choise == 1: 
        
        
        
        title = input("Enter title: ").strip()
        author = input("Enter the author: ").strip()
        
        while True:
            year = input("Enter the year : ").strip()
            
        
            try:
                
                int(year)
            
            except:
                
                print("\n Year must be number \n ")
                continue
            
            if  int(year) > datetime.date.today().year:
                
    
                
                print("Year Could not be more than current year ")
                               
                continue
            
            else:
                
                break
                 
        
        book_manager.add_book(title, author, year)
    
        print(" \n Book added successfully. \n ")   
    
    
    elif  choise == 2:
        print("\n Books in Library : \n")
        book_manager.get_all_books()
        
        
    elif choise == 3 :
        
        title = input(" \n Enter The Title to Search : \n ").strip()
        
        book_manager.search_book(title)        
        
    elif choise == 0:
        
        break
    
    else : 
        print("Wrong Input") 
        continue


