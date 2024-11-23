import matplotlib.pyplot as plt
import h5py

# Load the data
with h5py.File('2024-07-19t015048.107000.h5', 'r') as hf:
    waveforms_group = hf['waveforms']
    key = list(waveforms_group.keys())[0]
    full_key = f"waveforms/{key}"
    dataset = hf[full_key][:]



shifted = dataset[10000:]

plt.plot(dataset)
plt.xlabel('n')
plt.ylabel('x(n)')
plt.title("Original dataset")
plt.legend()
plt.show()

plt.plot(dataset)
plt.xlim(70000, 110000)
plt.xlabel('n')
plt.ylabel('x(n)')
plt.title("Limited dataset")
plt.legend()
plt.show()


plt.plot(dataset, label='Original')
plt.plot(shifted, label='Shifted')
plt.xlim(70000, 110000)
plt.xlabel('n')
plt.ylabel('x(n)')
plt.title("Limited dataset")
plt.legend()
plt.show()