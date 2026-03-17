import numpy as np

def manual_normal_pdf(x, mu, sigma):
    """
    Manually calculates the PDF of a normal distribution.
    
    Parameters:
    x (float or array): The point(s) to evaluate.
    mu (float): The mean of the distribution.
    sigma (float): The standard deviation.
    """

    coefficient = 1 / (sigma * np.sqrt(2 * np.pi))
    exponent = np.exp(-0.5 * ((x - mu) / sigma)**2)
    
    return coefficient * exponent

x = 0
density = manual_normal_pdf(x, mu=0, sigma=1)
print(f"Density at x={x}: {density:.4f}") # Should be ~0.3989
