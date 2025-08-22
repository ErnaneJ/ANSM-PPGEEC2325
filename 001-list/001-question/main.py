import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

def generate_uniform_sums(n, sample_size=10000):
    """
    Generate samples of the sum of 'n' independent uniform(0,1) variables.

    Parameters:
        n (int): Number of uniform variables to sum.
        sample_size (int): Number of samples to generate.

    Returns:
        np.ndarray: Array of summed samples.
    """
    return np.sum(np.random.uniform(0, 1, (sample_size, n)), axis=1)

def compute_statistics(samples):
    """
    Compute E[X], Var(X), and E[X^2] for a given sample.

    Parameters:
        samples (np.ndarray): Array of sample values.

    Returns:
        tuple: (mean, variance, second_moment)
    """
    mean = np.mean(samples)
    variance = np.var(samples)
    second_moment = np.mean(samples ** 2)
    return mean, variance, second_moment
  
def plot_pdf_cdf(samples, n):
    """
    Plot the PDF and CDF for a given sample of summed uniform variables.

    Parameters:
        samples (np.ndarray): Array of sample values.
        n (int): Number of uniform variables summed.
    """
    density = gaussian_kde(samples)
    x_vals = np.linspace(np.min(samples), np.max(samples), 1000)
    pdf_vals = density(x_vals)
    cdf_vals = np.cumsum(pdf_vals)
    cdf_vals /= cdf_vals[-1]  # Normalize

    plt.figure(figsize=(12, 5))

    # PDF
    plt.subplot(1, 2, 1)
    plt.plot(x_vals, pdf_vals)
    plt.title(f"PDF of Sum of {n} Uniform(0,1) variables")
    plt.xlabel("X")
    plt.ylabel("Density")

    # CDF
    plt.subplot(1, 2, 2)
    plt.plot(x_vals, cdf_vals)
    plt.title(f"CDF of Sum of {n} Uniform(0,1) variables")
    plt.xlabel("X")
    plt.ylabel("Cumulative Probability")

    plt.tight_layout()
    plt.show()
    
def analyze_distributions(max_n=12):
    """
    Run the analysis for sums of uniform variables from n=1 to n=max_n.

    Parameters:
        max_n (int): Maximum value of n to analyze.
    """
    for n in range(1, max_n + 1):
        samples = generate_uniform_sums(n)
        mean, var, second_moment = compute_statistics(samples)

        print(f"\n--- n = {n} ---")
        print(f"E[X]      = {mean:.4f}")
        print(f"Var[X]    = {var:.4f}")
        print(f"E[X^2]    = {second_moment:.4f}")

        plot_pdf_cdf(samples, n)
    
if __name__ == "__main__":
    analyze_distributions()