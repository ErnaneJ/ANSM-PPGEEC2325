import os
import numpy as np
from utils.distributions import generate_normal_samples, calculate_running_stats
from utils.plotting import plot_histograms, plot_convergence, plot_zoom_convergence

def question_4():
    num_samples = 10000
    sample_sizes = [10, 100, 1000, 10000]
    output_dir = 'outputs'
    
    os.makedirs(output_dir, exist_ok=True)
    
    samples = generate_normal_samples(num_samples)
    
    print("a) Obtendo histogramas para diferentes tamanhos de amostra")
    hist_path = os.path.join(output_dir, 'histograms.png')
    plot_histograms(samples, sample_sizes, hist_path)
    
    print("b) Calculando média e variância acumuladas...")
    running_means, running_variances = calculate_running_stats(samples)
    
    print("\n|  n   |   Média   |  Variância  |")
    print("|:----:|:---------:|:-----------:|")
    for n in sample_sizes:
        if n <= num_samples:
            mean_val = running_means[n-1]
            var_val = running_variances[n-1]
            print(f"| {n:4} | {mean_val:8.4f} | {var_val:10.4f} |")
    
    convergence_path = os.path.join(output_dir, 'convergence.png')
    plot_convergence(running_means, running_variances, convergence_path)
    
    zoom_path = os.path.join(output_dir, 'convergence_zoom.png')
    plot_zoom_convergence(running_means, running_variances, zoom_path)

if __name__ == "__main__":
    question_4()