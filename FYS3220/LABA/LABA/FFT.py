import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
import getopt

class FFT:
    """
    This class takes in a csv file with two columns, and plots the FFT of the signal.
    It also plots the peaks of the FFT and annotates the frequency and amplitude of each peak.
    """
    def __init__(self, file_name=None) -> None:
        self.file_name = file_name
        self._collect_data()
    
    def _collect_data(self):
        """
        This function reads in the csv file and extracts the time and voltage data.
        """
        # Read in the data
        data = pd.read_csv(self.file_name)

        # collects the header names
        header = data.columns

        # Extract the collumns from the DataFrame and converts to numpy arrays
        self.time = data[header[0]].to_numpy()
        
        if len(data.columns) < 4:
            self.voltage = data[header[1]].to_numpy()
        elif len(data.columns) > 3:
            print("the data has two header names, please specify which one is the voltage data")
            print("the options are: {:}".format(header[1:-1]))
            index_input = input("please write the index of the voltage data: 1/2/3/...")
            self.voltage = data[header[int(index_input)]].to_numpy()

    def _fft(self):
        """
        This function calculates the FFT of the signal.
        """
        # Calculate the FFT
        fft = np.fft.fft(self.voltage)

        # Calculate the frequency axis
        self.freq = np.fft.fftfreq(len(self.time), self.time[1] - self.time[0])

        # (optinaly) scales the amplitudes to be between 0 and 1
        try:
            self.fft = (fft / np.max(np.abs(fft))) * self.scaling_factor
        except AttributeError:
            self.fft = 2 / len(self.time) * np.abs(fft)
        
    def plot_fft(self, xlim_range=None, scaling_factor=None, peak_decimator=None, pltshow=True, return_dec=False):
        """
        This function plots the FFT of the signal.
        It also plots the peaks of the FFT and annotates the frequency and amplitude of each peak.
        """
        if scaling_factor:
            self.scaling_factor = scaling_factor
            plt.ylabel('Amplitude (Scaled)')
        else:
            plt.ylabel('Amplitude (FFT pure)')

        self._fft()

        self.return_dec = return_dec

        # Plot the results
        plt.plot(self.freq, np.abs(self.fft))
        plt.xlabel('Frequency (Hz)')

        # change the size of the plot
        if type(xlim_range) == tuple:
            try:
                plt.xlim(0, float(xlim_range[1]))
                self.xlim_range = float(xlim_range[1])
            except:
                plt.xlim(0, float(xlim_range[0]))
                self.xlim_range = float(xlim_range[0])
        elif xlim_range != None:
            plt.xlim(0, float(xlim_range))
            self.xlim_range = float(xlim_range)
        else:
            self.xlim_range = None
            plt.xlim(0, max(self.freq) + (max(self.freq) - min(self.freq))/10)
        
        if peak_decimator == None:
            plt.suptitle(f"FFT of {self.file_name}")
        else:
            self._plot_peaks(peak_decimator)

        if pltshow:
            plt.show()

    def _plot_peaks(self, peak_decimator):
        """
        This function plots the peaks of the FFT and annotates the frequency and amplitude of each peak.
        """
        # Find the peaks
        peaks = np.where(np.abs(self.fft) > max(self.fft)/peak_decimator)[0]

        # Plot the peaks
        plt.plot(self.freq[peaks], np.abs(self.fft[peaks]), 'ro')

        return_peaks = []
        # Annotate the peaks
        for i in peaks:
            plt.annotate(f"{self.freq[i]:.2f}, {np.abs(self.fft[i]):.2f}", (self.freq[i], np.abs(self.fft[i])))
            return_peaks.append((self.freq[i], np.abs(self.fft[i])))

        if self.return_dec:
            # [print(f"{i[0]:.1f}, {i[1]:.3f}") for i in return_peaks] # pretty print
            print(return_peaks)

        if self.xlim_range == None:
            # minimal distance between peaks
            min_dist = 100
            for i in peaks:
                for j in peaks:
                    if i != j:
                        min_dist = min(min_dist, abs(self.freq[i] - self.freq[j]))

            plt.xlim(0, max(self.freq[peaks]) + min_dist)

    def plot_time(self, xlim_range=None , pltshow=True):
        """
        This function plots the time and voltage data.
        """
        plt.plot(self.time, self.voltage)
        plt.xlabel('Time (s)')
        plt.ylabel('Voltage (V)')
        plt.suptitle(f"Time plot of {self.file_name}")

        # change the size of the plot
        if type(xlim_range) == tuple:
            try:
                plt.xlim(0, float(xlim_range[0]))
                self.xlim_range = float(xlim_range[0])
            except:
                plt.xlim(0, float(xlim_range[1]))
                self.xlim_range = float(xlim_range[1])
        elif xlim_range != None:
            plt.xlim(0, float(xlim_range))
            self.xlim_range = float(xlim_range)

        if pltshow:
            plt.show()

    def plot_both(self, xlim_range=None, scaling_factor=None, peak_decimator=None, pltshow=True):
        """
        This function plots the time and voltage data, as well as the FFT of the signal.
        It also plots the peaks of the FFT and annotates the frequency and amplitude of each peak.
        """
        plt.subplot(2, 1, 1)
        if xlim_range == None:
            self.plot_time(pltshow=False)
        else:
            self.plot_time(xlim_range=float(xlim_range[0]), pltshow=False)
        plt.subplot(2, 1, 2)
        if xlim_range == None:
            self.plot_fft(scaling_factor=scaling_factor, peak_decimator=peak_decimator, pltshow=False)
        else:
            self.plot_fft(xlim_range=float(xlim_range[1]), scaling_factor=scaling_factor, peak_decimator=peak_decimator, pltshow=False)
        plt.show()


if __name__ == "__main__":
 

    # define the command line arguments
    filename = None; xlim = None; scaling = None; peakd = None; plotting = None; show_window = True; return_dec = False
    argv = sys.argv[1:]
    try:
        options, args = getopt.getopt(argv, "f:x:s:d:p:w", ["filename=", "xlim=", "scaling=", "decimator=", "plotting=", "wait"])
    except getopt.GetoptError:
        print("Invalid option")
        sys.exit(1)
        
    # read in the command line arguments
    for name, value in options:
        if name in ['-f', '--filename']:
            filename = value
        if name in ['-x', '--xlim']:
            try:
                xlim = tuple(map(float, value.split(',')))
            except:
                xlim = float(value)
        if name in ['-s', '--scaling']:
            scaling = float(value)
        if name in ['-d', '--decimator']:
            if value == "yes" or value == "y":
                peakd = 3
            else:
                peakd = float(value)
        if name in ['-p', '--plotting']:
            if value == "fft" or value == "both" or value == "time":
                plotting = value
            elif value == "fftret" or value == "fftr" or value == "r":
                plotting = "fft"
                return_dec = True
            else:
                plotting = "fft"
        if name in ['-w', '--wait']:
            show_window = False

    # run the FFT
    fft = FFT(filename)
    if plotting == "time":
        fft.plot_time(xlim_range=xlim, pltshow=show_window)
    elif plotting == "fft":
        fft.plot_fft(xlim_range=xlim, scaling_factor=scaling, peak_decimator=peakd, pltshow=show_window, return_dec=return_dec)
    elif plotting == "both":
        fft.plot_both(xlim_range=xlim, scaling_factor=scaling, peak_decimator=peakd, pltshow=show_window)
    else:
        fft.plot_fft(xlim_range=xlim, scaling_factor=scaling, peak_decimator=peakd, pltshow=show_window)