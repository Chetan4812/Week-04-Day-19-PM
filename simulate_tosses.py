import numpy as np

tosses = np.random.randint(0, 2, size=1000)
heads_count = np.sum(tosses)

estimated_probability = heads_count / 1000

theoretical_probability = 0.5

print(f"Total Heads: {heads_count}")
print(f"Estimated Probability: {estimated_probability}")
print(f"Theoretical Probability: {theoretical_probability}")
print(f"Difference (Error): {abs(theoretical_probability - estimated_probability):.4f}")
