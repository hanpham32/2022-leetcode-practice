class Solution:
	def fib(self, n: int) -> int:
		if (n <= 0): # check for exceptional cases
			return 0
		if (n >= 3):
			return fib(n-1) + fib(n-2) # recursion
		else:
			return 1 # base case