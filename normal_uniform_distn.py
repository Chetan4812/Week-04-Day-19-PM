import numpy as np
import matplotlib.pyplot as plt

normal_data = np.random.normal(loc=0, scale=1, size=5000)
uniform_data = np.random.uniform(low=-2, high=2, size=5000)

# Plotting
fig, ax = plt.subplots(1, 2, figsize=(12, 4))

ax[0].hist(normal_data, bins=50, color='skyblue', edgecolor='black')
ax[0].set_title("Normal Distribution (μ=0, σ=1)")

ax[1].hist(uniform_data, bins=50, color='salmon', edgecolor='black')
ax[1].set_title("Uniform Distribution (Low=-2, High=2)")

plt.show()
