'''
Elayna Ridley
Project 3
'''
from Array import *
class Associator:
	'''This class hashes values and their keys into a primary area.
		If the index is already taken, then it rehashes.
		If both of those slots are taken, then it's put into the next avaliable slot in the overflow area.
	'''
	def __init__(self, size):
		'''
			self.size is the size of the array
			self.primaryKeys is the array of the primary area values
			self.overflowKeys is the array of the overflow area values
			self.primaryValues is the array of the values of the primary area
			self.overflowValues is the array of the values of the overflow area
			self.debug is if debuging is on or off. It's off by default
		'''
		self.size = size
		self.primaryKeys = Array(self.size)
		self.primaryValues = Array(self.size)
		self.overflowKeys = Array(self.size)
		self.overflowValues = Array(self.size)
		self._debug = False
		self.resizing = True
		

	def _hash(self, key):
		'''hash takes a string and for each letter it adds 79 X the ord of the letter to a sum and mods it by the lenght of the array
		'''
		sum = 0
		for i in range(len(key)):
			sum += 79 * ord(key[i])
		return sum % len(self.primaryKeys)
		#if len(key) == 1:
		#       sum += ord(key)
		#else:
		#       sum += (ord(key[0]) + ord(key[-1]))
		#return sum % len(self.primaryKeys)
			

	def _rehash(self, key):
		'''rehash takes a string and for each letter
			it adds 31 x the ord of the letter to a sum
			and mods it by the length of the array
		'''
		sum = 0
		for i in range(len(key)):
			sum += 31 * ord(key[i])
		return sum % len(self.primaryKeys)

	def put(self, key, value):
		'''this puts a value and key into primary or overflow based on its hash or rehash'''
		h1 = self._hash(key)
		h2 = self._rehash(key)

		if self.primaryKeys[h1] == None:
			self.primaryKeys[h1] = key
			self.primaryValues[h1] = value
		else:
			if self.primaryKeys[h1] == key:
				self.primaryValues[h1] = value
				return
			else:
				if self.primaryKeys[h2] == None:
					self.primaryKeys[h2] = key
					self.primaryValues[h2] = value
				else:
					if self.primaryKeys[h2] == key:
						self.primaryValues[h2] = value
					else:
						for i in range(len(self.overflowKeys)):
							if self.overflowKeys[i] == key:
								self.overflowValues[i] = value
							elif self.overflowKeys[i] == None:
								self.overflowKeys[i] = key
								self.overflowValues[i] = value
								return
								
		return True
				

		

	def get(self, key):
		'''
			this gets the value associated with a key or None if the key doesn't exist
		'''
		h1 = self._hash(key)
		h2 = self._rehash(key)

		if self._debug == True:
			#print("Hash 1("+key+")"+"=",h1)
			#print("Hash 2("+key+")"+"=",h2)
			for i in range(len(self.primaryKeys)):
				if self.primaryKeys[i] != None:
					print("Hash 1(",self.primaryKeys[i],")"+"=",h1)
					print("Hash 2(",self.primaryKeys[i],")"+"=",h2)

		if self.primaryKeys[h1] == None:
			return None
		else:
			if self.primaryKeys[h1] == key:
				return self.primaryValues[h1]
			else:
				if self.primaryKeys[h2] == None:
					return None
				else:
					if self.primaryKeys[h2] == key:
						return self.primaryValues[h2]
					else:
						for i in range(len(self.overflowKeys)):
							if self.overflowKeys[i] == key:
								return self.overflowValues[i]
							else:
								return None

	def delete(self, key):
		#extra credit
		pass

	def exists(self, key):
		for i in range(len(self.primaryKeys)):
			if self.primaryKeys[i] == key:
				return True
			elif self.overflowKeys[i] == key:
							return True
			else:
				done = False
		return done

	def find(self, value):
		#extra credit
		for i in range(len(self.primaryKeys)):
			if self.primaryKeys[i] == key:
						return i
		return -1

	def stats(self):
		primsize = len(self.primaryKeys)
		oversize = len(self.overflowKeys)
		primslotsclosed = 0
		overslotsclosed = 0
		for i in range(len(self.primaryKeys)):
			if self.primaryKeys[i] != None:
				primslotsclosed += 1
		for i in range(len(self.overflowKeys)):
			if self.overflowKeys[i] != None:
				overslotsclosed += 1
		return [primsize, primslotsclosed, oversize, overslotsclosed]

	def debug(self):
		self._debug = True

	'''def print(self):
		print("Primary:")
		for i in range(len(self.primaryKeys)):
			print(self.primaryKeys[i], ":", self.primaryValues[i])
		print()
		print("Overflow:")
		for i in range(len(self.overflowKeys)):
			print(self.overflowKeys[i], ":", self.overflowValues[i])'''


	def print(self):
		print("PRIMARY AREA")
		print("--------------------")
		count=0
		for i in range(len(self.primaryKeys)):
			if self.primaryKeys[i] != None:
				print("%2d. %-12s %-12s" % (i, self.primaryKeys[i], self.primaryValues[i]))
				count += 1
		print("(" + str(count) + " key/value pairs in primary area)")

		count = 0
		for i in range(len(self.overflowKeys)):
			if self.overflowKeys[i] != None:
				count += 1
		if count == 0:
			print(" Secondary area is empty")
			return

		print("\nSECONDARY AREA")
		print("--------------------")
		for i in range(len(self.overflowKeys)):
			if self.overflowKeys[i] != None:
				print("%2d. %-12s %-12s" % (i, self.overflowKeys[i], self.overflowValues[i]))

   

	def _find_ovflow(self, key):
		for i in range(len(self.overflowKeys)):
			if self.overflowKeys[i] == key:
				return i
		return -1

	def _find_empty(self):
		for i in range(len(self.overflowKeys)):
			if self.overflowKeys[i] == None:
				return i

	def clear(self):
		self.primaryKeys = Array(size)
		self.primaryValues = Array(size)
		self.overflowKeys = Array(size)
		self.overflowValues = Array(size)

	def dump(self):
		s = ""
		for i in range(0,len(self.primaryKeys)):
			if self.primaryKeys[i] is not None:
				s += "put " + self.primaryKeys[i] + "=" + self.primaryValues[i] + "\n"

		for i in range(0,len(self.overflowKeys)):
			if self.overflowKeys[i] is not None:
				s += "put " + self.overflowKeys[i] + "=" + self.overflowValues[i] + "\n";
		return s

				
	def _resize(self):
		#extra credit
		pass

	def _compact(self):
		#extra credit
		pass

	def __setitem__(self, key, value):
		#extra credit
		pass

	def __getitem__(self, key):
		#extra credit
		pass

	def __len__(self):
		#extra credit
		pass

	def __del__(self, key):
		#extra credit
		pass

if __name__ == "__main__":
	ok = Associator(10)
	ok.put("hello", "hi")
	ok.put("goodbye", "bye")
	ok.put("cat", "fluffy")
	ok.put("dog","bark")
	ok.put("bird", "feathers")
	ok.put("snake", "hiss")
	ok.put("cow", "moo")
	ok.put("horse", "neigh")
	ok.put("hamster", "small")
	ok.put("gerbil", "fur")
	ok.put("fox", "cute")
	ok.print()
	print("ok.get for horse:", ok.get("horse"))
	print("ok.get for emu:", ok.get("emu"))
	print("ok._find_ovflow for gerbil:" ,ok._find_ovflow("gerbil"))
	print("ok._find_ovflow for fox:" ,ok._find_ovflow("fox"))
	print('ok._find_empty:',ok._find_empty())
	print('ok.exists for cat:', ok.exists("cat"))
	print("ok.exists for giraffe:", ok.exists("giraffe"))
	print("ok.stats: [size of primary area, slots of primary area in use, size of overflow, overflow slots in use]:",ok.stats())
	print(ok.dump())
	ok.clear()
	ok.print()
					
					

