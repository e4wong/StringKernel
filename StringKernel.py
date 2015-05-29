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
	found = []
	for i in range(0, len(s) - p + 1):
		s_substring = s[i:i+p]
		for j in range(0, len(t) - p + 1):
			t_substring = t[j:j+p]
			if s_substring == t_substring and not(s_substring in found):
				found.append(s_substring)
				count = count + 1
				break
	return count

def kernel_dot_product(data, x, p):
	count = 0
	for (feature, label) in data:
		count = count + label * kernel_function(feature, x, p)
	return count

def train(dataset, p):
	collection = []
	for (feature, label) in dataset:
		if label * kernel_dot_product(collection, feature, p) <= 0:
			collection.append((feature, label))
	return collection

def test(collection, dataset, p):
	errors = 0
	num_samples = len(dataset)
	for (feature, label) in dataset:
		if label * kernel_dot_product(collection, feature, p) <= 0:
			errors = errors + 1
	return float(errors)/ float(num_samples)


def main():
	training_set = load("hw5train.txt")
	test_set = load("hw5test.txt")
	print "P = 3:"
	collections = train(training_set, 3)
	print "Training Error: " + str(test(collections, training_set, 3))
	print "Testing Error: " + str(test(collections, test_set, 3))
	print "P = 4:"
	collections = train(training_set, 4)
	print "Training Error: " + str(test(collections, training_set, 4))
	print "Testing Error: " + str(test(collections, test_set, 4))

if __name__ == '__main__':
	main()