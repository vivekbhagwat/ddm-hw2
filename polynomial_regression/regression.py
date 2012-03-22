import numpy as np
from numpy.random import permutation

N = 200

#multiplies w_k and x^k for every k
#then sums that up
def best_fit_polynomial(x,w,k_large):
	print "w[0] range(k_large+1)"
	print w
	print w[0]
	print range((k_large+1))

	inside = [w[0][k_small] * (x**k_small) for k_small in range(k_large)]
	print "inside"
	print inside
	return [y.cumsum() for y in inside][0][0,0]


orig_mat = np.loadtxt('polyfit.tsv',skiprows=1)

orig_x = orig_mat[:,0]
orig_y = orig_mat[:,1]

# new_mat = permutation(orig_mat)
new_mat = orig_mat

train = new_mat[0:(N/2),:]
test = new_mat[(N/2):200,:]

train_x = train[:,0]
train_y = train[:,1]

test_x = test[:,0]
test_y = test[:,1]

w_hat_arr = []
w_hat_err = []
best_error = (0, None) #K, best_fit

for k_large in range(10)[1:]:
	height = k_large+1
	phi = np.matrix( np.zeros((train.shape[0],height)) ) #100, K+1

	for j in range(height):
		phi[:,j] = np.matrix(train_x**j).transpose()

	w_hat = (phi.transpose() * phi).getI() * phi.transpose() * np.matrix(train_y).transpose()

	error = 0.0
	for i, x_i in enumerate(train_x):
		print "train_x[i]"
		print x_i
		print "w_hat"
		print w_hat
		print "k_large"
		print k_large
		fit = best_fit_polynomial(x_i,w_hat,k_large)
		print fit
		
		y_i = train_y[i]
		error += (y_i - fit)

	error /= len(train_x)


	best_error = (k_large, error) if not(best_error[1]) or best_error[1] > error else best_error
	# print k
	# print w_hat
	# print best_fit
	# print "\n"
	w_hat_arr.append(w_hat)

print w_hat_arr
print best_error








