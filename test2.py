from Associator import *

a =  Associator(10)
a.put("dog", "Hund")
print(a.get("dog"))
a.print()
print([i for i in range(len(a.primaryKeys))])
print([x for x in a.primaryKeys])
print([x for x in a.primaryKeys])
