import wavelets as wl
import time
import csv
import pywt
import numpy as np

lengths = [100, 200, 300, 400, 500, 600, 700, 800, 900]
lengths += [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000]
loops = 100000

# create a csv file to store the results
with open('./speed_tests/pywt_dwt_duration.csv', mode='w') as results_file:
    results_writer = csv.writer(results_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    results_writer.writerow(['Length', 'Average time', 'Max time', 'Min time', 'Standard deviation'])

    for length in lengths:
        x = np.random.rand(length)
        # time the function
        times = []
        for i in range(loops):
            start = time.time()
            ca, cd = pywt.dwt(x, 'db1')
            end = time.time()
            times.append(end-start)

        results_writer.writerow([str(length), str(sum(times)/len(times)), str(max(times)), str(min(times)), str(np.std(times))])

print("pywt dwt done")

with open('./speed_tests/wavelet_dwt_duration.csv', mode='w') as results_file:
    results_writer = csv.writer(results_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    results_writer.writerow(['Length', 'Average time', 'Max time', 'Min time', 'Standard deviation'])

    for length in lengths:
        x = np.random.rand(length)
        # time the function
        times = []
        lpf_D, hpf_D, lpf_R, hpf_R =wl.getFilters("db1")
        for i in range(loops):
            start = time.time()
            ca, cd = wl.dwt(x, lpf_D, hpf_D)
            end = time.time()
            times.append(end-start)

        results_writer.writerow([str(length), str(sum(times)/len(times)), str(max(times)), str(min(times)), str(np.std(times))])

print("wavelet dwt done")

with open('./speed_tests/pywt_idwt_duration.csv', mode='w') as results_file:
    results_writer = csv.writer(results_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    results_writer.writerow(['Length', 'Average time', 'Max time', 'Min time', 'Standard deviation'])

    for length in lengths:
        x = np.random.rand(length)
        ca, cd = pywt.dwt(x, 'db1')
        # time the function
        times = []
        for i in range(loops):
            start = time.time()
            pywt.idwt(ca, cd, 'db1')
            end = time.time()
            times.append(end-start)

        results_writer.writerow([str(length), str(sum(times)/len(times)), str(max(times)), str(min(times)), str(np.std(times))])

print("pywt idwt done")

with open('./speed_tests/wavelet_idwt_duration.csv', mode='w') as results_file:
    results_writer = csv.writer(results_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    results_writer.writerow(['Length', 'Average time', 'Max time', 'Min time', 'Standard deviation'])

    for length in lengths:
        x = np.random.rand(length)
        ca, cd = wl.dwt(x, lpf_D, hpf_D)
        # time the function
        times = []
        for i in range(loops):
            start = time.time()
            wl.idwt(ca, cd, len(x), lpf_R, hpf_R)
            end = time.time()
            times.append(end-start)

        results_writer.writerow([str(length), str(sum(times)/len(times)), str(max(times)), str(min(times)), str(np.std(times))])