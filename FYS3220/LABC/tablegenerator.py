from tabulate import tabulate
import latextable
from texttable import Texttable

# example code for latex table:

printtable = [
    ["Name", "Age", "Nickname"],
    ["Albert Einstein", 76, "E=mc^2 Master"],
    ["Niels Bohr", 77, "Quantum Guru"],
    ["Isaac Newton", 84, "Calculus Creator"],
    ["Marie Curie", 66, "Radium Queen"],
    ["Richard Feynman", 69, "Quantum Cowboy"],
    ["James Clerk Maxwell", 48, "Electro-Magician"]
]

table_1 = Texttable()
table_1.set_cols_align(["c" for i in range(len(printtable[0]))])
table_1.set_cols_valign(["m" for i in range(len(printtable[0]))])
table_1.add_rows(printtable)

# Output for Texttable (Terminal)
print('-- Example 1: Basic --')
print('Texttable Output:')  
print(table_1.draw())

# Output for Latextable
print('\nLatextable Output:')
print(latextable.draw_latex(table_1, caption="An example table.", label="table:example_table"))

# Output for Markdown using tabulate
print('\nMarkdown Output:')
print(tabulate(printtable[1:], headers=printtable[0], tablefmt="pipe"))