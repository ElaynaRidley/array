import Array

class FreqDist:
	def __init__(self, *args):
		if len(args) != 0:
			self.start = float(args[0])
			self.end = float(args[1])
			self.delta = float(args[2])
			if len(args) == 4:
				self.acquireDataFromFile(args[3])
				self.tabulate()
				self.display("")

	def setbounds(self, start, end, delta):
		self.start = start
		self.end = end
		self.delta = delta

	def acquireDataFromFile(self, filename):
		with open(filename) as f:
			self.lines = f.read().split("\n")

	def acquireData(self, somelist):
		if type(somelist) is list:
			self.lines = somelist
		elif type(somelist) is str:
			self.lines = text.split("\n")

	def tabulate(self):
		self.belowcount = 0           # this counts values below the starting value
		self.abovecount = 0           # this counts values above the ending value
		numslots = int(round((self.end - self.start)/self.delta, 0))
		self.counts = Array.Array(numslots, 0)
		for line in self.lines:
			n = float(line)
			if n < self.start:
				self.belowcount += 1
			elif n > self.end:
				self.abovecount += 1
			else:
				slotnumber = int((n - self.start) / self.delta)
				self.counts[slotnumber] += 1
		

	def info(self):
		print("start=",self.start)
		print("end=",self.end)
		print("delta=",self.delta)
		print("n in dataset=",len(self.lines))
		
	def display(self, direction):
		'''   right now we are only showing from lowest to highest, i.e. ascending '''
		print("%4d below %f" % (self.belowcount,self.start))
		x = self.start
		for k in range(len(self.counts)):
			pct = self.counts[k] / len(self.lines) * 100
			print("%6.2f     =   %4d occurrences (%3.0f %%)" % (x, self.counts[k], pct))
			x += self.delta
		print("%4d above %f" % (self.abovecount, self.end))

if __name__ == "__main__":
	fd = FreqDist(0, 100, 10)
	samples = [int(x) for x in "5,26,15,38,99,16,47,10,50,75,0,21,25,89,99,44,46,76,62,12,10,4".split(",")]
	fd.acquireData(samples)
	fd.tabulate()
	fd.display("ascending")
