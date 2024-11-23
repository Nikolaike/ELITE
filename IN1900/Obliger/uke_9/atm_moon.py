def dict(filename):
    d = {}
    with open(filename, "r") as infile:
        infile.readline()
        for line in infile:
            a = line.split(";")
            for k in a:
                b = k.split("-")
                d[b[0].upper()] = int(b[1].replace(",",""))


    print(d)

dict("atm_moon.txt")

"""
Terminal> python .\atm_moon.py
{'HELIUM 4 ': 40000, ' NEON 20 ': 40000, ' HYDROGEN ': 35000, 'ARGON 40 ': 30000,
' NEON 22 ': 5000, ' ARGON 36 ': 2000, 'METHANE ': 1000, ' AMMONIA ': 1000,
' CARBON DIOXIDE ': 1000}

"""
