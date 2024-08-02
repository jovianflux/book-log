'''
ldakfnadvdf vnfzdf
fjkfdf 
nfjaenfund

'''



class Book: 
    # pass - move on to the next line of code without error
    info = "A class to show my current read"
  
    # initialization function - whenever a new object gets created from 
    # class this function will be called
    def __init__(self, author, title, status, pages, pub_date):
        self.author = author
        self.title = title
        self.status = status
        self.pages = pages
        self.pub_date = pub_date

    def bookInfo(self):
        print(f"Author: {self.author}"
                + f"\nTitle: {self.title}"
                + f"\nStatus: {self.status}"
                + f"\nLength: {self.pages} pages"
                + f"\nPublished: {self.pub_date}")
        print("")
        
Book1 = Book("Ray Bradbury", "Now and Forever", "Complete", 209, 2007)
Book2 = Book("Gregory Benford", "Timescape", "Currently Reading", 412, 1980)
Book3 = Book("Gaston Bachelard", "The Poetics of Space", "Currently Reading", 255, 1958)

print("******July Reading stack******")
Book1.bookInfo()
Book2.bookInfo()
Book3.bookInfo()