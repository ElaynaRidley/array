from Associator import *

a =  Associator(10)
a.debug()
a.put("cat", "Katze")
a.put("mum", "Mutter")
a.put("mat", "Matte")
a.print()

print(a.get("mat"))
