import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def plot_scatter(X, Z, a, b, C, save_path=None):
    """
    Plota gráfico de dispersão entre X e Z
    
    Args:
        X (np.array): Amostras da variável X
        Z (np.array): Amostras da variável Z
        a (float): Coeficiente a
        b (float): Coeficiente b
        C (float): Constante C
        save_path (str): Caminho para salvar a figura
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    
    ax.scatter(X, Z, alpha=0.5, s=10)
    ax.set_title(f'Dispersão X vs Z para a={a}, b={b}, C={C}')
    ax.set_xlabel('X')
    ax.set_ylabel('Z')
    ax.grid(True)
    
    # Adicionar linha de regressão
    z = np.polyfit(X, Z, 1)
    p = np.poly1d(z)
    ax.plot(X, p(X), "r--", alpha=0.8)
    
    # Adicionar equação da linha de regressão
    equation = f'Z = {z[0]:.2f}X + {z[1]:.2f}'
    ax.text(0.05, 0.95, equation, transform=ax.transAxes, fontsize=12,
            verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    plt.close()

def plot_histograms(X, Y, Z, a, b, C, save_path=None):
    """
    Plota histogramas de X, Y e Z
    
    Args:
        X (np.array): Amostras da variável X
        Y (np.array): Amostras da variável Y
        Z (np.array): Amostras da variável Z
        a (float): Coeficiente a
        b (float): Coeficiente b
        C (float): Constante C
        save_path (str): Caminho para salvar a figura
    """
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))
    
    # Histograma de X
    sns.histplot(X, ax=ax1, stat='density', kde=True)
    ax1.set_title('Distribuição de X')
    ax1.set_xlabel('X')
    ax1.set_ylabel('Densidade')
    
    # Histograma de Y
    sns.histplot(Y, ax=ax2, stat='density', kde=True)
    ax2.set_title('Distribuição de Y')
    ax2.set_xlabel('Y')
    ax2.set_ylabel('Densidade')
    
    # Histograma de Z
    sns.histplot(Z, ax=ax3, stat='density', kde=True)
    ax3.set_title(f'Distribuição de Z (a={a}, b={b}, C={C})')
    ax3.set_xlabel('Z')
    ax3.set_ylabel('Densidade')
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    plt.close()