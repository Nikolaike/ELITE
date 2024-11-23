import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm


data = []
np.linspace(1,2,100)
with open("tid.csv" , "r") as infile:
    next(infile)
    for line in infile:
        line = line.split(";")
        data.append(line[1])
        data[-1]= data[-1].replace("00:00:", "")
        data[-1] = float(data[-1])

data = data[1:-1]
mean, sd = np.mean(data), np.std(data)
dx = 0.01
x_axis = np.linspace(min(data),max(data), 100)

avg = sum(data)/len(data)
print(avg)

plt.hist(data, density=True)
plt.plot(x_axis, norm.pdf(x_axis, mean, sd), color="red",label="normalfordeling")
plt.xlabel("Periodetid (s)")
plt.ylabel("Frekvenstetthet")
plt.legend()
plt.savefig("histogram.png")
