class Book:
    def __init__(self):
        self.title = ""
        self.author = "Me"
        self.year = 2000
        self.words = 1000
        self.numPages = 300
    
    def displayDetails(self):
        return f"""Title: {title}
Author: {self.author}
Year: {self.year}
Number of Pages: {self.numPages}"""

    def rateBook(rating):
        self.rating = rating
    
    def reviewBook(self, review):
        self.review = review

class Novel(Book):
    def __init__(self):
        self.genre = "Crime Fiction"
        self.numChapters = 20
    
    def calcReadTime(self, readSpeed):
        return self.words * readSpeed

class Magazine(Book):
    def __init__(self):
        self.issueNumber = 69
        self.numArticles = 20
        self.articles = {}
    
    def getArticleByTitle(self, title):
        return self.articles[title]