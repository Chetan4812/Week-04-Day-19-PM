# Week-04-Day-19-PM


## Part A — Concept Application (40%)

1. **Generate a synthetic dataset** (size = 1000) from a normal distribution using NumPy.
    *   Compute mean, variance, and standard deviation.
    *   Plot histogram and observe distribution shape.
[solution](mean_var_sd_usng_nmpy.py)
  
2. **Implement Probability Mass Function (PMF)** for a discrete distribution (e.g., Bernoulli or Binomial).
    *   Verify that total probability sums to 1.
[solution](pmf.py)
  
3. **Implement Probability Density Function (PDF)** of a normal distribution manually (without using built-in functions).
[solution](pdf.py)

4. Given a **dataset**, compute and interpret:
    *   Mean
    *   Median
    *   Mode
    *   Skewness (basic interpretation: left/right skew)
[solution](mean_mdn_mode_skwns.py)

5. **Simulate a real-world scenario:**
    *   Toss a coin 1000 times.
    *   Estimate probability of heads.
    *   Compare with theoretical probability.
[solution](simulate_tosses.py)  

---

## Part B — Stretch Problem (30%)

**Simulate and compare distributions:**

1. **Generate samples from:**
    *   Normal distribution
    *   Uniform distribution
[solutiion](normal_uniform_distn.py)

2. **Plot both distributions and compare:**
    *   Shape
    *   Spread
    *   Central tendency

Distribution Comparison

| Feature | Normal (Gaussian) | Uniform (Rectangular) |
| :--- | :--- | :--- |
| **Shape** | Bell-shaped and symmetric. Most data points are near the center. | Flat/Constant. Every value in the range has an equal chance of occurring. |
| **Spread** | Theoretically infinite, but 99.7% of data falls within $\pm 3\sigma$. | Strictly bounded between the defined low and high limits. |
| **Central Tendency** | Strong. Mean, median, and mode are all at the peak. | Weak. While the mean is the center, there is no single "most frequent" peak (no mode). |


3. **Explain:**
    *   When would you use each distribution in real-world problems?
Real-World Use Cases

#### When to use Normal Distribution
Use this for phenomena influenced by many small, independent random factors (Central Limit Theorem).
*   **Biological Traits:** Human height, weight, or blood pressure.
*   **Standardized Testing:** IQ scores or SAT results.
*   **Measurement Errors:** Small fluctuations in scientific instruments.

#### When to use Uniform Distribution
Use this when every outcome in a specific range is equally likely.
*   **Random Sampling:** Picking a winner from a list where everyone has one ticket.
*   **Physical Randomness:** The position of a spinner or rolling a fair die.
*   **Cryptography:** Generating raw random keys or "nonces" where predictability must be zero across the entire range.
Use code with caution.


---

## Part C — Interview Ready (20%)

**Q1 — What is the difference between PMF and PDF?**

The fundamental difference lies in the type of random variable they describe:

| Feature | Probability Mass Function (PMF) | Probability Density Function (PDF) |
| :--- | :--- | :--- |
| **Data Type** | Discrete (countable values like 1, 2, 3). | Continuous (infinite values like 1.245...). |
| **Interpretation** | Gives the exact probability of a specific outcome. | Gives the density; probability at a single point is always 0. |
| **Calculation** | Read directly from the function. | Probability is the area under the curve over an interval. |
| **Summation** | All probabilities sum to 1. | The integral over the entire range equals 1. |
| **Example** | Rolling a die, number of children. | Human height, temperature, time. |



**Q2 (Coding) — Write a function to compute probability of an event from frequency data (relative frequency approach).**
[Code](prob_from_freq_data.py)

**Q3 — What is the Central Limit Theorem? Why is it important in machine learning?**
#### Definition:
The **Central Limit Theorem** states that if you take sufficiently large random samples from any population (regardless of its original distribution), the distribution of the sample means will behave like a **Normal Distribution**. 

### Why it is important in Machine Learning:
*   **Algorithm Assumptions:** Many ML models (like Linear Regression and LDA) assume that the residuals or underlying data features are normally distributed. CLT justifies this assumption.
*   **Hypothesis Testing:** It allows us to calculate **Confidence Intervals** and **p-values**, which are critical for model evaluation and feature selection.
*   **Error Estimation:** It helps in estimating the "Standard Error" of a model's performance, giving us an idea of how much a model's accuracy might fluctuate with different training sets.
*   **Handling Noise:** Since many real-world "noise" factors are the sum of many small random errors, CLT suggests that this noise will often be **Gaussian**, making it easier to filter out.

---

## Part D — AI-Augmented Task (10%)

1. **Prompt AI:**  
   "Explain probability distributions (normal, uniform, binomial) with Python visualizations."
2. **Document prompt and output**

"Prompt: Explain probability distributions (normal, uniform, binomial) with Python visualizations."
  [AI output](ai_output.md)

4. **Evaluate:**
    *   Are the explanations correct?
    *   Are the visualizations meaningful and accurate?

### 1. Accuracy of Explanations
*   Each distribution is correctly categorized by its type (Continuous vs. Discrete).
*   The key parameters ($\mu, \sigma$ for Normal; $a, b$ for Uniform; $n, p$ for Binomial) are identified correctly. These are the levers that define the shape of each distribution.
*   The examples provided (heights for Normal, dice for Uniform, coin flips for Binomial) are the "gold standard" educational examples used to help learners anchor abstract math to reality.

### 2. Meaningfulness of Visualizations
*   **Normal Distribution:** Using `norm.pdf` with a shaded `fill_between` clearly illustrates the "Area Under the Curve" concept, which is essential for understanding continuous probabilities.
*   **Uniform Distribution:** The visualization correctly shows the "shelf" shape. By including a small buffer on the x-axis (from -2 to 12 for a 0-10 range), it accurately demonstrates that the probability is zero outside the defined bounds.
*   **Binomial Distribution:** Using a Bar Plot (`plt.bar`) instead of a line plot is a critical distinction. It visually reinforces that this is a discrete distribution—you can have 5 heads or 6 heads, but never 5.5.

### 3. Technical Correctness of Code
*   **Libraries:** The code correctly utilizes `scipy.stats` for the mathematical heavy lifting and `numpy` for data generation, which is the industry-standard stack for data science in Python.
*   **Functions:** It correctly distinguishes between `.pdf()` (Probability Density Function) for continuous data and `.pmf()` (Probability Mass Function) for discrete data.















