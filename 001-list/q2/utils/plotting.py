import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def plot_histogram_comparison(X, Y, a, b, save_path=None):
    """
    Plota histograma de Y e compara com a PDF teórica (se disponível)
    
    Args:
        X (np.array): Amostras de X
        Y (np.array): Amostras de Y
        a (float): Coeficiente a
        b (float): Coeficiente b
        save_path (str): Caminho para salvar a figura
    """
    _, ax = plt.subplots(figsize=(10, 6))
    
    sns.histplot(Y, ax=ax, stat='density', label='Empírico', alpha=0.7)
    
    if a != 0:
        # Para a != 0, a transformação é não linear e a PDF teórica pode ser derivada
        # Para uniforme X ~ U(0,1), Y = aX² + b
        # A função inversa: x = sqrt((y - b)/a), então a PDF de Y é f_Y(y) = f_X(x) / |dy/dx|
        # dy/dx = 2a*x = 2a*sqrt((y-b)/a) = 2*sqrt(a*(y-b))
        # Então f_Y(y) = 1 / (2*sqrt(a*(y-b))) para y em [b, a+b]
        y_min = b
        y_max = a + b
        y_vals = np.linspace(y_min, y_max, 1000)
        # Evitar divisão por zero e valores negativos dentro da raiz
        with np.errstate(divide='ignore', invalid='ignore'):
            pdf_vals = 1 / (2 * np.sqrt(a * (y_vals - b)))
        # A PDF é indefinida fora do intervalo [b, a+b]
        ax.plot(y_vals, pdf_vals, 'r-', label='Teórico')
    else:
        # Se a=0, então Y = b, que é uma constante, então a PDF é um pico em b
        ax.axvline(b, color='red', linestyle='--', label=f'Teórico (Y={b})')
    
    ax.set_title(f'Distribuição de Y para a={a}, b={b}')
    ax.set_xlabel('Y')
    ax.set_ylabel('Densidade')
    ax.legend()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    plt.close()

def plot_scatter(X, Y, a, b, save_path=None):
    """
    Plota gráfico de dispersão entre X e Y
    
    Args:
        X (np.array): Amostras de X
        Y (np.array): Amostras de Y
        a (float): Coeficiente a
        b (float): Coeficiente b
        save_path (str): Caminho para salvar a figura
    """
    _, ax = plt.subplots(figsize=(10, 6))
    
    ax.scatter(X, Y, alpha=0.5)
    ax.set_title(f'Dispersão X vs Y para a={a}, b={b}')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.grid(True)
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    plt.close()