import random
import numpy as np
import math
import matplotlib.pyplot as plt

# EggHolder function [-512,512]
def function(x):
	f = 0
	for i in range(len(x) - 1):
		f += -x[i] * math.sin(math.sqrt(abs(x[i] - x[i + 1] - 47))) - (x[i + 1] + 47) * math.sin(math.sqrt(abs(x[i + 1] + x[i] / 2 + 47)))
	return f
 
def sort(x, f):
		i = 1
		while i > 0:
			i = 0
			for j in range(len(f) - 1):
				if f[j] > f[j + 1]:
					buf = f[j]
					f[j] = f[j + 1]
					f[j + 1] = buf
					buf = x[j]
					x[j] = x[j + 1]
					x[j + 1] = buf
					i += 1
# Fish School Search algorithm
def FSS(X_min, X_max, N_agent, iter, Wmax, StepMax, StepMin):
	X = []
	SummWeight = 0
	# population initialization
	for i in range(N_agent):
		xi = []
		for j in range(len(X_min)):
			xi.append(X_min[j] + random.random() * (X_max[j] - X_min[j]))
		X.append(xi)
	weight = []
	for i in range(N_agent):
		weight.append(Wmax / 2)
 
	iteration = 0
	indStepMax = StepMax
	# main loop of the algorithm (by the number of iterations)
	while iteration < iter:
		delata_f = []
		X1_new = []
		indivitStep = []
		for i in range(N_agent):
			indivitStep.append(random.random() * indStepMax)
		# individual swimming
		for i in range(N_agent):
			xi = []
			for j in range(len(X_min)):
				dvij = X[i][j] + random.uniform(-1, 1) * indivitStep[i]
				if (dvij >= -512 and dvij <= 512):
					xi.append(dvij)
				else:
					xi.append(X[i][j])
			f1 = function(X[i])
			f2 = function(xi)
			if (f2 - f1 < 0 ):
				X1_new.append(xi)
			else:
				X1_new.append(X[i])
 
			delta = math.fabs(function(X1_new[i]) - function(X[i]))
			delata_f.append(delta)
		max_delta_f = max(delata_f)
 
		# weight recalculation
		for i in range(N_agent):
			if delata_f[i] != 0:
				weight[i] = weight[i] + delata_f[i] / max_delta_f
			if weight[i] < 1:
				weight[i] = 1
			elif weight[i] > Wmax:
				weight[i] = Wmax
		# instinctive collective swimming
		m = [] # general migration step
		chislitel = []
		for j in range(len(X_min)):
			chislitel.append(0)
		for i in range(N_agent):
			for j in range(len(X_min)):
				chislitel[j] = chislitel[j] + (X1_new[i][j] - X[i][j]) * delata_f[i]
		for j in range(len(X_min)):
			m.append(chislitel[j] / sum(delata_f))
 
		# population displacement
		X2_new = []
		for i in range(N_agent):
			xi = []
			for j in range(len(X_min)):
				dvij = X1_new[i][j] + m[j]
				if (dvij >= -512 and dvij <=512):
					xi.append(dvij)
				else:
					xi.append(X1_new[i][j])
			X2_new.append(xi)
	
		# calculate the center of gravity of the fish school
		Xcentre = []
		chislitel = []
		for j in range(len(X_min)):
			chislitel.append(0)
		# calculate of general migration step
		for i in range(N_agent):
			for j in range(len(X_min)):
				chislitel[j] = chislitel[j] + (X2_new[i][j] * weight[i])
		for j in range(len(X_min)):
			Xcentre.append(chislitel[j] / sum(weight))
 
		# collective-volitional swimming
		X3_new = []
		sign = 0
		if sum(weight) > SummWeight:
			sign = -1
		else:
			sign = 1
		for i in range(N_agent):
			xi = []
			for j in range(len(X_min)):
				dvij = X2_new[i][j] + sign * indStepMax * random.random() * (X2_new[i][j] - Xcentre[j])
				if (dvij >= -512 and dvij <= 512):
					xi.append(dvij)
				else:
					xi.append(X2_new[i][j])
			X3_new.append(xi)
		SummWeight = sum(weight)
 
		for i in range(N_agent):
			for j in range(len(X_min)):
				X[i][j] = X3_new[i][j]
 
		# decreasing the step of individual search
		indStepMax = indStepMax - (StepMax-StepMin) / iter
 
		iteration += 1
 
	f = []
	for xi in X:
		f.append(function(xi))
	sort(X,f)
	return X
	
#   FSS(X_min,              X_max,   N_agent, iter, Wmax, StepMax, StepMin)
x = FSS([-512, -512, -512, -512], [512, 512, 512, 512], 1000, 1000, 50, 50, 10) #you can change it

print(function(x[0]))
