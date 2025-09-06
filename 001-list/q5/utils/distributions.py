import numpy as np

def generate_normal_samples(num_samples=5000, mean=0, std=1):
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

def calculate_z_variable(X, Y, a, b, C):
    """
    Calcula Z = a*X + b*Y + C
    
    Args:
        X (np.array): Amostras da variável X
        Y (np.array): Amostras da variável Y
        a (float): Coeficiente de X
        b (float): Coeficiente de Y
        C (float): Termo constante
        
    Returns:
        np.array: Valores de Z
    """
    return a * X + b * Y + C

def calculate_stats(X, Y, Z):
    """
    Calcula estatísticas para X, Y e Z
    
    Args:
        X (np.array): Amostras da variável X
        Y (np.array): Amostras da variável Y
        Z (np.array): Amostras da variável Z
        
    Returns:
        dict: Dicionário com as estatísticas calculadas
    """
    cov_xy = np.cov(X, Y)[0, 1]
    cov_xz = np.cov(X, Z)[0, 1]
    
    mean_z = np.mean(Z)
    
    var_z = np.var(Z)
    
    return {
        'cov_xy': cov_xy,
        'cov_xz': cov_xz,
        'mean_z': mean_z,
        'var_z': var_z
    }

def calculate_theoretical_stats(a, b, C):
    """
    Calcula os valores teóricos das estatísticas para Z = aX + bY + C
    
    Args:
        a (float): Coeficiente de X
        b (float): Coeficiente de Y
        C (float): Termo constante
        
    Returns:
        dict: Dicionário com valores teóricos das estatísticas
    """
    # Como X e Y são independentes, Cov(X,Y) = 0
    cov_xy_theo = 0
    
    # Cov(X, Z) = Cov(X, aX + bY + C) = a*Var(X) + b*Cov(X,Y) = a
    cov_xz_theo = a
    
    # E[Z] = a*E[X] + b*E[Y] + C = C
    mean_z_theo = C
    
    # Var(Z) = a²*Var(X) + b²*Var(Y) + 2ab*Cov(X,Y) = a² + b²
    var_z_theo = a**2 + b**2
    
    return {
        'cov_xy_theo': cov_xy_theo,
        'cov_xz_theo': cov_xz_theo,
        'mean_z_theo': mean_z_theo,
        'var_z_theo': var_z_theo
    }