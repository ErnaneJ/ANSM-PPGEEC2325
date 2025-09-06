import os
import numpy as np
from utils.distributions import generate_uniform_sums, calculate_statistics
from utils.plotting import plot_distributions, plot_convergence

def question_1():
    n_values = range(1, 13)
    num_samples = 10000
    output_dir = 'outputs'
    
    os.makedirs(output_dir, exist_ok=True)
    
    results = {}
    
    print("|  n   |    E[X]   |   Var[X]  |   E[X²]   |")
    print("|:----:|:---------:|:---------:|:---------:|")
    for n in n_values:
        samples = generate_uniform_sums(n, num_samples)
        
        stats = calculate_statistics(samples)
        results[n] = stats
        
        plot_path = os.path.join(output_dir, f'distributions_n_{n}.png')
        plot_distributions(samples, n, plot_path)
        
        print(f"|  {n:02}   |   {stats['mean']:.4f}  |   {stats['variance']:.4f}  |  {stats['second_moment']:.4f}   |")

    convergence_path = os.path.join(output_dir, 'convergence.png')
    plot_convergence(results, convergence_path)
    
    return results

if __name__ == "__main__":
    question_1()