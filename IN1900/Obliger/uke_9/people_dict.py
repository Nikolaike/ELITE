#a)
def read_person_data(filename):
    d = {}
    with open(filename, "r") as infile:
        for line in infile:
            name,age,gender = line.split(" ")
            age,gender = info
            d[name] = info

    return d
print(read_person_data("people.txt"))
print(read_person_data("people.txt"))
#b)
"""def write_person_data(data_dict, filename):
    with open(filename, "w") as f:
        for i in data_dict:
            f.write(f"{i}")
            for a in data_dict[i]:
                f.write(f"{data_dict[i][d]}")
    f.write("\n")"""
"""
Terminal>python .\people_dict.py
{'John': {'Age': 55, 'Gender': 'Male'}, 'Toney': {'Age': 23, 'Gender': 'Male'},
 'Karin': {'Age': 42, 'Gender': 'Female'}, 'Cathie': {'Age': 29, 'Gender': 'Female'},
 'Rosalba': {'Age': 12, 'Gender': 'Female'}, 'Nina': {'Age': 50, 'Gender': 'Female'},
 'Burton': {'Age': 16, 'Gender': 'Male'}, 'Joey': {'Age': 90, 'Gender': 'Male'}}


"""
