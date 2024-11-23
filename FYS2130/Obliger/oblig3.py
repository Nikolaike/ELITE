import numpy as np
import matplotlib.pyplot as plt 
import scipy as sp

f_sig = 250 # Hz (assuming a harmonic oscillation)
omega_sig = 2*np.pi*f_sig
A = 1.0 # Amplitude

# samplings parametre
T = 1.5 # total samplingstid
f_samp = 1000 # samplingsfrekvens
t = np.linspace(0, T, int(T*f_samp)) # diskrete tidspunkter for sampling
N = len(t) # antall punkter
g = A*np.sin(omega_sig*t) # signal


fft = np.fft.fft(g) / N # fouriertransformasjon
dt = T/N

freq_correct = np.fft.fftfreq(N, dt) # frekvensakse

# plt.plot(np.abs(freq_correct), np.abs(fft))
# plt.xlim(200, 300)
# plt.xlabel('f [Hz]')
# plt.ylabel('x_k')
# plt.title('Fouriertransformasjon av sinussignal')
# plt.show()


# f_sig = [450, 1300, 1700]

# for i in f_sig:
#     omega_sig = 2*np.pi*i
#     g = A*np.sin(omega_sig*t) # signal
#     fft = np.fft.fft(g) / N
#     N = len(t)
#     freq_correct = np.fft.fftfreq(N, dt)
#     plt.plot(np.abs(freq_correct), np.abs(fft), label = f"Frequency: {i} Hz")
# plt.legend()
# plt.xlabel('f [Hz]')
# plt.ylabel('x_k')
# plt.title('Fouriertransformasjon av sinussignal')
# plt.show()


A_1 = 1
A_2 = 1.6
f_1 = 125
f_2 = 200
t_1= 0.25
t_2 =0.75
sigma_1 = 0.05
sigma_2 = 0.025
N = 2

f_t = A_1 * np.sin(2*np.pi * f_1 * t) * np.exp(-((t - t_1)/sigma_1)**2) + A_2 * np.sin(2*np.pi * f_2 * t) * np.exp(-((t - t_2)/sigma_2)**2)

signalbit_1, signalbit_2 = np.split(f_t, N)

len_f_t = len(f_t)

fft_1 = np.fft.fft(signalbit_1) / len_f_t
fft_2 = np.fft.fft(signalbit_2) / len_f_t
freq_correct = np.fft.fftfreq(int(len_f_t/2), dt)

# fig, ax = plt.subplots(2,1, figsize = (12, 5))
# ax[0].set_title("FFT for t1 = 0.75 and t2 = 1")
# ax[0].grid(1)
# ax[1].grid(1)
# ax[0].plot(np.abs(freq_correct), np.abs(fft_1))
# ax[0].plot(np.abs(freq_correct), np.abs(fft_2), ":")
# ax[0].set_xlabel('f [Hz]')
# ax[0].set_ylabel('x_k')

# ax[1].plot(t[:int(len(t)/2)], f_t[:int(len(t)/2)])
# ax[1].plot(t[int(len(t)/2):], f_t[int(len(t)/2):])
# ax[1].set_ylabel('X_n')
# ax[1].set_xlabel('t [s]')
# plt.show()


hann_funksjon = sp.signal.windows.hann(int(len_f_t/2))

signalbit_1 = signalbit_1 * hann_funksjon
signalbit_2 = signalbit_2 * hann_funksjon


vindu_størrelse = T / N

f_fft = np.fft.fftfreq(int(len_f_t/2), dt)
fft_1 = np.fft.fft(signalbit_1) / len_f_t
fft_2 = np.fft.fft(signalbit_2) / len_f_t
resultat = np.zeros((len(f_fft), N))
resultat[:, 0] = np.abs(fft_1)
resultat[:, 1] = np.abs(fft_2)


f = np.abs(f_fft)
f = np.append(f, f[-1] + (f[1] - f[0]))  # legger til et ekstra frekvenspunkt for å få riktig størrelse på f
t_plott = np.linspace(vindu_størrelse *.5 , T - vindu_størrelse*.5 , N)
t_plott = np.append(t_plott, t_plott[-1] + (t_plott[1] - t_plott[0]))  # legger til et ekstra tidspunkt for å få riktig størrelse på t

# plt.pcolormesh(t_plott , f , resultat, shading =  "auto")
# plt.colorbar(label="Amplitude [m]")  
# plt.xlabel('t [s]')
# plt.ylabel('f [Hz]')
# plt.title('Spectrogram med Hann-vindu')
# plt.show()   


def STFT(x_n, f_samp, overlapp, vindu_størrelse, Filter=False):
    # Antall punkter per vindu
    punkter_vindu = int(vindu_størrelse * f_samp)
    
    # Beregner antall vinduer gitt overlapp
    step = int(punkter_vindu * (1 - overlapp))
    totalt_antall_vindu = int(np.ceil((len(x_n) - punkter_vindu) / step)) + 1
    t_maks = len(x_n) / f_samp
    # Padder signalet med nuller for å få plass til det siste vinduet
    padding = np.zeros(punkter_vindu + (totalt_antall_vindu - 1) * step - len(x_n))
    x_n_pad = np.concatenate((x_n, padding))
    
    # Lager et Hann-vindu eller et vindu med bare 1-ere avhengig av Filter parameteren
    if Filter:
        vindu_funksjon = sp.signal.windows.hann(punkter_vindu)
    else:
        vindu_funksjon = np.ones(punkter_vindu)
    
    # Resultat array
    result = np.zeros((punkter_vindu // 2, totalt_antall_vindu))
    
    for i in range(totalt_antall_vindu):
        # Plukker ut bit av signalet med riktig overlapp
        start_index = i * step
        signalbit = x_n_pad[start_index:start_index + punkter_vindu]
        
        # Multipliserer med vindu-funksjon
        final_signalbit = vindu_funksjon * signalbit
        
        # FFT av signalbiten
        signalbit_FT = np.fft.fft(final_signalbit)
        
        # Lagrer FFT i resultatmatrisen. Vi er kun interessert i resultatet for positive frekvenser.
        result[:, i] = np.abs(signalbit_FT[:punkter_vindu // 2]) * 2 / punkter_vindu
    
    # Lager en tidsakse
    # t = np.linspace(0, len(x_n) / f_samp, totalt_antall_vindu)
    if overlapp == 0:
        t = np.linspace(vindu_størrelse / 2, t_maks - vindu_størrelse / 2, totalt_antall_vindu)
    else:
        t = np.linspace(vindu_størrelse / 3, t_maks + vindu_størrelse / 3, totalt_antall_vindu)
    # Lager en frekvensakse
    f_positive = np.linspace(0, f_samp / 2, punkter_vindu // 2)
    
    return t, f_positive, result
    



x_n = f_t  # et eksempel signal

# test_t, test_f, test_result = STFT(x_n, f_samp, 0, 0.75, Filter = True)
# plt.pcolormesh(test_t, test_f, test_result, shading =  "auto")
# plt.colorbar(label="Amplitude [m]")
# plt.xlabel('t [s]')
# plt.ylabel('f [Hz]')
# plt.title('Test for funksjonen STFT')
# plt.show()


overlapp = 0.5 # 50% overlapp
vindu_størrelse = 0.02  # vindusstørrelse i sekunder
vindu_størrelse2 = 0.15 # vindusstørrelse i sekunder
t, f, resultat = STFT(f_t, f_samp, overlapp, vindu_størrelse, Filter = False)
t2, f2, resultat2 = STFT(f_t, f_samp, overlapp, vindu_størrelse2, Filter = False)

t = np.append(t, t[-1] + (t[1] - t[0]))  # legger til et ekstra tidspunkt for å få riktig størrelse på t
f = np.append(f, f[-1] + (f[1] - f[0]))  # legger til et ekstra frekvenspunkt for å få riktig størrelse på f
t2 = np.append(t2, t2[-1] + (t2[1] - t2[0]))  # legger til et ekstra tidspunkt for å få riktig størrelse på t
f2 = np.append(f2, f2[-1] + (f2[1] - f2[0]))  # legger til et ekstra frekvenspunkt for å få riktig størrelse på f

# Kjør koden (dette er kommentert ut fordi vi ikke har et ekte signal å bruke det på)


# fig, ax = plt.subplots(2,1, figsize = (12, 5))
# p1 = ax[0].pcolormesh(t, f, resultat, shading =  "auto")
# ax[0].set_xlabel('t [s]')
# ax[0].set_ylabel('f [Hz]')
# ax[0].set_title('Spectrogram with window size 0.02s, uten filter')
# p2 = ax[1].pcolormesh(t2, f2, resultat2, shading =  "auto")
# ax[1].set_xlabel('t [s]')
# ax[1].set_ylabel('f [Hz]')
# ax[1].set_title('Spectrogram with window size 0.15s, uten filter')
# fig.colorbar(p1, label="Amplitude [m]", ax = ax[0])
# fig.colorbar(p2, label="Amplitude [m]", ax = ax[1])
# plt.show()

t3, f3, resultat3 = STFT(f_t, f_samp, overlapp, vindu_størrelse, Filter = True)
t4, f4, resultat4 = STFT(f_t, f_samp, overlapp, vindu_størrelse2, Filter = True)

t3 = np.append(t3, t3[-1] + (t3[1] - t3[0]))  # legger til et ekstra tidspunkt for å få riktig størrelse på t
f3 = np.append(f3, f3[-1] + (f3[1] - f3[0]))  # legger til et ekstra frekvenspunkt for å få riktig størrelse på f
t4 = np.append(t4, t4[-1] + (t4[1] - t4[0]))  # legger til et ekstra tidspunkt for å få riktig størrelse på t
f4 = np.append(f4, f4[-1] + (f4[1] - f4[0]))  # legger til et ekstra frekvenspunkt for å få riktig størrelse på f

# Kjør koden (dette er kommentert ut fordi vi ikke har et ekte signal å bruke det på)


# fig, ax = plt.subplots(2,1, figsize = (12, 5))
# p1 = ax[0].pcolormesh(t3, f3, resultat3, shading =  "auto")
# ax[0].set_xlabel('t [s]')
# ax[0].set_ylabel('f [Hz]')
# ax[0].set_title('Spectrogram med vindu storrelse 0.02s, med filter')
# p2 = ax[1].pcolormesh(t4, f4, resultat4, shading =  "auto")
# ax[1].set_xlabel('t [s]')
# ax[1].set_ylabel('f [Hz]')
# ax[1].set_title('Spectrogram med vindu storrelse 0.15s, med filter')
# fig.colorbar(p1, label="Amplitude [m]", ax = ax[0])
# fig.colorbar(p2, label="Amplitude [m]", ax = ax[1])
# plt.show()

# print(np.shape(t3))   
# print(np.shape(t4))
# print(np.shape(resultat3.T))
# print(np.shape(resultat4.T))

# fig, ax = plt.subplots(2,1, figsize = (12, 5))
# p1 = ax[0].pcolormesh(t3[:149], f3[:10], resultat3, shading =  "gouraud")
# ax[0].set_xlabel('t [s]')
# ax[0].set_ylabel('f [Hz]')
# ax[0].set_title('Spectrogram med vindu størrelse 0.02s')
# p2 = ax[1].pcolormesh(t4[:19], f4[:75], resultat4, shading =  "gouraud")
# ax[1].set_xlabel('t [s]')
# ax[1].set_ylabel('f [Hz]')
# ax[1].set_title('Spectrogram med vindu størrelse 0.15s')
# fig.colorbar(p1, label="Amplitude [m]", ax = ax[0])
# fig.colorbar(p2, label="Amplitude [m]", ax = ax[1])
# plt.show()

# t0, f0, resultat100 = STFT(f_t, f_samp, 0, 0.02, Filter = True)
# t25, f25, resultat25 = STFT(f_t, f_samp, 0.25, 0.02, Filter = True)
# t50, f50, resultat50 = STFT(f_t, f_samp, 0.5, 0.02, Filter = True)
# t75, f75, resultat75 = STFT(f_t, f_samp, 0.75, 0.02, Filter = True)

# fig, ax = plt.subplots(2,2, figsize = (12, 5))
# p1 = ax[0, 0].pcolormesh(t25, f25, resultat25, shading =  "auto", label = "0.25 overlapp")
# ax[0,0].set_xlabel('t [s]')
# ax[0,0].set_ylabel('f [Hz]')
# p2 = ax[0,1].pcolormesh(t50, f50, resultat50, shading =  "auto", label = "0.5 overlapp")
# ax[0,1].set_xlabel('t [s]')
# ax[0,1].set_ylabel('f [Hz]')
# p3 = ax[1,0].pcolormesh(t75, f75, resultat75, shading =  "auto", label = "0.75 overlapp")
# ax[1,0].set_xlabel('t [s]')
# ax[1,0].set_ylabel('f [Hz]')
# p4 = ax[1,1].pcolormesh(t0, f0, resultat100, shading = "auto", label = "0 overlapp")
# ax[1,1].set_xlabel('t [s]')
# ax[1,1].set_ylabel('f [Hz]')

# ax[0,0].set_title('0.25 overlapp')
# ax[0,1].set_title('0.5 overlapp')
# ax[1,0].set_title('0.75 overlapp')
# ax[1,1].set_title('0 overlapp')
# fig.colorbar(p1, label="Amplitude [m]", ax = ax[0])
# fig.colorbar(p2, label="Amplitude [m]", ax = ax[1])
# plt.show()




from scipy.io import wavfile

samplerate, data = wavfile.read("mistle_thrush.wav") # duetrost
x_n = data[: , 0] # velg en av to kanaler
f_samp = samplerate

t = np.linspace(0, len(x_n) / f_samp, len(x_n))

duetrost_fft = np.fft.fft(x_n) / len(x_n)
freq_correct = np.fft.fftfreq(len(x_n), 1/f_samp)

fig, ax = plt.subplots(2,1, figsize = (12, 5))
p1 = ax[0].plot(np.abs(freq_correct), np.abs(duetrost_fft))
ax[0].set_xlabel("f [Hz]")
ax[0].set_ylabel('x_k')
ax[0].set_xlim(0, 5000)
ax[0].set_title('')
p2 = ax[1].plot(t, x_n)
ax[1].set_xlabel('t [s]')
ax[1].set_ylabel('x_n')
plt.show()

print(f_samp)


t1 = 0.1
t2 = 0.4

t, f, resultat = STFT(x_n, f_samp, 0.5, 0.02, Filter = True)

fig, ax = plt.subplots(2,1, figsize = (12, 5))
p1 = ax[0].pcolormesh(t, f, resultat, shading =  "auto")
ax[0].set_xlabel("t [s]")
ax[0].set_ylim(0, 5000)
ax[1].set_ylim(0, 5000)
ax[0].set_ylabel('f [Hz]')
ax[0].set_title('Hele signalet')
p2 = ax[1].pcolormesh(t, f, resultat, shading =  "gouraud")
ax[1].set_xlabel('t [s]')
ax[1].set_ylabel('f [Hz]')
fig.colorbar(p1, label="Amplitude [m]", ax = ax[0])
fig.colorbar(p2, label="Amplitude [m]", ax = ax[1])
plt.show()


x_n = data[np.int_(t1*samplerate):np.int_(t2 * samplerate) , 0]
t2, f2, resultat2 = STFT(x_n, f_samp, 0.5, 0.02, Filter = True)
# fig, ax = plt.subplots(2,1, figsize = (12, 5))
# p1 = ax[0].pcolormesh(t2, f2, resultat2, shading =  "auto")
# ax[0].set_xlabel("t [s]")
# ax[0].set_ylim(0, 5000)
# ax[1].set_ylim(0, 5000)
# ax[0].set_ylabel('f [Hz]')
# ax[0].set_title('0.1 - 0.4 sekunder av signalet')
# p2 = ax[1].pcolormesh(t2, f2, resultat2, shading =  "gouraud")
# ax[1].set_xlabel('t [s]')
# ax[1].set_ylabel('f [Hz]')
# fig.colorbar(p1, label="Amplitude [m]", ax = ax[0])
# fig.colorbar(p2, label="Amplitude [m]", ax = ax[1])
# plt.show()




def punkter_vindu(x_n, f_samp, vindu_størrelse):
    return int(vindu_størrelse * f_samp)


from scipy import signal

f , t , Z = signal.stft(x_n , f_samp , nperseg = punkter_vindu(x_n, f_samp ,vindu_størrelse))

# fig, ax = plt.subplots(2,1, figsize = (12, 5))
# p1 = ax[0].pcolormesh(t2, f2, resultat2, shading =  "gouraud")
# ax[0].set_ylim(0, 5000)
# ax[0].set_xlabel('t [s]')
# ax[0].set_ylabel('f [Hz]')
# ax[0].set_title('Manually implemented STFT with window size 0.02s')
# p2 = ax[1].pcolormesh(t, f, np.abs(Z), shading =  "gouraud")

# ax[1].set_ylim(0, 5000)
# ax[1].set_xlabel('t [s]')
# ax[1].set_ylabel('f [Hz]')
# ax[1].set_title('scipy.signal.stft with window size 0.02s')
# fig.colorbar(p1, label="Amplitude [m]", ax = ax[0])
# fig.colorbar(p2, label="Amplitude [m]", ax = ax[1])
# plt.show()