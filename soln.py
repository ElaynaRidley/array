import Array

class Associator:
	def __init__(self, size):
		self.prim_keys = Array.Array(size)
		self.prim_values = Array.Array(size)
		self.ovflw_keys = Array.Array(size)
		self.ovflw_values = Array.Array(size)
		self.resizing = True                            # two different versions of the program, one resizes and the other does not
		self.debugging = False

	.... code here ....

	def debug(self):
		self.debugging = True

	def dump(self):
		s = ""
		for i in range(0,len(self.prim_keys)):
			if self.prim_keys[i] is not None:
				s += "put " + self.prim_keys[i] + "=" + self.prim_values[i] + "\n"

		for i in range(0,len(self.ovflw_keys)):
			if self.ovflw_keys[i] is not None:
				s += "put " + self.ovflw_keys[i] + "=" + self.ovflw_values[i] + "\n";
		return s

	def print(self):
		print("PRIMARY AREA")
		print("--------------------")
		count=0
		for i in range(len(self.prim_keys)):
			if self.prim_keys[i] != None:
				print("%2d. %-12s %-12s" % (i, self.prim_keys[i], self.prim_values[i]))
				count += 1
		print("(" + str(count) + " key/value pairs in primary area)")

		count = 0
		for i in range(len(self.ovflw_keys)):
			if self.ovflw_keys[i] != None:
				count += 1
		if count == 0:
			print(" Secondary area is empty")
			return

		print("\nSECONDARY AREA")
		print("--------------------")
		for i in range(len(self.ovflw_keys)):
			if self.ovflw_keys[i] != None:
				print("%2d. %-12s %-12s" % (i, self.ovflw_keys[i], self.ovflw_values[i]))
		
	def clear(self):
		self.prim_keys = Array.Array(size)
		self.prim_values = Array.Array(size)
		self.ovflw_keys = Array.Array(size)
		self.ovflw_values = Array.Array(size)

		
		
		