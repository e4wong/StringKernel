import re

def load(fn):
	data_matrix = []
	f = open(fn, "r")
	for line in f:
		tokens = line.split()
		protein_string = tokens[0]
		label = int(tokens[-1])
		data = (protein_string, label)
		data_matrix.append(data)
	return data_matrix



def kernel_function(string1, string2, substring_length):
	count = 0
	for i in range(0, len(string1) - substring_length + 1):
		string1_substring = string1[i:i+substring_length]
		for j in range(0, len(string2) - substring_length + 1):
			string2_substring = string2[j:j+substring_length]
			if string1_substring == string2_substring:
				count = count + 1
	return count


#the sign of the output of this function essentially depends on 
#which of previously mistaken protein_strings the current datapoint has
#more substrings in common with. If it has more in common with those
#labeled as postive ('1'), the output of this function will be positive.
#If it has more in common with those labeled as negative ('-1'), the output
#will be negative.
#
#If the actual label of this vector is negative, let's say, and it's dot product
#with the current w outputs positive, then dotproduct(w, datapoint)*label is negative
#and this classification is seen as a mistake, which adds the current vector to 
#w's collection. Now, there is another negative string in w's set so that when another
#negatively labeled string is being classified, the number of common substrings it has
#with the strings in w's collection will hopefully be weighted more towards negatively 
#classified strings since there are now more of them. That's my interpretation - Benjie.
def kernel_dot_product(w_collection, data_point, substring_length):
	count = 0
	for (protein_string, label) in w_collection:
		count = count + label * kernel_function(protein_string, data_point, substring_length)
	return count



#The current 'w' decision boundary vector consists of a linear combination of 
#past misclassifications. As more mistakes are made, more data is appended to 
#the collection of errors that make up w, and are further carried into the next
#dot product. 
def train(dataset, substring_length):
	w_collection = []
	for (protein_string, label) in dataset:
		if label * kernel_dot_product(w_collection, protein_string, substring_length) <= 0:
			w_collection.append((protein_string, label))
	return w_collection



def test(w_collection, dataset, substring_length):
	errors = 0
	num_samples = len(dataset)
	for (protein_string, label) in dataset:
		if label * kernel_dot_product(w_collection, protein_string, substring_length) <= 0:
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