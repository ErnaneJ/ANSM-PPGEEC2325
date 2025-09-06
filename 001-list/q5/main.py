import os
from utils.distributions import generate_normal_samples, calculate_z_variable, calculate_stats, calculate_theoretical_stats
from utils.plotting import plot_scatter, plot_histograms

def question_5():
    num_samples = 5000
    a_value = 1
    b_values = [-10, -1, -0.1, 0, 0.1, 1, 10]
    C_values = [0, 5]
    output_dir = 'outputs'
    
    os.makedirs(output_dir, exist_ok=True)
    
    print("Gerando amostras de X e Y...")
    X = generate_normal_samples(num_samples)
    Y = generate_normal_samples(num_samples)
    
    print("\n|   b   |   C   |  Cov(X,Y) (emp) | Cov(X,Y) (teo) |  Cov(X,Z) (emp) | Cov(X,Z) (teo) |   E[Z] (emp)  |  E[Z] (teo)  |  Var(Z) (emp) | Var(Z) (teo) |")
    print("|:-----:|:-----:|:---------------:|:--------------:|:---------------:|:--------------:|:-------------:|:------------:|:-------------:|:------------:|")
    
    results = []
    
    for b in b_values:
        for C in C_values:
            Z = calculate_z_variable(X, Y, a_value, b, C)
            
            stats_empirical = calculate_stats(X, Y, Z)
            
            stats_theoretical = calculate_theoretical_stats(a_value, b, C)
            
            scatter_path = os.path.join(output_dir, f'scatter_b_{b}_C_{C}.png')
            plot_scatter(X, Z, a_value, b, C, scatter_path)
            
            hist_path = os.path.join(output_dir, f'histograms_b_{b}_C_{C}.png')
            plot_histograms(X, Y, Z, a_value, b, C, hist_path)
            
            cov_xy_emp = f"{stats_empirical['cov_xy']:.4f}"
            cov_xy_teo = f"{stats_theoretical['cov_xy_theo']:.4f}"
            cov_xz_emp = f"{stats_empirical['cov_xz']:.4f}"
            cov_xz_teo = f"{stats_theoretical['cov_xz_theo']:.4f}"
            mean_z_emp = f"{stats_empirical['mean_z']:.4f}"
            mean_z_teo = f"{stats_theoretical['mean_z_theo']:.4f}"
            var_z_emp = f"{stats_empirical['var_z']:.4f}"
            var_z_teo = f"{stats_theoretical['var_z_theo']:.4f}"
            
            print(f"| {b:5.1f} | {C:3} | {cov_xy_emp:15} | {cov_xy_teo:14} | {cov_xz_emp:15} | {cov_xz_teo:14} | {mean_z_emp:13} | {mean_z_teo:12} | {var_z_emp:13} | {var_z_teo:12} |")
            
            result = {
                'a': a_value,
                'b': b,
                'C': C,
                'cov_xy_emp': stats_empirical['cov_xy'],
                'cov_xy_teo': stats_theoretical['cov_xy_theo'],
                'cov_xz_emp': stats_empirical['cov_xz'],
                'cov_xz_teo': stats_theoretical['cov_xz_theo'],
                'mean_z_emp': stats_empirical['mean_z'],
                'mean_z_teo': stats_theoretical['mean_z_theo'],
                'var_z_emp': stats_empirical['var_z'],
                'var_z_teo': stats_theoretical['var_z_theo']
            }
            results.append(result)
    
    return results

if __name__ == "__main__":
    question_5()