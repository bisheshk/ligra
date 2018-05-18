import csv

compressions = ["BYTERLE", "BYTE", "NIBBLE", "STREAMVEC", "STREAMVBYTE", "UNCOMPRESSED"]
applications = ["decoderSpeed", "PageRank", "BFS","BC","Radii","Components"]
testfiles = ["livejournal", "orkut", "nlp", "twitter", "uk-union"]

def find_med(l):
	return sorted(l)[len(l)//2]

if __name__ == "__main__":
	for file in testfiles:
		with open(file + ".csv", "wb") as csvfile:
			writer = csv.writer(csvfile, delimiter="\t")
			writer.writerow(['', 'ByteRLE', 'Byte', 'Nibble', 'StreamVec', 'StreamVByte', 'Uncompressed'])
			for app in applications:
				results_array = [[], [], [], [], [], []]
				with open("{}/{}.txt".format(file, app), "r") as f:
					runtimes = []
					i = 0
					for line in f.readlines():
						if line[:4] in ["size", "n = ", "read", "crea"] or line == "\n":
							continue
						if " 1 PROCESSORS " in line:
							break
						result = line.split()[-1] # either BYTERLE or a number
						try:
							runtimes.append(float(result))
						except Exception:
							if len(runtimes) == 0:
								continue
							results_array[i].append(find_med(runtimes))
							runtimes = []
							i = (i + 1) % 6
					results_array[i].append(find_med(runtimes))
				for i in range(len(results_array)):
					results_array[i] = find_med(results_array[i])
				writer.writerow([app] + results_array)
