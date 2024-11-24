import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy as sp


data = pd.read_csv("W10_CV_1um", sep='\t', skiprows=2, header=None)

data.columns = ["Voltage", "Capacitance", "Conductance", "Depth", "Doping Concentration"]

# fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))  # 2 rader, 2 kolonner



# Første plot: Spenning mot kapasitans
# ax1.plot(data["Voltage"], data["Capacitance"])
# ax1.set_xlabel("Bias (V)")
# ax1.set_ylabel("Capacitance (F)")
# ax1.set_title("Voltage vs Capacitance")

# # Andre plot: Spenning mot 1 / kapasitans^2
# ax2.plot(data["Voltage"], 1 / data["Capacitance"]**2)
# ax2.set_xlabel("Bias (V)")
# ax2.set_ylabel("1 / Capacitance² (F⁻²)")
# ax2.set_title("Voltage vs 1 / Capacitance²")

# regression = sp.stats.linregress(data["Voltage"], 1 / data["Capacitance"]**2)
# # print(regression)
# values = np.linspace(0, -16, 100)
# y = (regression.intercept) + (regression.slope * values)


# # Juster layout for å unngå overlapping
# # plt.tight_layout()
# # plt.show()

# # plt.plot(values, y)
# # plt.show()
# # print(regression)

# # print(1/data["Capacitance"]**2)

# Nd = 1.4e15
# epsilon = 11.8 * 8.85e-14
# Vbi = 0.395
# q = 1.6e-19

# W = np.sqrt(2 * epsilon * (Vbi + np.abs(data["Voltage"]))/ (q * Nd))
# print(W)

# plt.plot(data["Voltage"], W)
# plt.ylabel("Depletion Width (cm)")
# plt.xlabel("Bias (V)")
# plt.title("Depletion Width vs Bias")
# plt.show()


# filnavn_liste = [
#     "W10_IV_0_5mm", 
#     # "W10_IV_0_5mm_Ideality",
#     "W10_IV_0_5mm_Light_on",
#     # "W10_IV_1mm",
# ]
# for filnavn in filnavn_liste:
#     # Leser inn data
#     data = pd.read_csv(filnavn, sep="\t", header=None)
#     # Fjerner tomme rader
#     data = data.dropna()
#     # Setter kolonnenavn
#     data.columns = ["Vd", "Id"]
#     parts = filnavn.split("_")
#     label = "_".join(parts[2:])
#     # Use .iloc for slicing data correctly
#     Vd_segment = data["Vd"].iloc[2:7]
#     Id_segment = data["Id"].iloc[2:7]
#     # Apply linear regression
#     regression = sp.stats.linregress(Vd_segment, np.log(np.abs(Id_segment)))
#     # print(regression)
#     values = np.linspace(0, 0.5, 100)
#     y = np.exp(regression.intercept) * np.exp(regression.slope * values)

#     # Plot the data and fitted line
#     # plt.figure()  # Create a new figure for each plot
#     plt.plot(data["Vd"], np.abs(data["Id"]), label=label, marker="o")
#     # plt.plot(values, y, label = f"LinReg: {((regression.slope)):.2f}V {((regression.intercept)):.2f}", linestyle='--')

#     # Set labels and title
#     plt.title("IV Curve 0.5mm illuminatied and dark") 
#     plt.yscale("log")
#     # plt.xlim(0, 1)
#     plt.xlabel("Bias [V]")
#     plt.ylabel("I [A]")
#     plt.legend()
# plt.show()
# # Filnavn og laster inn data
# filnavn = "W10_Vd_08V_2_5um_gm"
# data = pd.read_csv(filnavn, sep='\t', header=None)

# # Parsing the filename to create a label
# parts = filnavn.split("_")
# label = "_".join(parts[2:-1])

# # Setting column names
# data.columns = ["Vgs", "Id"]

# # Plotting the original data
# plt.plot(data["Vgs"], data["Id"], label=label, marker="o")

# # Selecting the linear region (e.g., focusing on Vgs between 0.3V and 0.9V)
# linear_region = data[(data["Vgs"] >= 0.3) & (data["Vgs"] <= 0.9)]

# # Performing linear regression on the selected linear region
# slope, intercept, r_value, p_value, std_err = sp.stats.linregress(linear_region["Vgs"], linear_region["Id"])

# # Calculating the threshold voltage (Vt) as the x-intercept where Id = 0
# Vt = -intercept / slope
# gm = slope

# # Extending the linear fit line to reach Vgs = 0 for better visualization
# Vgs_fit = np.linspace(0, linear_region["Vgs"].max(), 100)
# Id_fit = slope * Vgs_fit + intercept

# # Plotting the linear fit
# plt.plot(Vgs_fit, Id_fit, 'r--', label=f'Linear Fit: {slope:.2e}V + {intercept:.2e}')

# # Adding labels and legend
# plt.xlabel("Vgs [V]")
# plt.ylabel("Id [A]")
# plt.title("I_D vs. V_GS with Linear Regression")
# plt.legend()
# plt.grid()

# # Displaying the threshold voltage (Vt)
# plt.axvline(x=Vt, color='g', linestyle=':', label=f'Threshold Voltage (Vt) = {Vt:.2f} V')
# plt.legend()
# plt.show()

# print(f"Threshold Voltage (Vt): {Vt:.2f} V")
# print(f"Transconductance (gm): {gm:.2e} A/V")


# Filnavn og laster inn data
filnavn = "W10_Vd_08V_2_5um_gm"
data = pd.read_csv(filnavn, sep='\t', header=None)

# Parsing the filename to create a label
parts = filnavn.split("_")
label = "_".join(parts[2:-1])

# Setting column names
data.columns = ["Vgs", "Id"]

# Plotting the original data
plt.plot(data["Vgs"], data["Id"], label="I_D vs V_GS", marker="o")

# Selecting the linear region (e.g., assuming Vgs > 0 for linear fit)
linear_region = data[(data["Vgs"] >= 0.4) & (data["Vgs"] <= 0.9)]

values = np.linspace(0, 0.9, 100)
# Performing linear regression on the linear region
slope, intercept, r_value, p_value, std_err = sp.stats.linregress(linear_region["Vgs"], linear_region["Id"])
V_T = -intercept / slope

# Plotting the linear fit
plt.plot(values, slope * values + intercept, 'r--', label=f'Linear Fit: {slope:.2e}V + {intercept:.2e}')
plt.axvline(x=V_T, color='g', linestyle=':', label=f'Threshold Voltage (V_T) = {V_T:.2f} V')

# Adding labels and legend
plt.xlabel("Vgs [V]")
plt.ylabel("Id [A]")
plt.title("I_D vs. V_GS with Linear Regression")
plt.legend()
plt.tight_layout()
plt.grid()
plt.show()



# filnavn1 = [
    
#     "W10_Vg_1V_2_5um",
#     "W10_Vg_2V_2_5um",
#     "W10_Vg_3V_2_5um",
#     "W10_Vg_4V_2_5um",
#     "W10_Vg_5V_2_5um",
# ]

# for filnavn in filnavn1:
#     # Leser inn data
#     parts = filnavn.split("_")
#     label = "_".join(parts[2:])
#     data = pd.read_csv(filnavn, sep="\t", header=None)
#     # Fjerner tomme rader
#     data = data.dropna()
#     # Setter kolonnenavn
#     data.columns = ["Vd", "Id"]
#     # Plotter data
#     plt.plot(data["Vd"], data["Id"], label=label)
# plt.title("MOSFET IV curve, 2.5um")
# plt.xlabel("Vds [V]")
# plt.ylabel("Id [A]")
# plt.legend()
# plt.show()

# filnavn2 = [
#     "W10_Vg_1V_5um",
#     "W10_Vg_2V_5um",
#     "W10_Vg_3V_5um",
#     "W10_Vg_4V_5um",
#     "W10_Vg_5V_5um",
# ]

# for filnavn in filnavn2:
#     # Leser inn data
#     data = pd.read_csv(filnavn, sep="\t", header=None)
#     # Fjerner tomme rader
#     data = data.dropna()
#     # Setter kolonnenavn
#     data.columns = ["Vd", "Id"]
#     # Plotter data
#     plt.plot(data["Vd"], data["Id"], label=filnavn)
# plt.xlabel("Vds [V]")
# plt.ylabel("Id [A]")
# plt.legend()
# plt.show()

# filnavn3 = [
#     "W10_Vg_1V_10um",
#     "W10_Vg_2V_10um",
#     "W10_Vg_3V_10um",
#     "W10_Vg_4V_10um",
#     "W10_Vg_5V_10um",
# ]
# for filnavn in filnavn3:
#     # Leser inn data
#     data = pd.read_csv(filnavn, sep="\t", header=None)
#     # Fjerner tomme rader
#     data = data.dropna()
#     # Setter kolonnenavn
#     data.columns = ["Vd", "Id"]
#     # Plotter data
#     plt.plot(data["Vd"], data["Id"], label=filnavn)
# plt.xlabel("Vds [V]")
# plt.ylabel("Id [A]")
# plt.legend()
# plt.show()

# filnavn4 = [
#     "W10_Vg_1V_20um",
#     "W10_Vg_2V_20um",
#     "W10_Vg_3V_20um",
#     "W10_Vg_4V_20um",
#     "W10_Vg_5V_20um",
# ]
# for filnavn in filnavn4:
#     # Leser inn data
#     data = pd.read_csv(filnavn, sep="\t", header=None)
#     # Fjerner tomme rader
#     data = data.dropna()
#     # Setter kolonnenavn
#     data.columns = ["Vd", "Id"]
#     # Plotter data
#     plt.plot(data["Vd"], data["Id"], label=filnavn)
# plt.xlabel("Vds [V]")
# plt.ylabel("Id [A]")
# plt.legend()
# plt.show()

# filnavn5 = [
    
#     "W10_Vg_1V_2_5um",
#     # "W10_Vg_1V_2_5um",
#     "W10_Vg_1V_5um",
#     "W10_Vg_1V_10um",
#     "W10_Vg_1V_20um",
# ]

# for filnavn in filnavn5:
#     # Leser inn data
#     parts = filnavn.split("_")
#     label = "_".join(parts[3:])
#     data = pd.read_csv(filnavn, sep="\t", header=None)
#     # Fjerner tomme rader
#     data = data.dropna()
#     # Setter kolonnenavn
#     data.columns = ["Vd", "Id"]
#     # Plotter data
#     plt.plot(data["Vd"], data["Id"], label=label)
# plt.title("MOSFET IV curve, 1V Vg")
# plt.xlabel("Vds [V]")
# plt.ylabel("Id [A]")
# plt.legend()
# plt.show()
