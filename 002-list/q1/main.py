import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

os.makedirs('images', exist_ok=True)

def __rotate(X, Y, theta):
    """Rotation transformation"""
    W = 2 * np.cos(theta) * X - np.sin(theta) * Y
    Z = 2 * np.sin(theta) * X + np.cos(theta) * Y
    return W, Z

def __create_scatter_plot(X, Y, title, filename):
    """Create scatter plot only (without marginal distributions)"""
    plt.figure(figsize=(6, 5))
    
    plt.scatter(X, Y, alpha=0.5, s=1)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title(f'{title} - Scatter Plot')
    
    plt.tight_layout()
    plt.savefig(f'images/{filename}_scatter.png', dpi=300, bbox_inches='tight')
    plt.close()

def __create_correlation_matrix(X, Y, title, filename):
    """Create correlation matrix heatmap"""
    corr_matrix = np.corrcoef([X, Y])
    
    plt.figure(figsize=(6, 5))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0,
                xticklabels=['X', 'Y'], yticklabels=['X', 'Y'])
    plt.title(f'{title} - Correlation Matrix')
    plt.savefig(f'images/{filename}_correlation.png', dpi=300, bbox_inches='tight')
    plt.close()

def __create_covariance_matrix(X, Y, title, filename):
    """Create covariance matrix heatmap"""
    cov_matrix = np.cov([X, Y])
    
    plt.figure(figsize=(6, 5))
    sns.heatmap(cov_matrix, annot=True, cmap='viridis',
                xticklabels=['X', 'Y'], yticklabels=['X', 'Y'])
    plt.title(f'{title} - Covariance Matrix')
    plt.savefig(f'images/{filename}_covariance.png', dpi=300, bbox_inches='tight')
    plt.close()

def __analyze_variables(X, Y, title, filename):
    """Create all three plots for given variables"""
    __create_scatter_plot(X, Y, title, filename)
    __create_correlation_matrix(X, Y, title, filename)
    __create_covariance_matrix(X, Y, title, filename)
    
    # Print statistics
    corr = np.corrcoef(X, Y)[0, 1]
    cov = np.cov(X, Y)[0, 1]
    print(f"{title}: Corr = {corr:.4f}, Cov = {cov:.4f}")

def question_1a(X, Y):
    """Original X and Y"""
    __analyze_variables(X, Y, "1a) Original X and Y", "1a")

def question_1b(X, Y):
    """W = 2X + 5, Z = Y"""
    W = 2 * X + 5
    Z = Y
    __analyze_variables(W, Z, "1b) W = 2X + 5, Z = Y", "1b")

def question_1c(X, Y):
    """W = 2X + 5, Z = Y + 3"""
    W = 2 * X + 5
    Z = Y + 3
    __analyze_variables(W, Z, "1c) W = 2X + 5, Z = Y + 3", "1c")

def question_1d(X, Y):
    """W = 2(X + 5), Z = Y + 3"""
    W = 2 * (X + 5)
    Z = Y + 3
    __analyze_variables(W, Z, "1d) W = 2(X + 5), Z = Y + 3", "1d")

def question_1e(X, Y):
    """Rotation with theta = 0"""
    W, Z = __rotate(X, Y, 0)
    __analyze_variables(W, Z, "1e) Rotation θ = 0", "1e")

def question_1f(X, Y):
    """Rotation with theta = π/4"""
    W, Z = __rotate(X, Y, np.pi/4)
    __analyze_variables(W, Z, "1f) Rotation θ = π/4", "1f")

def question_1g(X, Y):
    """Rotation with theta = π/2"""
    W, Z = __rotate(X, Y, np.pi/2)
    __analyze_variables(W, Z, "1g) Rotation θ = π/2", "1g")

def question_1h(X, Y):
    """Rotation with theta = 3π/4"""
    W, Z = __rotate(X, Y, 3*np.pi/4)
    __analyze_variables(W, Z, "1h) Rotation θ = 3π/4", "1h")

def question_1i(X, Y):
    """Rotation with translation, θ = π/4"""
    theta = np.pi/4
    W = np.cos(theta) * (2*X + 5) - np.sin(theta) * (Y + 3)
    Z = np.sin(theta) * (2*X + 5) + np.cos(theta) * (Y + 3)
    __analyze_variables(W, Z, "1i) Rotation with Translation θ = π/4", "1i")

def question_1j(X, Y):
    """Rotation after linear transformation + translation, θ = π/4"""
    theta = np.pi/4
    W = np.cos(theta) * (2*X) - np.sin(theta) * Y + 5
    Z = np.sin(theta) * (2*X) + np.cos(theta) * Y + 3
    __analyze_variables(W, Z, "1j) Rotation after Linear Transform θ = π/4", "1j")

def question_1k(X, Y):
    """Rotation after linear transformation + translation, θ = 3π/4"""
    theta = 3*np.pi/4
    W = np.cos(theta) * (2*X) - np.sin(theta) * Y + 5
    Z = np.sin(theta) * (2*X) + np.cos(theta) * Y + 3
    __analyze_variables(W, Z, "1k) Rotation after Linear Transform θ = 3π/4", "1k")

def main():
    np.random.seed(42) # for reproducibility
    
    n_samples = 5000
    X = np.random.normal(0, 1, n_samples)
    Y = np.random.normal(0, 1, n_samples)
    
    questions = [
        question_1a, question_1b, question_1c, question_1d,
        question_1e, question_1f, question_1g, question_1h,
        question_1i, question_1j, question_1k
    ]
    
    for _, question in enumerate(questions, 1):
        question(X, Y)
    
    print("All images saved in the 'images' directory")

if __name__ == "__main__":
    main()