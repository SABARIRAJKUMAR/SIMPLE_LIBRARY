class library:
    def __init__(self, books):
        self.books = books

    def list_books(self):
        print("available books")
        for book in self.books:
            print(book)

    def borrow_books(self, borrow_books):
        if borrow_books in self.books:
            print("get your books now")
            self.books.remove(borrow_books)
        else:
            print("book not available")

    def receive_book(self, receive_books):
        print("you have returned the book")
        self.books.append(receive_books)


books = ['c', 'c++', 'java', 'python', 'javascript', 'html', 'css', 'php']
o = library(books)

msg = """
     1.display books
     2.borrow books
     3.return books
     4.exit
"""
while True:
    print(msg)
    ch = int(input("enter your choice :"))
    if ch == 1:
        o.list_books()
    elif ch == 2:
        book = input("enter book name to borrow :")
        o.borrow_books(book)
    elif ch == 3:
        book = input("enter book name to return :")
        o.receive_book(book)
    else:
        print("thank you come again")
        quit()
#code with ❤ by SABARIRAJKUMAR️
