import os
import numpy as np
from utils.distributions import generate_uniform_samples, exponential_inverse_transform, exponential_pdf
from utils.plotting import plot_exponential_comparison, plot_qq_plot

def question_3():
    lambda_params = [0.5, 1, 2, 5]  # Diferentes valores de λ para testar
    num_samples = 10000
    output_dir = 'outputs'
    
    os.makedirs(output_dir, exist_ok=True)
    
    print("|   λ   |   E[X] (emp)  |  E[X] (teo)  |  Var(X) (emp) | Var(X) (teo) |")
    print("|:-----:|:-------------:|:------------:|:-------------:|:------------:|")
    
    for lambda_param in lambda_params:
        uniform_samples = generate_uniform_samples(num_samples)
        
        exponential_samples = exponential_inverse_transform(uniform_samples, lambda_param)
        
        # estatísticas empíricas
        mean_emp = np.mean(exponential_samples)
        var_emp = np.var(exponential_samples)
        
        # estatísticas teóricas
        mean_teo = 1 / lambda_param
        var_teo = 1 / (lambda_param ** 2)
        
        comparison_path = os.path.join(output_dir, f'exponential_comparison_lambda_{lambda_param}.png')
        plot_exponential_comparison(uniform_samples, exponential_samples, lambda_param, comparison_path)
        
        qq_path = os.path.join(output_dir, f'qq_plot_lambda_{lambda_param}.png')
        plot_qq_plot(exponential_samples, lambda_param, qq_path)
        
        print(f"|  {lambda_param}  |  {mean_emp:.4f}  |  {mean_teo:.4f}  |  {var_emp:.4f}  |  {var_teo:.4f}  |")
    
if __name__ == "__main__":
    question_3()