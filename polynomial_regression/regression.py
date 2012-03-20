import numpy as np
from numpy.random import permutation

orig_mat = np.loadtxt('polyfit.tsv',skiprows=1)

orig_x = orig_mat[:,0]
orig_y = orig_mat[:,1]

new_mat = permutation(orig_mat)

train = new_mat[0:100,:]
test = new_mat[100:200,:]




