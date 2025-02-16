import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.colors as mcolors
import mne
from scipy.signal import stft
from matplotlib.widgets import Button, Slider

# ------------------------
# PARAMETERS
# ------------------------
sfreq = 256  # Sampling frequency (Hz)
window_size = 5  # Time window in seconds for DSA (rolling)
freq_range = (0.5, 40)  # Frequency range (Hz)
nperseg = 256  # STFT window size
noverlap = 128  # STFT overlap
max_power = 20  # Max power in µV² (adjustable)

# ------------------------
# EEG SIGNAL SIMULATION
# ------------------------
def generate_eeg(signal_type, duration):
    """Generate different EEG patterns based on anesthesia type."""
    times = np.arange(0, duration, 1/sfreq)
    noise = 2 * np.random.randn(len(times))  # Baseline noise

    if signal_type == "Propofol":
        delta = 10 * np.sin(2 * np.pi * 1 * times)  # Strong delta (1 Hz)
        alpha = 7 * np.sin(2 * np.pi * 10 * times)  # Alpha spindles (10 Hz)
        eeg_signal = delta + alpha + noise

    elif signal_type == "Sevoflurane":
        delta = 15 * np.sin(2 * np.pi * 0.8 * times)  # Dominant delta (0.8 Hz)
        eeg_signal = delta + noise  # More slow-wave, less alpha

    elif signal_type == "Ketamine":
        gamma = 10 * np.sin(2 * np.pi * 40 * times)  # Gamma oscillations (40 Hz)
        eeg_signal = gamma + noise  # High-frequency activity

    return eeg_signal

# ------------------------
# LIVE PLOTTING SETUP
# ------------------------
fig, (ax_eeg, ax_dsa) = plt.subplots(2, 1, figsize=(10, 7))
plt.subplots_adjust(bottom=0.3)

# Initial EEG signal & type
eeg_type = "Propofol"
eeg_data = generate_eeg(eeg_type, window_size)

# ------------------------
# PLOTTING FUNCTIONS
# ------------------------
def update_plot(frame):
    global eeg_data

    # Simulate new EEG data
    new_eeg = generate_eeg(eeg_type, 1)  # Generate 1 second of new data
    eeg_data = np.roll(eeg_data, -sfreq)  # Shift left by 1 sec
    eeg_data[-sfreq:] = new_eeg  # Append new data

    # Update EEG Plot
    ax_eeg.clear()
    ax_eeg.plot(np.linspace(-window_size, 0, len(eeg_data)), eeg_data, color="black")
    ax_eeg.set_title(f"Simulated EEG - {eeg_type}")
    ax_eeg.set_xlabel("Time (s)")
    ax_eeg.set_ylabel("Amplitude (µV)")
    ax_eeg.set_xlim(-window_size, 0)
    ax_eeg.set_ylim(-30, 30)

    # Compute STFT for DSA
    f, t, Zxx = stft(eeg_data, sfreq, nperseg=nperseg, noverlap=noverlap)
    power = np.abs(Zxx) ** 2  # Convert to power
    power = np.clip(power, 0, max_power)  # Cap max power for visualization

    # Update DSA Plot
    ax_dsa.clear()
    ax_dsa.imshow(power, aspect="auto", extent=[-window_size, 0, freq_range[0], freq_range[1]],
                  cmap=cmap, origin="lower")

    ax_dsa.set_title("Density Spectral Analysis (DSA)")
    ax_dsa.set_xlabel("Time (s)")
    ax_dsa.set_ylabel("Frequency (Hz)")

# ------------------------
# BUTTON CALLBACKS
# ------------------------
def set_propofol(event):
    global eeg_type
    eeg_type = "Propofol"

def set_sevoflurane(event):
    global eeg_type
    eeg_type = "Sevoflurane"

def set_ketamine(event):
    global eeg_type
    eeg_type = "Ketamine"

def adjust_power(val):
    global max_power
    max_power = val

# ------------------------
# CUSTOM COLORMAP (BLUE → RED)
# ------------------------
colors = ["blue", "darkblue", "purple", "red"]  # Blue to pure red
cmap = mcolors.LinearSegmentedColormap.from_list("custom_cmap", colors, N=256)

# ------------------------
# GUI BUTTONS
# ------------------------
ax_propofol = plt.axes([0.1, 0.1, 0.2, 0.075])
ax_sevoflurane = plt.axes([0.4, 0.1, 0.2, 0.075])
ax_ketamine = plt.axes([0.7, 0.1, 0.2, 0.075])

btn_propofol = Button(ax_propofol, "Propofol")
btn_sevoflurane = Button(ax_sevoflurane, "Sevoflurane")
btn_ketamine = Button(ax_ketamine, "Ketamine")

btn_propofol.on_clicked(set_propofol)
btn_sevoflurane.on_clicked(set_sevoflurane)
btn_ketamine.on_clicked(set_ketamine)

# ------------------------
# POWER SCALING SLIDER
# ------------------------
ax_slider = plt.axes([0.1, 0.02, 0.65, 0.03])
slider = Slider(ax_slider, "DSA Power (µV²)", 1, 50, valinit=max_power)
slider.on_changed(adjust_power)

# ------------------------
# START ANIMATION
# ------------------------
ani = animation.FuncAnimation(fig, update_plot, interval=1000)  # Update every second
plt.show()
