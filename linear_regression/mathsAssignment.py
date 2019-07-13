import math

def correlationCoeff(X, Y, n):
	sumX = 0
	sumY = 0
	sumXY = 0
	sumXsquare = 0
	sumYsquare = 0
	i = 0
	for i in range(0,n):
		sumX = sumX + X[i]
		sumY = sumY + Y[i]
		sumXY = sumXY + X[i]*Y[i]
		sumXsquare = sumXsquare + X[i]*X[i]
		sumYsquare = sumYsquare + Y[i]*Y[i]
	numerator = (float)((n * sumXY) - (sumX * sumY))
	denominator = (float)(math.sqrt((n * sumXsquare) - (sumX*sumX)) * ((n * sumYsquare) - (sumY * sumY)))
	r = numerator / denominator
	return r

def regressionCoeff(X, Y, n): # Y = bX + a regressing Y on X
	sumX = 0
	sumY = 0
	sumXY = 0
	sumXsquare = 0
	i = 0
	for i in range(0,n):
		sumX = sumX + X[i]
		sumY = sumY + Y[i]
		sumXY = sumXY + X[i]*Y[i]
		sumXsquare = sumXsquare + X[i]*X[i]
	numerator = (float)((n * sumXY) - (sumX * sumY))
	denominator = (float)((n * sumXsquare) - (sumX*sumX))
	b = numerator / denominator
	meanX = (float) (sumX / n)
	meanY = (float) (sumY / n)
	a = meanY - (b*meanX)
	return b, a, meanX, meanY

def error(actual, predicted, n):
	diff = 0
	for i in range(0,n):
		diff = diff + math.pow((predicted[i] - actual[i]), 2)
		# print(predicted[i], actual[i])
	meanSquareError = (float) (diff / n)
	return meanSquareError

def y(x, b, a):
	return b*x + a

journal_name = []
H_index = []
impact_factor = []
with open("journals.csv") as f:
	for line in f:
		line_elts = line.strip(" \n").split(",")
		try:
			journal_name.append(line_elts[0])
			H_index.append(float(line_elts[1]))
			impact_factor.append(float(line_elts[2]))
		except ValueError:
			# print('Exception on {} or {}'.format(line_elts[1], line_elts[2]))
			pass
journal_name = journal_name[1:]
	
# print(H_index)
# print(impact_factor)

n = len(H_index)
corrCoeff = correlationCoeff(H_index, impact_factor, n)

end = int(0.8 * n)
trainingData = H_index[:end]
b, a, meanX, meanY = regressionCoeff(trainingData, impact_factor, end)
print("Regression Line equation is y = ", b, "x + ", a)

start = n - end
copyH_index = H_index[::-1]
testData = copyH_index[:start]
predicted_impact_factor = []
for i in range(0, start):
	predicted_impact_factor.append(y(copyH_index[i], b, a))
predicted_impact_factor_inOrder = predicted_impact_factor[::-1]

copy_impact_factor = impact_factor[::-1]
actual_impact_factor = copy_impact_factor[:start]
error = error(actual_impact_factor, predicted_impact_factor, start)
print("Mean squared error = ", error)

with open ('journalsResult.csv','w') as f:
	f.write('{},{},{},{}\n'.format("Journal", "H Index", "Impact Factor", "Predicted Impact Factor"))
	for i in range(0, end):
		f.write('{},{},{}\n'.format(journal_name[i], H_index[i], impact_factor[i]))
	for i in range(end, n):
		j = i - end
		f.write('{},{},{},{}\n'.format(journal_name[i], H_index[i], impact_factor[i], predicted_impact_factor_inOrder[j]))

conf_name = []
H_index_conf = []
with open("conferences.csv") as f:
	for line in f:
		line_elts = line.strip(" \n\"").split(",")
		try:
			conf_name.append(line_elts[0])
			H_index_conf.append(float(line_elts[1]))
		except ValueError:
			# print('Exception on {} or {}'.format(line_elts[1], line_elts[2]))
			pass
conf_name = conf_name[1:]

n_conf = len(H_index_conf)
impact_factor_conf = []
for i in range(0, n_conf):
	impact_factor_conf.append(y(H_index_conf[i], b, a))
# print(impact_factor_conf)

with open ('conferenceResult.csv','w') as f:
	f.write('{},{},{},\n'.format("Journal", "H Index", "Impact Factor"))
	for i in range(0, n_conf):
		f.write('{},{},{}\n'.format(conf_name[i], H_index_conf[i], impact_factor_conf[i]))
