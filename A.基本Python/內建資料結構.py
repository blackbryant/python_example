
lista = ['a','b','c']
mappinga ={} 
for i ,value in enumerate(lista):
    print(f"{i}-{value}")
for i ,value in enumerate(lista):
    mappinga[i] =value
print(mappinga)

sorted([7,6,5,3,2,1])
print(sorted([7,6,5,3,2,1]))
#zip
seq01= ['a','b','c']
seq02= ['apple','banana','cream']
zipped = zip(seq01,seq02)
print(list(zipped))
# that zip is an iterator which stores values once and are then disposed
print(list(zipped))
#unziped01,unziped02 = zip(*list(zipped)) # appear error
#print(unziped01)
#print(unziped02)

for i,(a,b) in enumerate(zipped):
    print("{0}:{1},{2}".format(i,a,b))

##dict
words=['apple','banana','bar','kiwi','cherry','strawberry','pineapple','plum']
by_letter={}
for word in words:
    letter=word[0]
    by_letter.setdefault(letter,[]).append(word)
print(by_letter)


from collections import defaultdict
letters = defaultdict(list)

