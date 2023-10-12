import numpy as np
import time 
import itertools
import matplotlib.pyplot as plt

t = time.time()
sun, wind, hosp, fact, house = np.loadtxt('./forecast.csv', unpack=True, skiprows=1)


iter = itertools.combinations_with_replacement('012345678', 5)
sums = []
ens = []
for c in iter:
    s, w, h, f, h_ = map(int, c)
    if  s > 3 or s < 1 or w > 2 or h > 3 or f > 3 or h_ < 1:
        continue

    sum = 0
    energy = 0
    for i in range(len(sun)):
        energy += (s * sun[i]
            + w * wind[i]
            - h * hosp[i]
            - f * fact[i]
            - h_ * house[i])

        sum -= (10 * s * sun[i]
            + 10 * w * wind[i]
            - 5 * h * hosp[i]
            - 5 * f * fact[i]
            - 5 * h_ * house[i])
    if energy < 0:
        continue
    sums.append((sum/len(sun), c, energy))

sums = sorted(sums, key=lambda x: x[0])
print(sums[0])
print('----', time.time() - t, 'seconds ----')