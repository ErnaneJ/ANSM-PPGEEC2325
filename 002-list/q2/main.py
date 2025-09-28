import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import multivariate_normal
import os

os.makedirs('images', exist_ok=True)

def create_3d_plot(mu, P, title, filename):
    """Create 3D plot of the bivariate normal distribution"""
    # Convert P to numpy array for proper indexing
    P_array = np.array(P)
    
    x = np.linspace(mu[0] - 3*np.sqrt(P_array[0,0]), mu[0] + 3*np.sqrt(P_array[0,0]), 100)
    y = np.linspace(mu[1] - 3*np.sqrt(P_array[1,1]), mu[1] + 3*np.sqrt(P_array[1,1]), 100)
    X, Y = np.meshgrid(x, y)
    pos = np.dstack((X, Y))
    
    # Create multivariate normal distribution
    rv = multivariate_normal(mu, P_array)
    Z = rv.pdf(pos)
    
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    surf = ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('PDF')
    ax.set_title(title)
    plt.colorbar(surf, ax=ax, shrink=0.5, aspect=5)
    
    plt.savefig(f'images/{filename}_3d.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_contour_plot(mu, P, title, filename):
    """Create contour plot of the bivariate normal distribution"""
    
    P_array = np.array(P)
    x = np.linspace(mu[0] - 3*np.sqrt(P_array[0,0]), mu[0] + 3*np.sqrt(P_array[0,0]), 100)
    y = np.linspace(mu[1] - 3*np.sqrt(P_array[1,1]), mu[1] + 3*np.sqrt(P_array[1,1]), 100)
    X, Y = np.meshgrid(x, y)
    pos = np.dstack((X, Y))
    
    # Create multivariate normal distribution
    rv = multivariate_normal(mu, P_array)
    Z = rv.pdf(pos)
    
    plt.figure(figsize=(8, 6))
    contour = plt.contour(X, Y, Z, levels=10)
    plt.clabel(contour, inline=True, fontsize=8)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title(title)
    plt.grid(True, alpha=0.3)
    
    plt.savefig(f'images/{filename}_contour.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_scatter_plot(X, Y, title, filename):
    """Create scatter plot of samples"""
    
    plt.figure(figsize=(6, 5))
    plt.scatter(X, Y, alpha=0.3, s=1)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title(title)
    plt.grid(True, alpha=0.3)
    
    plt.savefig(f'images/{filename}_scatter.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_correlation_matrix(X, Y, title, filename):
    """Create correlation matrix heatmap"""
    corr_matrix = np.corrcoef([X, Y])
    
    plt.figure(figsize=(6, 5))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0,
                xticklabels=['X', 'Y'], yticklabels=['X', 'Y'])
    plt.title(f'{title} - Correlation Matrix')
    plt.savefig(f'images/{filename}_correlation.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_covariance_matrix(X, Y, title, filename):
    """Create covariance matrix heatmap"""
    cov_matrix = np.cov([X, Y])
    
    plt.figure(figsize=(6, 5))
    sns.heatmap(cov_matrix, annot=True, cmap='viridis',
                xticklabels=['X', 'Y'], yticklabels=['X', 'Y'])
    plt.title(f'{title} - Covariance Matrix')
    plt.savefig(f'images/{filename}_covariance.png', dpi=300, bbox_inches='tight')
    plt.close()

def analyze_samples(X, Y, mu, P, title, filename):
    """Create all plots for given samples"""
    create_scatter_plot(X, Y, title, filename)
    create_correlation_matrix(X, Y, title, filename)
    create_covariance_matrix(X, Y, title, filename)
    
    corr = np.corrcoef(X, Y)[0, 1]
    cov = np.cov(X, Y)[0, 1]
    print(f"{title}: Corr = {corr:.4f}, Cov = {cov:.4f}")
    print(f"Sample means: X = {np.mean(X):.4f}, Y = {np.mean(Y):.4f}")
    print(f"Theoretical means: X = {mu[0]}, Y = {mu[1]}")
    print(f"Sample covariance matrix:\n{np.cov([X, Y])}")
    print(f"Theoretical covariance matrix:\n{P}")
    print("-" * 50)

def question_2a(mu, P, samples):
    """2a) 3D plot of the PDF"""
    create_3d_plot(mu, P, "2a) 3D Plot of Bivariate Normal PDF", "2a")

def question_2b(mu, P, samples):
    """2b) Contour plot of the PDF"""
    create_contour_plot(mu, P, "2b) Contour Plot of Bivariate Normal PDF", "2b")

def question_2c(mu, P, samples):
    """2c) Compare with question 1j"""
    X, Y = samples.T
    
    np.random.seed(42) # Ensure reproducibility
    
    n_samples = 5000
    X_orig = np.random.normal(0, 1, n_samples)
    Y_orig = np.random.normal(0, 1, n_samples)
    
    # Apply transformation from 1j
    theta = np.pi/4
    W_1j = np.cos(theta) * (2*X_orig) - np.sin(theta) * Y_orig + 5
    Z_1j = np.sin(theta) * (2*X_orig) + np.cos(theta) * Y_orig + 3
    
    plt.figure(figsize=(12, 5))
    
    plt.subplot(1, 2, 1)
    plt.scatter(W_1j, Z_1j, alpha=0.3, s=1)
    plt.xlabel('W')
    plt.ylabel('Z')
    plt.title('1j) Transformed Variables')
    plt.grid(True, alpha=0.3)
    
    plt.subplot(1, 2, 2)
    plt.scatter(X, Y, alpha=0.3, s=1)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('2) Bivariate Normal Samples')
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('images/2c_comparison_1j.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    corr_1j = np.corrcoef(W_1j, Z_1j)[0, 1]
    cov_1j = np.cov(W_1j, Z_1j)[0, 1]
    corr_2 = np.corrcoef(X, Y)[0, 1]
    cov_2 = np.cov(X, Y)[0, 1]
    
    print("2c) Comparison with 1j:")
    print(f"1j - Corr = {corr_1j:.4f}, Cov = {cov_1j:.4f}")
    print(f"2  - Corr = {corr_2:.4f}, Cov = {cov_2:.4f}")
    print(f"Difference - Corr = {abs(corr_1j - corr_2):.4f}, Cov = {abs(cov_1j - cov_2):.4f}")
    print("-" * 50)

def question_2d(mu, P, samples):
    """2d) Adjust P to match question 1k"""
    
    np.random.seed(42) # Ensure reproducibility
    
    n_samples = 5000
    X_orig = np.random.normal(0, 1, n_samples)
    Y_orig = np.random.normal(0, 1, n_samples)
    
    # Apply transformation from 1k
    theta = 3*np.pi/4
    W_1k = np.cos(theta) * (2*X_orig) - np.sin(theta) * Y_orig + 5
    Z_1k = np.sin(theta) * (2*X_orig) + np.cos(theta) * Y_orig + 3
    
    # Calculate target covariance matrix
    target_cov = np.cov([W_1k, Z_1k])
    
    # Generate new samples with adjusted covariance matrix
    new_samples = np.random.multivariate_normal(mu, target_cov, 100000)
    X_new, Y_new = new_samples.T
    
    plt.figure(figsize=(12, 5))
    
    plt.subplot(1, 2, 1)
    plt.scatter(W_1k, Z_1k, alpha=0.3, s=1)
    plt.xlabel('W')
    plt.ylabel('Z')
    plt.title('1k) Target Distribution')
    plt.grid(True, alpha=0.3)
    
    plt.subplot(1, 2, 2)
    plt.scatter(X_new, Y_new, alpha=0.3, s=1)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('2d) Adjusted Bivariate Normal')
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('images/2d_comparison_1k.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # Analyze the adjusted distribution
    analyze_samples(X_new, Y_new, mu, target_cov, "2d) Adjusted Distribution", "2d")
    
    print("2d) Original vs Adjusted Covariance Matrix:")
    print(f"Original P:\n{P}")
    print(f"Adjusted P:\n{target_cov}")
    print("-" * 50)

def main():
    np.random.seed(42)  # For reproducibility
    
    # Parameters for bivariate normal distribution
    mu = [5, 3]  # means
    P = [[4, 1.8], [1.8, 1]]  # covariance matrix
    
    # Generate samples
    n_samples = 100000
    samples = np.random.multivariate_normal(mu, P, n_samples)
    
    X, Y = samples.T
    
    question_2a(mu, P, samples)
    
    question_2b(mu, P, samples)
    
    analyze_samples(X, Y, mu, P, "2c) Original Bivariate Normal", "2c")
    
    question_2c(mu, P, samples)
    question_2d(mu, P, samples)
    
    print("All images saved in the 'images' directory")

if __name__ == "__main__":
    main()