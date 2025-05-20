class Book:
    def __init__(self, title: str, author: str, year: int, words: int, numPages: int):
        self.title = title
        self.author = author
        self.year = year
        self.words = words
        self.numPages = numPages
    
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
    def __init__(self, title: str, author: str, year: int, words: int, numPages: int, genre: str, numChapters: int):
        super().__init__(title, author, year, words, numPages)
        self.genre = genre
        self.numChapters = numChapters
    
    def calcReadTime(self, readSpeed):
        return self.words * readSpeed

    def displayDetails(self):  # Method override (Polymorphism)
        print(f"{self.title} by {self.author}")
        print(f"Genre: {self.genre}")
        print(f"Chapters: {self.numChapters}")

class Magazine(Book):
    def __init__(self, title: str, author: str, year: int, words: int, numPages: int, issueNumber: int, numArticles: int):
        super().__init__(title, author, year, words, numPages)
        self.issueNumber = issueNumber
        self.numArticles = numArticles
        self.articles = {}
    
    def getArticleByTitle(self, title):
        return self.articles[title]

biography = Book("Israel Irawan - An Autobiography", "Israel Irawan", 2025, 60000, 400)
biography2 = Book("Israel Irawan - The Greatest Man Who Ever Lived", 2025, 60000, 400)
mystery = Novel("The Mysterious Adventures of Israel Irawan", "Israel Irawan", 2025, 60000, 400, "Mystery", 20)
crime = Novel("The Tales of Detective Israel Irawan", "Israel Irawan", 2025, 60000, 400, "Crime Fiction", 20)
daily = Magazine("Israel Irawan Daily", "Israel Irawan", 2025, 60000, 400, 142, 40)
lifestyle = Magazine("Lifestyle by Israel Irawan", "Israel Irawan", 2025, 60000, 400, 142, 40)