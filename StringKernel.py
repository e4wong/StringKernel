import re

def load(fn):
	ds = []
	f = open(fn, "r")
	for line in f:
		tokens = line.split()
		data = (tokens[0], int(tokens[-1]))
		ds.append(data)
	return ds


def main():
	training_set = load("hw5train.txt")
	test_set = load("hw5test.txt")
if __name__ == '__main__':
	main()