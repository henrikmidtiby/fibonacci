# Program for calculating fibonacci numbers.

def fibRecursive(n):
	return 1

def fibIterative(n):
	(a, b) = (1, 1)
	for k in range(n):
		(a, b) = (b, a + b)
	return a

def fibDirect(n):
	return 1

# Main method for displaying fibonacci numbers.
def main():
	fibonaccinumbers = [fibRecursive(n) for n in range(10)]
	for fib in fibonaccinumbers:
		print fib, 

main()
