import matplotlib.pyplot as plt
import seaborn as sns

def plot_distributions(samples, n, save_path=None):
    """
    Plota PDF e CDF para um conjunto de amostras
    
    Args:
        samples (np.array): Array de amostras
        n (int): Valor de n (para título do gráfico)
        save_path (str): Caminho para salvar a figura
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # Plot PDF (histograma)
    sns.histplot(samples, ax=ax1, stat='density', kde=True)
    ax1.set_title(f'PDF para n = {n}')
    ax1.set_xlabel('X')
    ax1.set_ylabel('Densidade')
    
    # Plot CDF
    sns.ecdfplot(samples, ax=ax2)
    ax2.set_title(f'CDF para n = {n}')
    ax2.set_xlabel('X')
    ax2.set_ylabel('Probabilidade Acumulada')
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    plt.close()

def plot_convergence(results, save_path=None):
    """
    Plota a convergência da média e variância em função de n
    
    Args:
        results (dict): Dicionário com resultados para cada n
        save_path (str): Caminho para salvar a figura
    """
    n_values = list(results.keys())
    means = [results[n]['mean'] for n in n_values]
    variances = [results[n]['variance'] for n in n_values]
    
    # Valores teóricos
    theoretical_means = [n * 0.5 for n in n_values]
    theoretical_variances = [n * (1/12) for n in n_values]
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # Plot média
    ax1.plot(n_values, means, 'bo-', label='Simulado')
    ax1.plot(n_values, theoretical_means, 'r--', label='Teórico')
    ax1.set_xlabel('n')
    ax1.set_ylabel('E[X]')
    ax1.set_title('Convergência da Média')
    ax1.legend()
    ax1.grid(True)
    
    # Plot variância
    ax2.plot(n_values, variances, 'bo-', label='Simulado')
    ax2.plot(n_values, theoretical_variances, 'r--', label='Teórico')
    ax2.set_xlabel('n')
    ax2.set_ylabel('Var[X]')
    ax2.set_title('Convergência da Variância')
    ax2.legend()
    ax2.grid(True)
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    plt.close()