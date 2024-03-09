#!/usr/bin/env python3
# class TestShoe:
#     '''Shoe in shoe.py'''

#     def test_has_brand_and_size(self):
#         '''has the brand and size passed to __init__, and values can be set to new instance.'''
#         stan_smith = Shoe("Adidas", 9)
#         assert(stan_smith.brand == "Adidas")
#         assert(stan_smith.size == 9)

#     def test_requires_int_size(self):
#         '''prints "size must be an integer" if size is not an integer.'''
#         stan_smith = Shoe("Adidas", 9)
#         captured_out = io.StringIO()
#         sys.stdout = captured_out
#         stan_smith.size = "not an integer"
#         sys.stdout = sys.__stdout__
#         assert captured_out.getvalue() == "size must be an integer\n"

#     def test_can_cobble(self):
#         '''says that the shoe has been repaired.'''
#         stan_smith = Shoe("Adidas", 9)
#         captured_out = io.StringIO()
#         sys.stdout = captured_out
#         stan_smith.cobble()
#         sys.stdout = sys.__stdout__
#         assert(captured_out.getvalue() == "Your shoe is as good as new!\n")
    
#     def test_cobble_makes_new(self):
#         '''creates an attribute on the instance called 'condition' and set equal to 'New' after repair.'''
#         stan_smith = Shoe("Adidas", 9)
#         stan_smith.cobble()
#         assert(stan_smith.condition == "New")
        
        
   


class Shoe:
    def __init__(self,brand="Adidas",size=7) :
        self.brand=brand
        self.size=size
        

    @property
    def brand(self):
        return self._brand
    
    @brand.setter
    def brand(self,brand):
        self._brand=brand

    @property 
    def size(self):
        return self._brand
    
    @size.setter
    def size(self,size):
        if isinstance(size,int):
            self._size=size
        else:
            print("size must be an integer")

    def cobble(self):        
        print("Your shoe is as good as new!")
        self.condition="New"

    #@property
    # def condition(self):
    #     print("Your shoe is as good as new")
    #     return self._condition
    
    # @condition.setter
    # def condition(self,condition="New"):
    #     self._condition=condition
        

Adidas=Shoe("Puma",10)
print(Adidas._brand)
print(Adidas.cobble())



               
       