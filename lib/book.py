#!/usr/bin/env python3

#from typing import Self

# class TestBook:
#     '''Book in book.py'''

#     def test_has_title_and_page_count(self):
#         '''has the title and page_count passed into __init__, and values can be set to new instance.'''
#         book = Book("And Then There Were None", 272)
#         assert(book.page_count == 272)
#         assert(book.title == "And Then There Were None")

#     def test_requires_int_page_count(self):
#         '''prints "page_count must be an integer" if page_count is not an integer.'''
#         book = Book("And Then There Were None", 272)
#         captured_out = io.StringIO()
#         sys.stdout = captured_out
#         book.page_count = "not an integer"
#         sys.stdout = sys.__stdout__
#         assert captured_out.getvalue() == "page_count must be an integer\n"

#     def test_can_turn_page(self):
#         '''outputs "Flipping the page...wow, you read fast!" when method turn_page() is called'''
#         book = Book("The World According to Garp", 69)
#         captured_out = io.StringIO()
#         sys.stdout = captured_out
#         book.turn_page()
#         sys.stdout = sys.__stdout__
#         assert(captured_out.getvalue() == "Flipping the page...wow, you read fast!\n")


class Book:
    def __init__(self,title="How ",page_count=9) :
        self._title=title
        self._page_count=page_count
        # if not isinstance(page_count,int):
        #      print(ValueError("Page_count must be an integer"))
        # else:self.page_count=page_count

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self,title):
      self._title=title

    @property   
    def page_count(self):
        return self._page_count
        
    @page_count.setter
    def page_count(self,page_count):
        if not isinstance(page_count,int):
             print(ValueError("page_count must be an integer"))
        else:self._page_count=page_count

    def turn_page(self):
     print("Flipping the page...wow, you read fast!")
     return "Flipping the page...wow, you read fast!"
    
    #page_count=property(get_page_count)
# Rails=Book("And Then There Were None","272")
# print(Rails.page_count,Rails.title)
# print(Rails.turn_page())