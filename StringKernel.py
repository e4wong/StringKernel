import re
import numpy

def load(fn):
	data_matrix = []
	f = open(fn, "r")
	for line in f:
		tokens = line.split()
		data = (tokens[0], int(tokens[-1]))
		data_matrix.append(data)
	return data_matrix

def kernel_function(s, t, p):
	count = 0
	for i in range(0, len(s) - p + 1):
		s_substring = s[i:i+p]
		for j in range(0, len(t) - p + 1):
			t_substring = t[j:j+p]
			if s_substring == t_substring:
				count = count + 1
	return count



def main():
	training_set = load("hw5train.txt")
	test_set = load("hw5test.txt")
<<<<<<< HEAD
	a = "asdf"
	b = "adfsdsdsdsd"
	print kernel_function(a, b, 2)
=======

>>>>>>> b0537375e6863078c362004de6ca2375793240b9
if __name__ == '__main__':
	main()