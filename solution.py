"""
Author: Bharadwaj Srigiriraju

Input: 	Consists of a single test case, which consists of integer n
(n >= 3 and n <= 100).

Output: Shortest sequence of moves that will correctly reorder the bins.
Each move is of the form "f to t", where f at t are integers
representing the movement of bins in locations
f and f+1 to locations t and t+1.
If multiple solutions are possible, display any one of them.

Note: It's not clear what should be printed in case of a swapping 
from positions f+1 => t and f => t+1. 

This solution assumes we can print f and t in such cases as an alternate path.
"""

def baggage_solver(n):
	""" 
	Reduces the pattern to the form ABBA....BBAA,
	and then create pairs of A's and B's in the middle until
	we have all As and Bs in pairs, and then rearrange.
	"""
	if n == 3:
		# special case solution for n == 3, as it goes until index -3.
		moves = [(2,-1), (5,2), (3,-3)]
		return moves
	if n > 7:
		"""
		from n == 8, we can reduce pattern to this form: ABBA[__(BA)*]BBAA
		in which the part inside [] can be solved recursively by calling
		baggage_solver(n-4) as 4 A's and 4 B's are outside.
		"""
		moves = [(2*n-2, -1), (3, 2*n-2)]
		recursive_pattern_moves = baggage_solver(n-4)
		# print changed positions with updated index as per n, not n-4
		moves += [(x+4,y+4) for (x,y) in recursive_pattern_moves]
		moves += [(0, 2*n-5), (2*n-1,0)]
		return moves
	else:
		"""
		returns the positions to be printed for the given simple case
		"""
		moves = []
		if n == 4:
			moves.append((2*n-2, -1))
			moves.append((n-1, 2*n-2))
			moves.append((0, n-1))
			moves.append((2*n-1,0))
		if n == 5:
			moves.append((2*n-2, -1))
			moves.append((n-2, 2*n-2))
			moves.append((n, n-2))
			moves.append((-1, n))
			moves.append((2*n-1, -1))
		if n == 6:
			moves.append((2*n-2, -1))
			moves.append((2*n-5, 2*n-2))
			moves.append((2*n-10, 2*n-5))
			moves.append((n, 2*n-10))
			moves.append((-1, n))
			moves.append((2*n-1, -1))
		if n == 7:
			moves.append((2*n-2, -1))
			moves.append((n-2, 2*n-2))
			moves.append((n+1, n-2))
			moves.append((n-4, n+1))
			moves.append((n+2, n-4))
			moves.append((-1, n+2))
			moves.append((2*n-1, -1))
		return moves


if __name__ == "__main__":
	print "Enter your input (Enter the character 'x' to run all the cases: "
	n = raw_input()
	if n == 'x':
		for i in xrange(3,101):
			print "for n == ", i
			a = baggage_solver(i)
			for m in a:
				print m[0], " to ", m[1]
			print
		exit()

	try:
		n = int(n)
	except ValueError:
		print "Wrong input, Enter a number or x"
		exit()

	if not ( 3 <= n <= 100):
		print "Wrong input, Enter a number between 3 and 100 inclusive"
	else:
		for i in xrange(n, n+1):
			print "for n == ", i
			a = baggage_solver(i)
			for m in a:
				print m[0], " to ", m[1]
			print 

