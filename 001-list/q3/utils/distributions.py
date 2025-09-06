import numpy as np

def generate_uniform_samples(num_samples=1000):
    """
    Gera amostras de uma distribuição uniforme entre 0 e 1
    
    Args:
        num_samples (int): Número de amostras a serem geradas
        
    Returns:
        np.array: Array com as amostras uniformes
    """
    return np.random.uniform(0, 1, num_samples)

def exponential_inverse_transform(uniform_samples, lambda_param):
    """
    Aplica a transformação inversa para gerar distribuição exponencial
    
    Args:
        uniform_samples (np.array): Amostras da distribuição uniforme
        lambda_param (float): Parâmetro lambda da distribuição exponencial
        
    Returns:
        np.array: Amostras da distribuição exponencial
    """
    # Fórmula: X = -ln(1 - U) / λ
    # Como U e 1-U têm a mesma distribuição, podemos usar X = -ln(U) / λ
    return -np.log(uniform_samples) / lambda_param