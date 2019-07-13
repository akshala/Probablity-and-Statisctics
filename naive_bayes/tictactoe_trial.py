# Akshala Bhatnagar
# 2018012
# Group 6
# Section A

import math
import numpy as np
import pandas as pd
data_map = {
	'x':0, 'o':1, 'b': 2
}

output_map = {
	'negative': 0,
	'positive': 1
}

totalDataFrame = pd.read_csv("/home/akshala/Documents/IIITD/P&S/Assignment/assignment3/dataSets/tic-tac-toe.csv")
n = len(totalDataFrame)
# nTrain = len(trainingData)
m = len(totalDataFrame.columns)
accuracy_count = 0

for k in range(0,n):
	trainingData = totalDataFrame.iloc[0:k].append(totalDataFrame.iloc[k+1:n])
	df_list = []

	x = trainingData.groupby(["Output"]).agg({'Output' : ["count"]})
	x.columns = ["_".join(y) for y in x.columns.ravel()]
	sum = x.iloc[0,0] + x.iloc[1,0]
	no = x.iloc[0,0]
	yes = x.iloc[1,0]
	p0 = x.iloc[0,0]/sum # 0,no
	p1 = x.iloc[1,0]/sum # 1,yes

	for index in range(1,m):
		col = "i"+str(index)
		col_summary_df = trainingData.groupby([col, 'Output']).size().unstack(fill_value=0)
		# print(col_summary_df)
		num_rows = len(col_summary_df)
		num_cols = len(col_summary_df.columns)
		frame_list = []
		for i in range(0,num_rows):
			sum = 0
			for j in range(0,num_cols):
				sum += col_summary_df.iloc[i,j]
			row_list = []
			for j in range(0,num_cols):
				row_list.append(col_summary_df.iloc[i,j]/sum)
			frame_list.append(row_list)
		probability_df = pd.DataFrame(frame_list)
		# print(probability_df)
		df_list.append(probability_df)

	k_probability_op_0 = p0
	k_probability_op_1 = p1
	for index in range(1,m):
		k_value = data_map[totalDataFrame.iloc[k,index]]
		k_probability_op_0 *= df_list[index-1].iloc[k_value,0]
		k_probability_op_1 *= df_list[index-1].iloc[k_value,1]
	k_output = output_map[totalDataFrame.iloc[k,0]]
	if (k_probability_op_0 > k_probability_op_1 and k_output == 0) or (k_probability_op_0 <= k_probability_op_1 and k_output == 1):
		accuracy_count += 1
		# print('row = {}, k_probability_op_0 = {}, k_probability_op_1 = {}, k_output = {}, accuracy = {}'.format(k,k_probability_op_0,k_probability_op_1, k_output, accuracy_count/(k+1)))
print('Accuracy = {}'.format(accuracy_count/n))



