import numpy as np
from scipy.stats import binom

n = 10  # number of trials
p = 0.5 # probability of success

k_values = np.arange(0, n + 1)

pmf_values = binom.pmf(k_values, n, p)

total_probability = np.sum(pmf_values)

print(f"Outcomes: {k_values}")
print(f"Total Probability Sum: {total_probability}")
