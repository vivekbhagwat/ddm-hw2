import numpy as np

def load_section(sect):
	return np.loadtxt(sect+'.tsv', delimiter="\t", dtype="string")


def randomize_and_split(mat, N=2000):
	new_mat = np.random.permutation(mat)
	return (new_mat[0:(N/2), :], new_mat[(N/2):N, :])

def add_column(mat, value=0, at_index=0):
	(rows, cols) = mat.shape
	mat = np.append(mat, np.zeros(rows).reshape(rows, 1), axis=1) #append a column of the same height
	mat[at_index,cols-1] = value
	return mat

sections = ("Arts", "Business", "Obituaries", "Sports", "World")

words = {}
word_count = 0

bayes_matrix = np.matrix((5,0))

test_matrices = []

sect_index = 0

for sect in sections:
	(train, test) = randomize_and_split(load_section(sect))
	test_matrices.append(test)

	for row in train:
		# url = row[0]
		title = ' '.split(row[1])
		body = ' '.split(row[2])
		for word in title:
			print bayes_matrix
			print words

			if not(words.has_key(word)):
				words[word] = word_count
				word_count += 1
				bayes_matrix = add_column(bayes_matrix, 1, sect_index)
			else:
				bayes_matrix[sect_index,words[word]] += 1


		for word in body:
			if not(words.has_key(word)):
				words[word] = word_count
				word_count += 1
				bayes_matrix = add_column(bayes_matrix, 1, sect_index)
			else:
				bayes_matrix[sect_index,words[word]] += 1


	sect_index += 1


#trained.







