# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 22:34:43 2024

@author: demar
"""

class Book():
    def __init__(self, t = "no book", w = 0):
        self.title = t
        self.weight = w
        
    def __str__(self):
        return self.title
    
    
class ForSaleBook(Book):
    def __init__(self, t = "no book", w = 0, p = 0.0):
        Book.__init__(self, t, w)
        self.price = p
        
    def __str__(self):
        return f'{self.title:s} (${self.price:.2f})'
    
    
class ExaminationCopy(Book):
    def __init__(self, t = "no book", w = 0, r = "no recevier"):
        Book.__init__(self, t, w)
        self.receiver = r
        
    def __str__(self):
        return f'{self.title:s} ({self.receiver:s})'
    

class Box():
    content = []
    
    
    def __init__(self, iden = 0, c = 0):
        self.ID = iden
        self.capacity = c
        
        
    def __str__(self):
        return str(self.ID)
    
    
    def total_weight(self):
        tweight = 0.0
        for b in Box.content:
            tweight += b.weight
        return tweight
        #another way:
        #return sum(b.weight for b in Box.content)
    
    
    def add_book(self, bk):
        if (bk.weight + self.total_weight()) > self.capacity:
            raise ValueError("Capacity of " + str(self.ID) + " exceeded.")
        else:
            Box.content.append(bk)
            
            
    def print_content(self):
        for b in Box.content:
            print(b)
            
            
if __name__ == '__main__':
    fs_bk = ForSaleBook('MobyDick', 3.5, 12.50)
    print(str(fs_bk) + ' has weight ' + str(fs_bk.weight) + ' pounds.')
    ex_cp = ExaminationCopy('Little Women', 2.7, 'Fred')
    print(str(ex_cp) + ' has weight ' + str(ex_cp.weight) + ' pounds.')
    print('-' * 40)
    bx = Box(12, 10.0)
    bx.add_book(fs_bk)
    bx.add_book(ex_cp)
    bx.add_book(ForSaleBook('Catch 22', 3.2, 10.75))
    bx.print_content()
    try:
        bx.add_book(ExaminationCopy('Networks: An Introduction', 3.7, 'Al'))
    except ValueError as detail:
        print(detail)

    
        