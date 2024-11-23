#a)

elements_10 = {1: "-", 2: "Helium", 3: "Lithium",
4: "Beryllium", 5: "Boron", 6: "Carbon",
7: "Nitrogen", 8: "-",
9: "Fluorine", 10: "Neon"}
elements_10[1] = "Hydrogen"
elements_10[8] = "Oxygen"

#b)

elements_10_copy = elements_10.copy()
elements_10_copy.update({11: "Sodium"})
print(elements_10)
print("\n")

elements_11 = elements_10
elements_11.update({11: "Sodium"})
print(elements_10)

"""
Forskjellen mellom dem er at den første ikke får sodium i outputen, men
den andre får sodium.

Grunnen til dette er at når man bruker .copy får man en kopi av den originale
dictionary og når man da endrer på den kopien endrer ikke det på den originale,
hvis det hadde vært print(elements_10_copy) hadde man fått den samme outputen

Når man bruker = vil man også få en kopi, men når man endrer på kopien vil det
også endre på den originale

"""
"""
Terminal> python .\chemical_elements_dict.py
{1: 'Hydrogen', 2: 'Helium', 3: 'Lithium', 4: 'Beryllium', 5: 'Boron', 6:
 'Carbon', 7: 'Nitrogen', 8: 'Oxygen', 9: 'Fluorine', 10: 'Neon'}


{1: 'Hydrogen', 2: 'Helium', 3: 'Lithium', 4: 'Beryllium', 5: 'Boron', 6:
 'Carbon', 7: 'Nitrogen', 8: 'Oxygen', 9: 'Fluorine', 10: 'Neon', 11: 'Sodium'}

"""
