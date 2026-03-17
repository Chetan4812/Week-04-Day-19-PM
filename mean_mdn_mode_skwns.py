import numpy as np
from scipy import stats

# Sample Dataset
data = [45, 50, 55, 60, 60, 65, 70, 150] 

mean = np.mean(data)
median = np.median(data)
mode = stats.mode(data, keepdims=True).mode[0]
skewness = stats.skew(data)

print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}")
print(f"Skewness Score: {skewness:.2f}")
