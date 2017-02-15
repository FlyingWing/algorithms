#encoding:utf-8

class BitMap(object):
	"""docstring for BitMap"""
	def __init__(self, max):
		self.size  = self.calculateElemIndex(max, True)
		self.array = [0 for i in xrange(self.size)]

	def calculateElemIndex(self, num, up=False):
		if up:
			return int((num + 31 -1) /31 )
		else:
			return num /31

	def calculateBitIndex(sef, num):
		return num % 31

	def set(self, num):
		elemIndex = self.calculateElemIndex(num)
		bitIndex  = self.calculateBitIndex(num)
		elem = self.array[elemIndex]
		self.array[elemIndex] = elem | (1 << bitIndex)

	def clean(self, i):
		elemIndex = self.calculateElemIndex(i)
		bitIndex  = self.calculateBitIndex(i)
		elem = self.array[elemIndex]
		self.array[elemIndex] = elem & (~(1 << bitIndex))
		
if __name__=="__main__":
	bitmap = BitMap(87)
	bitmap.set(0)
	bitmap.set(34)
	print bitmap.array
	bitmap.clean(0)
	print bitmap.array
	bitmap.clean(34)
	print bitmap.array