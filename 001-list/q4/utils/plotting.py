import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def plot_histograms(samples, sample_sizes, save_path=None):
    """
    Plota histogramas para diferentes tamanhos de amostra
    
    Args:
        samples (np.array): Amostras da distribuição normal
        sample_sizes (list): Lista de tamanhos de amostra para plotar
        save_path (str): Caminho para salvar a figura
    """
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    axes = axes.ravel()
    
    for i, n in enumerate(sample_sizes):
        if n > len(samples):
            continue
            
        subset = samples[:n]
        sns.histplot(subset, ax=axes[i], stat='density', kde=True)
        axes[i].set_title(f'Histograma para n = {n}')
        axes[i].set_xlabel('X')
        axes[i].set_ylabel('Densidade')
        
        # Adicionar linhas para média teórica (0) e desvios padrão
        axes[i].axvline(0, color='red', linestyle='--', label='Média teórica (0)')
        axes[i].axvline(1, color='green', linestyle=':', label='+1σ teórico')
        axes[i].axvline(-1, color='green', linestyle=':', label='-1σ teórico')
        axes[i].legend()
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    plt.close()

def plot_convergence(running_means, running_variances, save_path=None):
    """
    Plota a convergência da média e variância em função do tamanho da amostra
    
    Args:
        running_means (np.array): Médias acumuladas
        running_variances (np.array): Variâncias acumuladas
        save_path (str): Caminho para salvar a figura
    """
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
    
    # Plot convergência da média
    ax1.plot(running_means, 'b-', alpha=0.7, label='Média acumulada')
    ax1.axhline(0, color='r', linestyle='--', label='Média teórica (0)')
    ax1.set_xlabel('Tamanho da amostra')
    ax1.set_ylabel('Média')
    ax1.set_title('Convergência da Média')
    ax1.legend()
    ax1.grid(True)
    
    # Adicionar pontos de interesse
    points_of_interest = [10, 100, 1000, 10000]
    for point in points_of_interest:
        if point < len(running_means):
            ax1.plot(point, running_means[point-1], 'ro')
            ax1.annotate(f'n={point}', (point, running_means[point-1]), 
                        xytext=(10, 10), textcoords='offset points')
    
    # Plot convergência da variância
    ax2.plot(running_variances, 'g-', alpha=0.7, label='Variância acumulada')
    ax2.axhline(1, color='r', linestyle='--', label='Variância teórica (1)')
    ax2.set_xlabel('Tamanho da amostra')
    ax2.set_ylabel('Variância')
    ax2.set_title('Convergência da Variância')
    ax2.legend()
    ax2.grid(True)
    
    # Adicionar pontos de interesse
    for point in points_of_interest:
        if point < len(running_variances):
            ax2.plot(point, running_variances[point-1], 'ro')
            ax2.annotate(f'n={point}', (point, running_variances[point-1]), 
                        xytext=(10, 10), textcoords='offset points')
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    plt.close()

def plot_zoom_convergence(running_means, running_variances, save_path=None):
    """
    Plota um zoom da convergência para os primeiros 1000 pontos
    
    Args:
        running_means (np.array): Médias acumuladas
        running_variances (np.array): Variâncias acumuladas
        save_path (str): Caminho para salvar a figura
    """
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
    
    # Zoom da convergência da média (primeiros 1000 pontos)
    ax1.plot(running_means[:1000], 'b-', alpha=0.7, label='Média acumulada')
    ax1.axhline(0, color='r', linestyle='--', label='Média teórica (0)')
    ax1.set_xlabel('Tamanho da amostra')
    ax1.set_ylabel('Média')
    ax1.set_title('Convergência da Média (Primeiros 1000 pontos)')
    ax1.legend()
    ax1.grid(True)
    
    # Zoom da convergência da variância (primeiros 1000 pontos)
    ax2.plot(running_variances[:1000], 'g-', alpha=0.7, label='Variância acumulada')
    ax2.axhline(1, color='r', linestyle='--', label='Variância teórica (1)')
    ax2.set_xlabel('Tamanho da amostra')
    ax2.set_ylabel('Variância')
    ax2.set_title('Convergência da Variância (Primeiros 1000 pontos)')
    ax2.legend()
    ax2.grid(True)
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    plt.close()