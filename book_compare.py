#연산자 오버로딩으로 책 페이지 비교

class book:
    title = ""
    page = 0

    def __init__(self, title, page):
        self.title = title
        self.page = page

    def __str__(self):
        return self.title

    def __gt__(self, other):
        return self.page > other.page

book1 = book("magic of python", 600)
book2 = book("master of the python", 700)
print(book1 > book2)