def filter(fName, var):
	print("Filtering raw text files");
	#print(fName)
	filteredFile = "Node" + str(var) + "_filtered.txt"
	f = open(fName, "r")
	file = open(filteredFile, "w")
	lines = f.readlines()

	for line in lines:
		if 'ping' in line:
			file.write(line) 
			
	f.close()
	file.close()