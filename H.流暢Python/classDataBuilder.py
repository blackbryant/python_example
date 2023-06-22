from collections import namedtuple
print("===========AAAAAAAAAAAAAAA=========")
Coordinate = namedtuple('Coordinate', 'lat lon')
print(issubclass(Coordinate, tuple))
moscow = Coordinate(55.756, 37.617)
moscow2 = Coordinate(55.756, 37.617)
print(id(moscow))
print(id(moscow2))
print(moscow == moscow2)


print("====================")
Card = namedtuple('Card', ['rank', 'suit'])
class FrenchDeck:
 ranks = [str(n) for n in range(2, 11)] + list('JQKA')
 suits = 'spades diamonds clubs hearts'.split()
 def __init__(self):
    self._cards = [Card(rank, suit) for suit in self.suits
 for rank in self.ranks]
 def __len__(self):
    return len(self._cards)
 def __getitem__(self, position):
    return self._cards[position]
Card.suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0) 
def spades_high(card):
   print("rank:"+card.rank+"rank_value:"+str(FrenchDeck.ranks.index(card.rank)))
   rank_value = FrenchDeck.ranks.index(card.rank)
   suit_value = card.suit_values[card.suit]
   return rank_value * len(card.suit_values) + suit_value
Card.overall_rank = spades_high
lowest_card = Card('2', 'clubs')
highest_card = Card('A', 'spades')
print(lowest_card.overall_rank() )
print(highest_card.overall_rank() )

 


City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
print(tokyo)
print(tokyo.__repr__)
print(tokyo.population)
for field_name in tokyo._fields:
    print(field_name)
for field_vaule in tokyo:
    print(field_vaule)
print(tokyo._asdict())
from collections import OrderedDict
print(OrderedDict(tokyo._asdict()))

#
print("=========typingtyping===========")
from typing import NamedTuple
class Coordinatet(NamedTuple):
    lat: float
    lon: float
    def __str__(self):
        ns = 'N' if self.lat >= 0 else 'S'
        we = 'E' if self.lon >= 0 else 'W'
        return f'{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}'
coord01 = Coordinatet(lon=20,lat=10)
print(coord01)
coord02 = Coordinatet(lon=40,lat=20)
coord01 = coord01._replace(lon=100)
print(coord01)
print(coord02)


trash = Coordinate('Ni!', None)
print(trash)
class DemoNTClass(NamedTuple):
 a: int 
 b: float = 1.1 
 c = 'spam' 

nt = DemoNTClass(8)
print(nt.a)

from dataclasses import dataclass, field
@dataclass
class ClubMember:
 name: str
 guests: list[str] = field(default_factory=list)

club = ClubMember( name="aa",guests=['a','b','c'])
print(club)
print(type(club.guests[0] ))

from dataclasses import dataclass
@dataclass
class DemoDataClass:
 a: int 
 b: float = 1.1 
 c = 'spam' 
dc = DemoDataClass(9)
dc.a = 10
dc.b = 'oops'
dc.c = 'whatever'
dc.z = 'secret stash'
print(dc.a)
print(dc.b)
print(dc.c)
print(dc.z)

print("=========183183===========")
from dataclasses import fields
import dataclasses

@dataclass
class ClubMember:
 name: str
 guests: list = field(default_factory=list)
 athlete: bool = field(default=None, repr=False)

aaa = ClubMember("Beer",["a","b"])
print(aaa.name)
print(aaa.guests)
print(aaa.athlete == dataclasses.MISSING)

@dataclass  
class Product:
    name: str
    price: int
    qty: int
    weight: float = field(default=0.0, repr=False)
    amount: int = field(init=False)
    def __post_init__(self):
        self.amount = self.price * self.qty
itemA = Product(name="itemA", price=100, qty=10)
itemB = Product(name="itemA", price=100, qty=10)
print(itemA)
print(itemA == itemB)









