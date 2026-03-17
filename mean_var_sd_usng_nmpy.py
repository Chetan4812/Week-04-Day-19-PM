import numpy as np
import matplotlib.pyplot as plt

data = np.random.normal(loc=0, scale=1, size=1000)

mean = np.mean(data)
variance = np.var(data)
std_dev = np.std(data)

# Plot histogram
plt.hist(data, bins=30, color='skyblue', edgecolor='black', alpha=0.7)
plt.title('Histogram of Synthetic Normal Distribution (n=1000)')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()
