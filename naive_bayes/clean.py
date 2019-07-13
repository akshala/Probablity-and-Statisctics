with open ("/home/akshala/Documents/IIITD/P&S/Assignment/assignment3/shuttle-landing-control_final.csv") as f:
	for line in f:
		outputs1 = []
		outputs2 = []
		outputs3 = []
		line_elts = line.strip('\n').split(',')
		# print(line_elts)
		out_str = '{},{},{}'.format(line_elts[0], line_elts[1], line_elts[2])
		if line_elts[3]=='"*"':
			for i in range(1,3):
				outputs1.append(out_str+',{}'.format(i))
		else:
			outputs1.append(out_str+',{}'.format(line_elts[3]))
		if line_elts[4]=='"*"':
			for i in range(1,3):
				for temp_line in outputs1:
					outputs2.append(temp_line+',{}'.format(i))
		else:
			for temp_line in outputs1:
				outputs2.append(temp_line+',{}'.format(line_elts[4]))	
		if line_elts[5]=='"*"':
			for i in range(1,5):
				for temp_line in outputs2:
					outputs3.append(temp_line+',{}'.format(i))
		else:
			for temp_line in outputs2:
				outputs3.append(temp_line+',{}'.format(line_elts[5]))
		for temp_line in outputs3:
			print(temp_line+',{}'.format(line_elts[6]))