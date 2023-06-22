# 撲克牌
#
import collections
from random import choice
from math import hypot

#定義一個類別，裡面有兩個欄位
Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    #class init
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]
    #return lenght of the _cards
    def __len__(self):
        return len(self._cards)

    #return value of the _cards
    def __getitem__(self, position):
        return self._cards[position]
    

beer_card = Card('7','diamonds')
beer_card
print(beer_card)
deck = FrenchDeck()
print(len(deck))

print(choice(deck))
print(choice(deck))
print(deck[:3])

for card in deck:
    print(card)

#二維向量
class Vector:

    def __init__(self,x=0,y=0) -> None:
        self.x = x
        self.y = y 
    
    def __repr__(self) -> str:
        return "Vector(%r, %r)" %(self.x,self.y)
    
    def __abs__(self):
        return hypot(self.x,self.y)
    
    def __bool__(self):
        return bool(abs(self))
    
    def __add__(self,other):
        x= self.x + other.x
        y = self.y + other.y
        return Vector(x,y)

    def __mul__(self,scalar):
        return Vector(self.x*scalar, self.y*scalar)



v1 = Vector(1,2)
v2 = Vector(2,1)
print(v1+v2)
