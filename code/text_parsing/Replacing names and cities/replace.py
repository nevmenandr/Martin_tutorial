fin = open("C:/Users/vital/Documents/Python Scripts/texts.txt", "r", encoding='UTF-8')
fout = open("texts2.txt", "w", encoding='UTF-8')
memes = open("cities", "r")

a = fin.read()
b = memes.readlines()


def pars(list1):
	res = []
	
	for line in list1:
		line1= []
		line  = line.split(',')
		line[-1] = line[-1].split('-')[0]
		for i in line:
			line1.append(i.strip())
		res.append(line1)
	return res
	

def repl(a, b):
	for names in b:
		for j in names:
			print(j)
			a = a.replace(j, names[0])
	return a

a = repl(a, pars(b))
fout.write(a)
fout.close()
