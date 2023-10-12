import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Read the CSV files into Pandas DataFrames
pywt_dwt_df = pd.read_csv("pywt_dwt_duration.csv")
pywt_idwt_df = pd.read_csv("pywt_idwt_duration.csv")
wavelet_dwt_df = pd.read_csv("wavelet_dwt_duration.csv")
wavelet_idwt_df = pd.read_csv("wavelet_idwt_duration.csv")

# Create a dictionary to store the data in a plot-friendly format
def prepare_results(df):
    results = {
        'average_time': df['Average time'].tolist(),
        'max_time': df['Max time'].tolist(),
        'min_time': df['Min time'].tolist(),
        'std_dev': df['Standard deviation'].tolist()
    }
    return results

pywt_results = {
    'dwt': prepare_results(pywt_dwt_df),
    'idwt': prepare_results(pywt_idwt_df)
}

wavelet_results = {
    'dwt': prepare_results(wavelet_dwt_df),
    'idwt': prepare_results(wavelet_idwt_df)
}

x = pywt_dwt_df['Length'].tolist()

# Plot average time
plt.plot(x, pywt_results['dwt']['average_time'], label='pywt dwt', color='purple')

# Fill between for standard deviation
plt.fill_between(x, [avg - std for avg, std in zip(pywt_results['dwt']['average_time'], pywt_results['dwt']['std_dev'])], 
                 [avg + std for avg, std in zip(pywt_results['dwt']['average_time'], pywt_results['dwt']['std_dev'])],
                 alpha=0.3, color='purple')

# Thin line for max and min time
# plt.plot(x, pywt_results['dwt']['max_time'], alpha=0.3)
plt.plot(x, pywt_results['dwt']['min_time'], alpha=0.3, color='purple')

# Repeat for wavelet
plt.plot(x, wavelet_results['dwt']['average_time'], label='wavelet dwt', color='green')

plt.fill_between(x, [avg - std for avg, std in zip(wavelet_results['dwt']['average_time'], wavelet_results['dwt']['std_dev'])],
                    [avg + std for avg, std in zip(wavelet_results['dwt']['average_time'], wavelet_results['dwt']['std_dev'])],
                    alpha=0.3, color='green')

# plt.plot(x, wavelet_results['dwt']['max_time'], alpha=0.3)
plt.plot(x, wavelet_results['dwt']['min_time'], alpha=0.3, color='green')

plt.legend()
plt.xlabel('Length of input array')
plt.ylabel('Time taken (s)')
plt.title('DWT comparison')

plt.show()