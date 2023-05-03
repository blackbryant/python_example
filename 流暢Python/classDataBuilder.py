from collections import namedtuple
City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
print(tokyo)
print(tokyo.population)
for field_name in tokyo._fields:
    print(field_name)
for field_vaule in tokyo:
    print(field_vaule)



