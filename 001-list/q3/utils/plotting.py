import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def plot_exponential_comparison(uniform_samples, exponential_samples, lambda_param, save_path=None):
    """
    Plota comparação entre distribuição uniforme, exponencial gerada e PDF teórica
    
    Args:
        uniform_samples (np.array): Amostras da distribuição uniforme
        exponential_samples (np.array): Amostras da distribuição exponencial
        lambda_param (float): Parâmetro lambda da distribuição exponencial
        save_path (str): Caminho para salvar a figura
    """
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))
    
    # Histograma da distribuição uniforme
    sns.histplot(uniform_samples, ax=ax1, stat='density')
    ax1.set_title('Distribuição Uniforme (U)')
    ax1.set_xlabel('U')
    ax1.set_ylabel('Densidade')
    
    # Histograma da distribuição exponencial gerada
    sns.histplot(exponential_samples, ax=ax2, stat='density', label='Empírico')
    
    # PDF teórica
    x_vals = np.linspace(0, np.max(exponential_samples), 1000)
    pdf_vals = lambda_param * np.exp(-lambda_param * x_vals)
    ax2.plot(x_vals, pdf_vals, 'r-', label='Teórico')
    ax2.set_title(f'Distribuição Exponencial (λ={lambda_param})')
    ax2.set_xlabel('X')
    ax2.set_ylabel('Densidade')
    ax2.legend()
    
    # Gráfico de dispersão U vs X
    ax3.scatter(uniform_samples, exponential_samples, alpha=0.5)
    ax3.set_title('Transformação: U → X = -ln(U)/λ')
    ax3.set_xlabel('U (Uniforme)')
    ax3.set_ylabel('X (Exponencial)')
    ax3.grid(True)
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    plt.close()

def plot_qq_plot(exponential_samples, lambda_param, save_path=None):
    """
    Plota Q-Q plot para verificar a qualidade do ajuste
    
    Args:
        exponential_samples (np.array): Amostras da distribuição exponencial
        lambda_param (float): Parâmetro lambda da distribuição exponencial
        save_path (str): Caminho para salvar a figura
    """
    from scipy import stats
    
    # Gerar quantis teóricos
    theoretical_quantiles = stats.expon.ppf(np.linspace(0.01, 0.99, len(exponential_samples)), 
                                           scale=1/lambda_param)
    
    # Ordenar amostras
    sample_quantiles = np.sort(exponential_samples)
    
    _, ax = plt.subplots(figsize=(8, 6))
    ax.scatter(theoretical_quantiles, sample_quantiles, alpha=0.5)
    
    # Linha de referência y=x
    min_val = min(theoretical_quantiles.min(), sample_quantiles.min())
    max_val = max(theoretical_quantiles.max(), sample_quantiles.max())
    ax.plot([min_val, max_val], [min_val, max_val], 'r--', label='y=x')
    
    ax.set_title(f'Q-Q Plot para Distribuição Exponencial (λ={lambda_param})')
    ax.set_xlabel('Quantis Teóricos')
    ax.set_ylabel('Quantis Amostrais')
    ax.legend()
    ax.grid(True)
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    plt.close()