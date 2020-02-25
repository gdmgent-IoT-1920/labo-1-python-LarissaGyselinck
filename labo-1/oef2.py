f = open("namen.txt", "r")

d = dict()

for line in f.readlines():
	line = line.strip()
	line = line.lower()

	names = line.split(" ")

	for name in names:
		if name in d:
			d[name] = d[name] + 1
		else:
			d[name] = 1

for key in list(d.keys()):
	print(key, ":", d[key])