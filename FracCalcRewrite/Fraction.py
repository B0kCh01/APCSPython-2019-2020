# Python rewrite of FracCalc with Objects

class Fraction():
	def __init__(self, string):
		parts = self.parseFraction(string)
		self.whole = parts[0]
		self.numerator = parts[1]
		self.denominator = parts[2]
		self.negative = 1

	def parseFraction(self, string):
		wholeAndFrac = string.split("_")
		if ("/" in string):
			return [int(wholeAndFrac), 0, 1]
		fraction = wholeAndFrac[len(wholeAndFrac) - 1].split("/")
		if (len(wholeAndFrac) == 1):
			return [0, int(fraction[0], int(fraction[1]))]
		else:
			return [int(wholeAndFrac[0]), int(fraction[0]), int(fraction[1])]
	# Get numbers
	def get_properties(self):
		print(f"whole:{self.whole} "
			  f"fraction:{self.negative * self.numerator}/{self.denominator}")
def main():
	myFrac = Fraction(whole=1, denomintator=23, numerator="322")
	myFrac.get_properties()

if __name__ == "__main__":
	main()
