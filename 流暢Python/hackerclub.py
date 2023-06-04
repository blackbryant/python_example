from dataclasses import dataclass
from dataclasses import dataclass, field
import dataclasses

'''
@dataclass
class ClubMember:
 name: str=""
 guests: list = field(default_factory=list)
 athlete: bool = field( default=False, repr=False)

@dataclass
class HackerClubMember(ClubMember): 
 all_handles = set() 
 handle: str = '' 
 def __post_init__(self):
    cls = self.__class__ 
    if self.handle == '': 
        print(self.name)
        self.handle = self.name
    if self.handle in cls.all_handles: 
        msg = f'handle {self.handle!r} already exists.'
        raise ValueError(msg)
    cls.all_handles.add(self.handle)

club = ClubMember("sport soccer",['jack','john'],True)
hack = HackerClubMember(club)
'''

from dataclasses import dataclass, field
from typing import Optional
from enum import Enum, auto
import datetime
class ResourceType(Enum): 
 BOOK = auto()
 EBOOK = auto()
 VIDEO = auto()




@dataclass
class Resource:
 identifier: str 
 title: str = '<untitled>' 
 creators: list[str] = field(default_factory=list)
 date: Optional[date] = None 
 type: ResourceType = ResourceType.BOOK 
 description: str = ''
 language: str = ''
 subjects: list[str] = field(default_factory=list)

 
description = 'Improving the design of existing code'
book=Resource('978-0-13-475759-9', 'Refactoring, 2nd Edition',['Martin Fowler', 'Kent Beck'], datetime.date(2018, 11, 19),ResourceType.BOOK, description, 'EN',['computer programming', 'OOP'])
print(book)

aa = dataclasses.replace(book,title="1234")
print(aa.__repr__)





import typing
class City(typing.NamedTuple):
 continent: str
 name: str
 country: str
cities = [
 City('Asia', 'Tokyo', 'JP'),
 City('Asia', 'Delhi', 'IN'),
 City('North America', 'Mexico City', 'MX'),
 City('North America', 'New York', 'US'),
 City('South America', 'São Paulo', 'BR'),
]



def match_asian_cities():
 results = []
 for city in cities:
    match city:
        case City(continent='Asia'):
            results.append(city)
 return results
#[City(continent='Asia', name='Tokyo', country='JP'), City(continent='Asia', name='Delhi', country='IN')]
resulta = match_asian_cities()
print(resulta)

def match_asian_countries2():
 results = []
 for city in cities:
    match city:
        case City(continent='Asia', country=country):
            results.append(country)
 return results
#['JP', 'IN']
resultb = match_asian_countries2()
print(resultb)
print(City.__match_args__)

def match_asian_cities_pos():
 results = []
 for city in cities:
    match city:
        case City('Asia'):
            results.append(city)
 return results
resultb = match_asian_cities_pos()
print(resultb)


def match_asian_countries_pos():
 results = []
 for city in cities:
    match city:
        case City('Asia', _, country):
            results.append(country)
 return results

resultb = match_asian_countries_pos()
print(resultb)










































