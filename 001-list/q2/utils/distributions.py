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

def transform_samples(X, a, b):
    """
    Aplica a transformação Y = a*X² + b
    
    Args:
        X (np.array): Amostras da variável original
        a (float): Coeficiente quadrático
        b (float): Termo constante
        
    Returns:
        np.array: Amostras transformadas
    """
    return a * X**2 + b

def calculate_stats(X, Y):
    """
    Calcula estatísticas descritivas para X e Y
    
    Args:
        X (np.array): Amostras da variável X
        Y (np.array): Amostras da variável Y
        
    Returns:
        dict: Dicionário com as estatísticas calculadas
    """
    E_X = np.mean(X)
    E_X2 = np.mean(X**2)
    Var_X = np.var(X)
    std_X = np.std(X)
    
    E_Y = np.mean(Y)
    E_Y2 = np.mean(Y**2)
    Var_Y = np.var(Y)
    std_Y = np.std(Y)
    
    Cov_XY = np.cov(X, Y)[0, 1]
    Corr_XY = np.corrcoef(X, Y)[0, 1]
    
    return {
        'E_X': E_X,
        'E_Y': E_Y,
        'E_X2': E_X2,
        'E_Y2': E_Y2,
        'Var_X': Var_X,
        'Var_Y': Var_Y,
        'std_X': std_X,
        'std_Y': std_Y,
        'Cov_XY': Cov_XY,
        'Corr_XY': Corr_XY
    }

def calculate_theoretical_stats(a, b):
    """
    Calcula os valores teóricos das estatísticas para Y = aX² + b
    
    Args:
        a (float): Coeficiente quadrático
        b (float): Termo constante
        
    Returns:
        dict: Dicionário com valores teóricos das estatísticas
    """
    E_X = 0.5
    E_X2 = 1/3
    E_X4 = 1/5
    Var_X = 1/12
    std_X = np.sqrt(Var_X)
    
    E_Y = a * E_X2 + b
    E_Y2 = a**2 * E_X4 + 2*a*b*E_X2 + b**2
    Var_Y = E_Y2 - E_Y**2
    std_Y = np.sqrt(Var_Y)
    
    E_X3 = 1/4
    E_XY = a * E_X3 + b * E_X
    Cov_XY = E_XY - E_X * E_Y
    
    if Var_X > 0 and Var_Y > 0:
        Corr_XY = Cov_XY / (std_X * std_Y)
    else:
        Corr_XY = np.nan
    
    return {
        'E_X': E_X,
        'E_Y': E_Y,
        'E_X2': E_X2,
        'E_Y2': E_Y2,
        'Var_X': Var_X,
        'Var_Y': Var_Y,
        'std_X': std_X,
        'std_Y': std_Y,
        'Cov_XY': Cov_XY,
        'Corr_XY': Corr_XY
    }