# a)
import numpy as np
def extract_data(filename):
    infile = open(filename , "r")
    profile_list = infile.readline()
    temperatur = []
    for line in infile:
        line = line.split()
        for i in line:
            temperatur.append(float(i))
    infile.close()
    return temperatur
temp_oct_1945 = extract_data("temp_oct_1945.txt")
temp_oct_2014 = extract_data("temp_oct_2014.txt")



mean_1945 = np.mean(temp_oct_1945)
max_1945 = np.max(temp_oct_1945)
min_1945 = np.min(temp_oct_1945)

mean_2014 = np.mean(temp_oct_2014)
max_2014 = np.max(temp_oct_2014)
min_2014 = np.min(temp_oct_2014)

print("Temperatur i october 1945:")
print(f"Gjennomsnittstempereratur {mean_1945:.1f} celcius")
print(f"Høyeste temperatur {max_1945:.1f} celcius")
print(f"Laveste temperatur {min_1945:.1f} celcius")

print("-"*40)

print("Temperatur i october 2014")
print(f"Gjennomsnittstempereratur {mean_2014:.1f} celcius")
print(f"Høyeste temperatur {max_2014:.1f} celcius")
print(f"Laveste temperatur {min_2014:.1f} celcius")

# b)

def write_formatting(filename, list1, list2):
    with open(filename,"w") as f:
        for i, j in zip(list1,list2):
            f.write(f"{i} {j}\n")
write_formatting("temp_formatted.txt", temp_oct_1945, temp_oct_2014)



"""
Terminal> python .\temp_read_write.py
Temperatur i october 1945:
Gjennomsnittstempereratur 6.5 celcius
Høyeste temperatur 11.6 celcius
Laveste temperatur 2.1 celcius
----------------------------------------
Temperatur i october 2014
Gjennomsnittstempereratur 8.9 celcius
Høyeste temperatur 13.6 celcius
Laveste temperatur 2.3 celcius
"""
