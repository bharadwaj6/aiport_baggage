"""
Author: Bharadwaj Srigiriraju

Input: 	Consists of a single test case, which consists of integer n
(n >= 3 and n <= 100).

Output: Shortest sequence of moves that will correctly reorder the bins.
Each move is of the form "f to t", where f at t are integers
representing the movement of bins in locations
f and f+1 to locations t and t+1.
If multiple solutions are possible, display any one of them.
"""

# n = int(raw_input())
def baggage_solver(n):
	""" If n == 3, it solves the baggage problem by brute force.
	If n > 3, we create a pattern of the form ABBA....BBAA,
	and then create pairs of A's and B's in the middle until
	we have all As and Bs in pairs, and then rearrange."""
	
	if n > 7:
		"""
		from n == 8, we can reduce pattern to this form: ABBA[__(BA)*]BBAA
		in which the part inside [] can be solved recursively by calling
		baggage_solver(n-4) as 4 A's and 4 B's are outside.
		"""
		changed_positions = baggage_solver(n-4) # print changed positions with updated index as per n, not n-4

	if n > 3:
		"""
		returns the positions to be printed for the given (sub)string
		"""
		no_pos = 2 * n
		positions = [''] * no_pos
		string_list = ['B' if x % 2 == 0 else 'A' for x in xrange(no_pos)]
		positions += string_list
		astring = ''.join(string_list)
		moves = []
		if n == 4:
			positions[2*n-2], positions[2*n-1] = positions[4*n-3], positions[4*n-2]
			positions[4*n-3], positions[4*n-2] = '', ''
			moves.append((4*n-3, 2*n-2))
			positions[4*n-3], positions[4*n-2] = positions[4*n-6], positions[4*n-5]
			positions[4*n-5], positions[4*n-6] = '', ''
			moves.append((4*n-6, 4*n-3))
			# ABBA()BBAA pattern created
			positions[2*n+2], positions[2*n+3] = positions[2*n], positions[2*n-1]
			positions[2*n], positions[2*n-1] = '', ''
			moves.append((2*n, 2*n+2))
			positions[2*n], positions[2*n-1] = positions[4*n-1], positions[4*n-2]
			positions[4*n-1], positions[4*n-2] = '', ''
			moves.append((4*n-1, 2*n))
			for m in moves:
				print m[0]-2*n+1, " to ", m[1]-2*n+1



	if n == 3:
		# special case solution for n == 3, as it goes until index -3.
		pass


baggage_solver(4)
