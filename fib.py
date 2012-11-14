# Program for calculating fibonacci numbers.

def fibRecursive(n):
	return 1

def fibIterative(n):
	return 1

def fibDirect(n):
	n = n + 1
	# Using binets formula
	phi = (1 + 5**0.5) / 2
	return int(round((phi**n - (1-phi)**n) / 5**0.5))

# Main method for displaying fibonacci numbers.
def main():
	fibonaccinumbers = [fibRecursive(n) for n in range(10)]
	for fib in fibonaccinumbers:
		print fib, 

main()
