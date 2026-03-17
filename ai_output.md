To explain probability distributions, we look at how data points are spread out and how likely each value is to occur. Below is a breakdown of the three most common distributions with Python visualizations.

### 1. Normal Distribution (Gaussian)
The Normal Distribution is a continuous distribution that is symmetric and bell-shaped. Most observations cluster around the central peak (the mean).

*   **Real-world Example:** Human height, standardized test scores.
*   **Key Parameters:** Mean ($\mu$) and Standard Deviation ($\sigma$).

```pyhton
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Generate data
mu, sigma = 0, 1
x = np.linspace(-4, 4, 100)
y = norm.pdf(x, mu, sigma)

plt.plot(x, y, color='blue', lw=2)
plt.fill_between(x, y, alpha=0.2, color='blue')
plt.title("Normal Distribution (Bell Curve)")
plt.show()
```

### 2. Uniform Distribution

In a Uniform Distribution, every value within a specific range $[a, b]$ has an equal probability of occurring. The shape is a flat rectangle. 

*   **Real-world Example:** Rolling a single fair die, or the "minutes" hand on a clock at a random glance.
*   **Key Parameters:** Lower bound ($a$) and Upper bound ($b$).

```python
from scipy.stats import uniform

# Generate data
low, width = 0, 10 # Range from 0 to 10
x = np.linspace(-2, 12, 100)
y = uniform.pdf(x, low, width)

plt.plot(x, y, color='red', lw=2)
plt.fill_between(x, y, alpha=0.2, color='red')
plt.title("Uniform Distribution (Equal Likelihood)")
plt.show()
```

### 3. Binomial Distribution
The Binomial Distribution is a discrete distribution. It represents the number of "successes" in a fixed number of independent trials (like coin flips). 

*   **Real-world Example:** Number of "heads" in 10 coin tosses.
*   **Key Parameters:** Number of trials ($n$) and probability of success ($p$). 

```python
from scipy.stats import binom

# Generate data
n, p = 10, 0.5
x = np.arange(0, n + 1)
y = binom.pmf(x, n, p)

plt.bar(x, y, color='green', alpha=0.7)
plt.title("Binomial Distribution (10 Coin Flips)")
plt.xlabel("Number of Successes")
plt.show()
```

### Summary Table


| Distribution | Type | Shape | Common Use Case |
| :--- | :--- | :--- | :--- |
| **Normal** | Continuous | Bell Curve | Modeling natural phenomena (Heights, Weights). |
| **Uniform** | Continuous | Rectangular | Random number generation, fair selection. |
| **Binomial** | Discrete | Step/Bar | Success/Failure outcomes (Yes/No events). |










