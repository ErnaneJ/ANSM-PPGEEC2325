import numpy as np

def generate_uniform_sums(n, num_samples=10000):
    """
    Gera a soma de n variáveis aleatórias uniformes [0, 1]
    
    Args:
        n (int): Número de variáveis uniformes a serem somadas
        num_samples (int): Número de amostras a serem geradas
        
    Returns:
        np.array: Array com as somas das n variáveis uniformes
    """
    uniform_samples = np.random.uniform(0, 1, (n, num_samples))
    sums = np.sum(uniform_samples, axis=0)
    
    return sums

def calculate_statistics(samples):
    """
    Calcula estatísticas descritivas para um conjunto de amostras
    
    Args:
        samples (np.array): Array de amostras
        
    Returns:
        dict: Dicionário com média, variância e segundo momento
    """
    mean = np.mean(samples)
    variance = np.var(samples)
    second_moment = np.mean(samples**2)
    
    return {
        'mean': mean,
        'variance': variance,
        'second_moment': second_moment
    }