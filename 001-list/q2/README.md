# Questão 2 - Análise da Transformação $Y = aX² + b$

## Objetivo

Analisar o comportamento da transformação $Y = aX² + b$, onde $X$ é uma variável aleatória uniforme entre $0$ e $1$.

## Metodologia

1. Geração de $1.000$ amostras de $X ~ Uniform(0,1)$
2. Aplicação da transformação para diferentes valores de $a$ e $b$
3. Cálculo de estatísticas descritivas (empíricas e teóricas)
4. Visualização das distribuições e relação entre $X$ e $Y$

### Combinações testadas

- $a = [0, 0.5, 1, 2]$
- $b = [-1, 0, 1, 2, 4]$

### Estatísticas calculadas

- $E[X]$, $E[Y]$, $E[X²]$, $E[Y²]$
- $Var(X)$, $Var(Y)$, $σ(X)$, $σ(Y)$
- $Cov(X,Y)$, $Corr(X,Y)$

## Como Executar

```bash
# em /001-list/q2

python -m venv .venv  
source .venv/bin/activate

pip install -r requirements.txt  

python main.py
```

## Resultado

Para $a=0$, $Y$ é constante, então variância zero e correlação indefinida Para $a>0$, os valores empíricos estão próximos dos teóricos, confirmando a precisão da simulação. A correlação entre $X$ e $Y$ é sempre positiva quando $a>0$, com valores em torno de $0.97$. O valor de $b$ não afeta a correlação entre $X$ e $Y$, apenas desloca a distribuição de $Y$.

|   a   |   b   |   E[Y] (emp)  |  E[Y] (teo)  |  Var(Y) (emp) | Var(Y) (teo) | Corr(X,Y) (emp) | Corr(X,Y) (teo) |
|:-----:|:-----:|:-------------:|:------------:|:-------------:|:------------:|:---------------:|:---------------:|
|  0  |  -1  |  -1.0000  |  -1.0000  |  0.0000  |  0.0000  |  -  |  -  |
|  0  |  0  |  0.0000  |  0.0000  |  0.0000  |  0.0000  |  -  |  -  |
|  0  |  1  |  1.0000  |  1.0000  |  0.0000  |  0.0000  |  -  |  -  |
|  0  |  2  |  2.0000  |  2.0000  |  0.0000  |  0.0000  |  -  |  -  |
|  0  |  4  |  4.0000  |  4.0000  |  0.0000  |  0.0000  |  -  |  -  |
|  0.5  |  -1  |  -0.8277  |  -0.8333  |  0.0228  |  0.0222  |  0.9702  |  0.9682  |
|  0.5  |  0  |  0.1679  |  0.1667  |  0.0221  |  0.0222  |  0.9687  |  0.9682  |
|  0.5  |  1  |  1.1659  |  1.1667  |  0.0219  |  0.0222  |  0.9682  |  0.9682  |
|  0.5  |  2  |  2.1624  |  2.1667  |  0.0219  |  0.0222  |  0.9686  |  0.9682  |
|  0.5  |  4  |  4.1600  |  4.1667  |  0.0214  |  0.0222  |  0.9683  |  0.9682  |
|  1  |  -1  |  -0.6806  |  -0.6667  |  0.0900  |  0.0889  |  0.9688  |  0.9682  |
|  1  |  0  |  0.3183  |  0.3333  |  0.0886  |  0.0889  |  0.9688  |  0.9682  |
|  1  |  1  |  1.3443  |  1.3333  |  0.0913  |  0.0889  |  0.9687  |  0.9682  |
|  1  |  2  |  2.3331  |  2.3333  |  0.0880  |  0.0889  |  0.9683  |  0.9682  |
|  1  |  4  |  4.3393  |  4.3333  |  0.0950  |  0.0889  |  0.9685  |  0.9682  |
|  2  |  -1  |  -0.3563  |  -0.3333  |  0.3378  |  0.3556  |  0.9675  |  0.9682  |
|  2  |  0  |  0.6726  |  0.6667  |  0.3652  |  0.3556  |  0.9686  |  0.9682  |
|  2  |  1  |  1.6167  |  1.6667  |  0.3374  |  0.3556  |  0.9669  |  0.9682  |
|  2  |  2  |  2.6407  |  2.6667  |  0.3500  |  0.3556  |  0.9675  |  0.9682  |
|  2  |  4  |  4.6721  |  4.6667  |  0.3470  |  0.3556  |  0.9682  |  0.9682  |

Os gráficos e resultados foram salvos na pasta `outputs/`.

### Histogramas

|📊|                    `a = 0`                    |                     `a = 0.5`                     |                    `a = 1`                    |                    `a = 2`                    |
|:-:| :-------------------------------------------: | :-----------------------------------------------: | :-------------------------------------------: | :-------------------------------------------: |
|`b = -1`| ![h_0_-1](./outputs/histogram_a_0_b_-1.png) | ![h_0.5_-1](./outputs/histogram_a_0.5_b_-1.png) | ![h_1_-1](./outputs/histogram_a_1_b_-1.png) | ![h_2_-1](./outputs/histogram_a_2_b_-1.png) |
|`b = 0`|  ![h_0_0](./outputs/histogram_a_0_b_0.png)  |  ![h_0.5_0](./outputs/histogram_a_0.5_b_0.png)  |  ![h_1_0](./outputs/histogram_a_1_b_0.png)  |  ![h_2_0](./outputs/histogram_a_2_b_0.png)  |
|`b = 1`|  ![h_0_1](./outputs/histogram_a_0_b_1.png)  |  ![h_0.5_1](./outputs/histogram_a_0.5_b_1.png)  |  ![h_1_1](./outputs/histogram_a_1_b_1.png)  |  ![h_2_1](./outputs/histogram_a_2_b_1.png)  |
|`b = 2`|  ![h_0_2](./outputs/histogram_a_0_b_2.png)  |  ![h_0.5_2](./outputs/histogram_a_0.5_b_2.png)  |  ![h_1_2](./outputs/histogram_a_1_b_2.png)  |  ![h_2_2](./outputs/histogram_a_2_b_2.png)  |
|`b = 4`|  ![h_0_4](./outputs/histogram_a_0_b_4.png)  |  ![h_0.5_4](./outputs/histogram_a_0.5_b_4.png)  |  ![h_1_4](./outputs/histogram_a_1_b_4.png)  |  ![h_2_4](./outputs/histogram_a_2_b_4.png)  |
||||||

### Scatter Plots

|🔵|                    `a = 0`                    |                     `a = 0.5`                     |                    `a = 1`                    |                    `a = 2`                    |
|:-:| :-------------------------------------------: | :-----------------------------------------------: | :-------------------------------------------: | :-------------------------------------------: |
|`b = -1`| ![s_0_-1](./outputs/scatter_a_0_b_-1.png) | ![s_0.5_-1](./outputs/scatter_a_0.5_b_-1.png) | ![s_1_-1](./outputs/scatter_a_1_b_-1.png) | ![s_2_-1](./outputs/scatter_a_2_b_-1.png) |
|`b = 0`|  ![s_0_0](./outputs/scatter_a_0_b_0.png)  |  ![s_0.5_0](./outputs/scatter_a_0.5_b_0.png)  |  ![s_1_0](./outputs/scatter_a_1_b_0.png)  |  ![s_2_0](./outputs/scatter_a_2_b_0.png)  |
|`b = 1`|  ![s_0_1](./outputs/scatter_a_0_b_1.png)  |  ![s_0.5_1](./outputs/scatter_a_0.5_b_1.png)  |  ![s_1_1](./outputs/scatter_a_1_b_1.png)  |  ![s_2_1](./outputs/scatter_a_2_b_1.png)  |
|`b = 2`|  ![s_0_2](./outputs/scatter_a_0_b_2.png)  |  ![s_0.5_2](./outputs/scatter_a_0.5_b_2.png)  |  ![s_1_2](./outputs/scatter_a_1_b_2.png)  |  ![s_2_2](./outputs/scatter_a_2_b_2.png)  |
|`b = 4`|  ![s_0_4](./outputs/scatter_a_0_b_4.png)  |  ![s_0.5_4](./outputs/scatter_a_0.5_b_4.png)  |  ![s_1_4](./outputs/scatter_a_1_b_4.png)  |  ![s_2_4](./outputs/scatter_a_2_b_4.png)  |
||||||

Data: [results.csv](./outputs/results.csv)
