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


def main():
	training_set = load("hw5train.txt")
	test_set = load("hw5test.txt")

if __name__ == '__main__':
	main()