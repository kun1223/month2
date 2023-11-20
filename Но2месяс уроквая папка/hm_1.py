#№1
# class Fruits:
#     def __init__(self, name ,color, weight):
#         self.name=name
#         self.name=name
#         self.color=color
#         self.weight=weight

#     def info(self): 
#         print(f"Name-{self.name},цвет-{self.color},масса-{self.weight}")

# apple = Fruits("apple", "red", 20)
# banana= Fruits ("banana","yellow", 40)
# kivi=Fruits("kivi","green", 80)
# print(apple.info())
# print(banana.info())
# print (kivi.info())

#         #№2
# class Book:
#     def __init__(self, title, author, pages):
#             self.title=title
#             self.author=author
#             self.pages=pages

#     def chek_pages(self):
#           if self.pages <100:
#                 return "Эта книга тонкая"
#           elif 100 <=self.pages <= 300:
#                 return "это книга средние"
#           else:
#                 return "это книга толстая"
          
# book= Book("Ранние журавли", "Чынгыз Айтматов", 350)   
# print(book.chek_pages())  
        

    
#    #№доп дз
# class Book:
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.aulse:
#             return "Эта книга толстая"thor = author
#         self.pages = pages
#         self.current_page = 1 

#     def check_pages(self):
#         if self.pages < 100:
#             return "Эта книга тонкая"
#         elif 100 <= self.pages <= 300:
#             return "Эта книга средняя"
#         e

#     def turn_page(self, page_number):
#         if 1 <= page_number <= self.pages:
#             self.current_page = page_number
#             print(f"Вы на странице {self.current_page}.")
#         else:
#             print("Эта страница не существует в книге.")

# book = Book("Ранние журавли", "Чынгыз Айтматов", 99) 
# print(book.check_pages())

# book.turn_page(56) 
