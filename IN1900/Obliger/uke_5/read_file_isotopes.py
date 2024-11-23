weight = []
Natural_abundance = []
infile = open("oxygen.txt" , "r")

for line in infile:
    words = line.split()
    weight.append(words[1])
    Natural_abundance.append(words[2])


y = 16
for i in range(1, len(weight)):
    x = float(weight[i])*float(Natural_abundance[i])
    print(f"Molar masse for isotop {y}: {x:7.4f} mol")
    y +=1

"""
Terminal> python .\read_file_isotopes.py
Molar masse for isotop 16: 15.9564 mol
Molar masse for isotop 17:  0.0063 mol
Molar masse for isotop 18:  0.0367 mol



"""
