# Book Checkout Create a class LibraryBook. 
# The constructor takes title and initializes self.is_checked_out to False. 
# Add a method checkout() that sets self.is_checked_out to True but only if it is currently False.

class LibraryBook:
    def __init__(self,title):
        self.title=title
        self.is_checked_out=False
    def checkout(self):
        if self.is_checked_out==True:
            print(f"The {self.title} Book is checked out")
        else:
            print(f"The {self.title} book is checked out alredy")
book=LibraryBook("Athadu Adavini Jayinchadu")
book.checkout()

        
