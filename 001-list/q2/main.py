import os
import numpy as np
import warnings
from utils.distributions import generate_uniform_samples, transform_samples, calculate_stats, calculate_theoretical_stats
from utils.plotting import plot_histogram_comparison, plot_scatter

def question_2():
    a_values = [0, 0.5, 1, 2]
    b_values = [-1, 0, 1, 2, 4]
    num_samples = 1000
    output_dir = 'outputs'
    
    os.makedirs(output_dir, exist_ok=True)
    
    warnings.filterwarnings('ignore', category=RuntimeWarning, module='numpy.lib._function_base_impl')
    
    print("|   a   |   b   |   E[Y] (emp)  |  E[Y] (teo)  |  Var(Y) (emp) | Var(Y) (teo) | Corr(X,Y) (emp) | Corr(X,Y) (teo) |")
    print("|:-----:|:-----:|:-------------:|:------------:|:-------------:|:------------:|:---------------:|:---------------:|")
    
    results = []
    
    for a in a_values:
        for b in b_values:
            X = generate_uniform_samples(num_samples)
            
            Y = transform_samples(X, a, b)
            
            stats_empirical = calculate_stats(X, Y)
            
            stats_theoretical = calculate_theoretical_stats(a, b)
            
            hist_path = os.path.join(output_dir, f'histogram_a_{a}_b_{b}.png')
            plot_histogram_comparison(X, Y, a, b, hist_path)
            
            scatter_path = os.path.join(output_dir, f'scatter_a_{a}_b_{b}.png')
            plot_scatter(X, Y, a, b, scatter_path)
            
            e_y_emp = f"{stats_empirical['E_Y']:.4f}"
            e_y_teo = f"{stats_theoretical['E_Y']:.4f}"
            var_y_emp = f"{stats_empirical['Var_Y']:.4f}"
            var_y_teo = f"{stats_theoretical['Var_Y']:.4f}"
            
            if a == 0:
                corr_xy_emp = "-"
                corr_xy_teo = "-"
            else:
                corr_xy_emp = f"{stats_empirical['Corr_XY']:.4f}"
                corr_xy_teo = f"{stats_theoretical['Corr_XY']:.4f}"
            
            print(f"|  {a}  |  {b}  |  {e_y_emp}  |  {e_y_teo}  |  {var_y_emp}  |  {var_y_teo}  |  {corr_xy_emp}  |  {corr_xy_teo}  |")
            
            result = {
                'a': a,
                'b': b,
                'E_X_emp': stats_empirical['E_X'],
                'E_X_teo': stats_theoretical['E_X'],
                'E_Y_emp': stats_empirical['E_Y'],
                'E_Y_teo': stats_theoretical['E_Y'],
                'E_X2_emp': stats_empirical['E_X2'],
                'E_X2_teo': stats_theoretical['E_X2'],
                'E_Y2_emp': stats_empirical['E_Y2'],
                'E_Y2_teo': stats_theoretical['E_Y2'],
                'Var_X_emp': stats_empirical['Var_X'],
                'Var_X_teo': stats_theoretical['Var_X'],
                'Var_Y_emp': stats_empirical['Var_Y'],
                'Var_Y_teo': stats_theoretical['Var_Y'],
                'std_X_emp': stats_empirical['std_X'],
                'std_X_teo': stats_theoretical['std_X'],
                'std_Y_emp': stats_empirical['std_Y'],
                'std_Y_teo': stats_theoretical['std_Y'],
                'Cov_XY_emp': stats_empirical['Cov_XY'],
                'Cov_XY_teo': stats_theoretical['Cov_XY'],
                'Corr_XY_emp': stats_empirical['Corr_XY'],
                'Corr_XY_teo': stats_theoretical['Corr_XY']
            }
            results.append(result)
    
    warnings.filterwarnings('default')
    
    return results

if __name__ == "__main__":
    question_2()