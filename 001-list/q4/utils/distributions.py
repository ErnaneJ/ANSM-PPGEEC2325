import numpy as np

def generate_normal_samples(num_samples=10000, mean=0, std=1):
    """
    Gera amostras de uma distribuição normal
    
    Args:
        num_samples (int): Número de amostras a serem geradas
        mean (float): Média da distribuição normal
        std (float): Desvio padrão da distribuição normal
        
    Returns:
        np.array: Array com as amostras normais
    """
    return np.random.normal(mean, std, num_samples)

def calculate_running_stats(samples):
    """
    Calcula estatísticas acumuladas (média e variância) à medida que a amostra aumenta
    
    Args:
        samples (np.array): Amostras da distribuição normal
        
    Returns:
        tuple: (running_means, running_variances)
    """
    running_means = np.cumsum(samples) / np.arange(1, len(samples) + 1)
    running_variances = [np.var(samples[:i]) for i in range(1, len(samples) + 1)]
    
    return running_means, running_variances