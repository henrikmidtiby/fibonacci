# Program for calculating fibonacci numbers.

def fibRecursive(n):
	if n < 2:
		return 1
	else:
		return fibRecursive(n - 1) + fibRecursive(n - 2)

def fibIterative(n):
	return 1

def fibDirect(n):
	return 1

# Main method for displaying fibonacci numbers.
def main():
	fibonaccinumbers = [fibRecursive(n) for n in range(10)]
	for fib in fibonaccinumbers:
		print fib, 

main()
