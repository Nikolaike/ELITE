# Requires the obspy and obspyh5 packages
#
# Can be installed through Conda:
#
# conda config --add channels conda-forge
# conda create -n obsh5 numpy obspy h5py scienceplots cartopy
# conda activate obsh5
# pip install obspyh5

import obspy
from obspy.clients.fdsn import Client
from obspy import UTCDateTime
import matplotlib.pyplot as plt
import scienceplots # For plot formatting

plt.style.use(['science', 'no-latex'])

# Define FDSN client for earthquake catalog loading
client = Client("IRIS")

# Define parameters for a significant earthquake search
min_magnitude = 6.8
t1 = UTCDateTime("2020-01-01T00:00:00")
t2 = UTCDateTime("2024-07-31T23:59:59")
Nevents = 100

# Load the catalog of events
event_catalog = client.get_events(starttime=t1, endtime=t2, minmagnitude=min_magnitude, limit=Nevents, orderby="time", includearrivals=True)

# Print event details
print(event_catalog.__str__(print_all=True))

event_catalog.plot(outfile='event_map.pdf')


# ---- Load data
#
#
data_client = Client("UIB-NORSAR") # A Norwegian data centre

# University of Oslo campus seismic station information
network = "NS"  
station = "OSL" 
location = "00" 
channel = "HHZ" 

# Loop over all events 
for this_event in event_catalog:

    # Define time window around the event origin time
    origin_time = this_event.origins[0].time
    start_time = origin_time - 5 * 60  # 5 minutes before origin time
    end_time = origin_time + 2 * 3600  # 2 hours after origin time
    
    # Get waveform data, decimate, and put into a trace vector
    st = data_client.get_waveforms(network=network, station=station, location=location, channel=channel, starttime=start_time, endtime=end_time)
    st.decimate(2)

    tr = st[0]
    print('f_T = ' + str(tr.stats.sampling_rate) + ' s')

    # Detrend and frequency bandpass
    tr.detrend('linear')
    tr.filter('bandpass', freqmin=0.05, freqmax=8)

    # Trim start and end to remove prospective filtering artefacts
    trimlength = 5
    tr.trim(starttime=start_time+trimlength, endtime=end_time+trimlength)

    # Save to HDF format
    fn = this_event.origins[0].time.isoformat() + '.h5'
    print('Saving ' + fn)
    tr.write(fn, 'H5')
