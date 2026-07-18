# #1 მინი-ბიბლიოთეკა
# --------------------
# თქვენი მიზანია შექმნათ „მინი-ბიბლიოთეკის მართვის სისტემა“, სადაც:
# - მომხმარებელს შეუძლია დაამატოს წიგნი (სათაური, ავტორი, წელი)
# - შეინახოს ისინი სიაში
# - მოძებნოს წიგნი სათაურით
# - დაინახოს ყველა წიგნის სია (სათაური + ავტორი)
# დეტალები:
# -----------
# 1. შექმენით წინასწარი "სია" სადაც მოთავსებული იქნება 10 თქვენს მიერ არჩეული
# წიგნის სახელი/ავტორი და წელი
# 2. მომხმარებელს აქვს საშუალება: წიგნი დაამატოს ამ ფორმატით სახელი/ავტორი
# და წელი
# 3. მომხმარებელს აქვს საშუალება: ნახოს უკვე არსებული წიგნები რაც
# ბიბლიოთეკაშია (10 წიგნი)
# 4. აირჩიოს მისთვის სასურველი და გაიტანოს ბიბლიოთეკიდან "წასაკითხად"
# 5. მომხმარებლის მიერ დამატებული წიგნი უნდა დაემატოს ბიბლიოთეკის სიას და
# მომდევნო გამოძახებაზე 10-ის მაგივრად უნდა გამოჩნდეს 11 და ა.შ. სანამ
# მომხმარებელი დაამატებს წიგნებს
# 6. ვალიდაცია არაა საჭირო lower/upper და ა.შ. (მომხმარებელს ყოველთვის შეჰყავს
# სწორი ინფორმაცია)#2 პროგრამა "21" ქულა



class MiniLibrary:
    def __init__(self, *args , **kwargs):
        self._books = kwargs
    
    def get_book(self, title : str):
        
        return print(self._books.pop(title))
    
    def add_book(self, title, auth, year):
        
        title2 = MiniLibrary.cleaner(title)
        self._books[title2] = {'title' : title,
                              'author' : auth,
                              'year' : year}
        
        return print('თქვენი წიგნი წარმატებით დაემატა')
    
    def __str__(self):
        result = "Library:\n"

        for book in self._books.values():
            result += (
                f"Title : {book['title']}\n"
                f"Author: {book['author']}\n"
                f"Year  : {book['year']}\n"
                "--------------------\n"
            )
        return result
    
    @staticmethod
    def cleaner(word):
        return word.strip().lower().replace(" ", "")
    

books = {
    "tokillamockingbird": {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "year": 1960
    },
    "1984": {
        "title": "1984",
        "author": "George Orwell",
        "year": 1949
    },
    "thegreatgatsby": {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "year": 1925
    },
    "prideandprejudice": {
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "year": 1813
    },
    "thehobbit": {
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "year": 1937
    },
    "thecaatcherintherye": {
        "title": "The Catcher in the Rye",
        "author": "J.D. Salinger",
        "year": 1951
    },
    "bravenewworld": {
        "title": "Brave New World",
        "author": "Aldous Huxley",
        "year": 1932
    },
    "thealchemist": {
        "title": "The Alchemist",
        "author": "Paulo Coelho",
        "year": 1988
    },
    "thelittleprince": {
        "title": "The Little Prince",
        "author": "Antoine de Saint-Exupéry",
        "year": 1943
    },
    "harrypotterandthephilosopher'sstone": {
        "title": "Harry Potter and the Philosopher's Stone",
        "author": "J.K. Rowling",
        "year": 1997
    }
}
library1 = MiniLibrary(**books)

while True:
    welcome = input('hello, please enter service Get book / Add Book \n for cancel write c')

    if MiniLibrary.cleaner(welcome) == 'getbook':
        while True:
            title = input(f'please choose book / for cancel type c : \n {library1} : ')
            title = MiniLibrary.cleaner(title)


            if title in library1._books:
                library1.get_book(title=title)
                anothertry =MiniLibrary.cleaner(input('do you need any more book y/n:'))

                if anothertry == 'y':
                    continue
                elif anothertry == 'n':
                    break
                else:
                    print('try again : out of books')
                    break

            elif  MiniLibrary.cleaner(title) == 'c':
                break

            elif title not in library1._books:
                print('book not found')
                continue

        
    if MiniLibrary.cleaner(welcome) == 'addbook':
        while True:
            auth  = input('author: ')
            year  = int(input('year: '))
            title = input('title:')
            library1.add_book(title=title, auth=auth, year=year)

            anothertry = input('do you want to add another book y/n:')

            if anothertry == 'y':
                continue
            if anothertry == 'n':
                break

        
    if MiniLibrary.cleaner(welcome) == 'c':
        break

