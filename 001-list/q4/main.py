import os
import numpy as np
from utils.distributions import generate_normal_samples, calculate_running_stats
from utils.plotting import plot_histograms, plot_convergence, plot_zoom_convergence

def question_4():
    """
    Resolve a Questão 4 da lista de exercícios
    """
    # Configurações
    num_samples = 10000
    sample_sizes = [10, 100, 1000, 10000]
    output_dir = 'outputs'
    
    # Criar diretório de saída se não existir
    os.makedirs(output_dir, exist_ok=True)
    
    # Gerar amostras da distribuição normal padrão
    print("Gerando amostras da distribuição normal padrão...")
    samples = generate_normal_samples(num_samples)
    
    # a) Obter histogramas para diferentes tamanhos de amostra
    print("Gerando histogramas...")
    hist_path = os.path.join(output_dir, 'histograms.png')
    plot_histograms(samples, sample_sizes, hist_path)
    
    # b) Calcular média e variância acumuladas
    print("Calculando estatísticas acumuladas...")
    running_means, running_variances = calculate_running_stats(samples)
    
    # Imprimir resultados para os tamanhos de amostra específicos
    print("\n|  n   |   Média   |  Variância  |")
    print("|:----:|:---------:|:-----------:|")
    for n in sample_sizes:
        if n <= num_samples:
            mean_val = running_means[n-1]
            var_val = running_variances[n-1]
            print(f"| {n:4} | {mean_val:8.4f} | {var_val:10.4f} |")
    
    # Plotar convergência da média e variância
    print("Plotando gráficos de convergência...")
    convergence_path = os.path.join(output_dir, 'convergence.png')
    plot_convergence(running_means, running_variances, convergence_path)
    
    # Plotar zoom da convergência (primeiros 1000 pontos)
    zoom_path = os.path.join(output_dir, 'convergence_zoom.png')
    plot_zoom_convergence(running_means, running_variances, zoom_path)
    
    # Análise dos resultados
    print("\nAnálise dos resultados:")
    print("1. Para amostras pequenas (n=10), o histograma pode não parecer muito com uma distribuição normal.")
    print("2. À medida que n aumenta, o histograma se aproxima cada vez mais da forma da distribuição normal teórica.")
    print("3. A média e variância acumuladas convergem para os valores teóricos (0 e 1) à medida que n aumenta.")
    print("4. Para n pequeno, as estatísticas podem variar bastante, mas se estabilizam com amostras maiores.")
    print("5. Este é um exemplo da Lei dos Grandes Números em ação.")

if __name__ == "__main__":
    question_4()