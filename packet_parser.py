def parse(fname, L):

	print("Parsing the filtered raw packets.")

	f = open(fname, "r")
	lines = f.readlines()

	for line in lines:
		L.append(line.strip().split())
		line = f.readline()
	f.close()