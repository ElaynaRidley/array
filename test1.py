from Associator import *

a =  Associator(10)
word = "dog"
print(word, a._hash(word), a._rehash(word))

word = "nasty"
print(word, a._hash(word), a._rehash(word))

word = "weird"
print(word, a._hash(word), a._rehash(word))

word = "gross"
print(word, a._hash(word), a._rehash(word))

word = "thing"
print(word, a._hash(word), a._rehash(word))

# nasty has the same hash values   9

#weird and thing both hash to 1
#gross and thing both rehash to 8
