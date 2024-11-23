import numpy as np

# Constants
# ???
# ???
# ???
R = 1e4
C = 10e-9
omega = 1 / (R * C)
# Initialize the table
table = []
header = ["G", "omega", "Q", "Re(pol1)", "Im(pol1)", "Re(pol2)", "Im(pol2)", "stability", "oscillation"]


# Function to round numbers and convert to int if decimal part is zero
def custom_round(num):
    rounded_num = round(num, 3)
    return int(rounded_num) if rounded_num == int(rounded_num) else rounded_num


# Initialize the table with corrected 'a' term and rounding
table_corrected = []
for G in np.arange(0, 7.25, 0.25):
    # Handle the case where Q would be infinite
    if G == 3:
        Q = "inf"
    else:
        Q = custom_round(1 / (3 - G))
    
    # seperate the terms to account for np.roots()
    a = (R*C)**2
    b = (3 - G) * R*C
    c = 1

    poles = np.roots([a, b, c])

    # Stability and oscillation
    stability = "Stable" if all(np.real(poles) < 0) else "Unstable" if all(np.real(poles) > 0) else "Marginally_Stable"
    oscillation = "No" if all(np.imag(poles) == 0) else "Dampened" if stability == "Stable" else "Constant" if stability == "Marginally_Stable" else "Increasing"

    # Append to table with rounded values
    table_row = [custom_round(G), custom_round(omega), Q]
    for pole in poles:
        table_row.extend([custom_round(np.real(pole)), custom_round(np.imag(pole))])
    table_row.extend([stability, oscillation])
    
    table_corrected.append(table_row)

# Function to format and print the table using f-strings for better readability
def print_pretty_table(table, header):
    # Determine the maximum width for each column
    col_widths = [max(len(str(x)) for x in col) for col in zip(*[header] + table)]
    
    # Print header with formatting
    header_str = ' | '.join(f"{str(item):<{col_widths[i]}}" for i, item in enumerate(header))
    print(header_str)
    print('-' * len(header_str))
    
    # Print each row with formatting
    for row in table:
        row_str = ' | '.join(f"{str(item):<{col_widths[i]}}" for i, item in enumerate(row))
        print(row_str)

# Print the complete table in a pretty format
print_pretty_table(table_corrected, header)
