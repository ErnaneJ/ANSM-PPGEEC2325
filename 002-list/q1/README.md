# Questão 1 - Análise de Transformações em Variáveis Aleatórias Normais

## Objetivo

Analisar o efeito de diferentes transformações lineares e rotações em pares de variáveis aleatórias normais independentes X e Y (com média zero e variância 1) sobre suas propriedades estatísticas, especificamente correlação e covariância.

## Fundamentação Teórica

Dadas duas variáveis aleatórias normais independentes:
$$
  X \approx N(0, 1) \newline
  Y \approx N(0, 1)
$$

Temos que:
$$
  E[X] = E[Y] = 0 \newline
  Var[X] = Var[Y] = 1 \newline
  Cov(X,Y) = 0 \text{ (devido à independência)} \newline
  Corr(X,Y) = 0 \text{ (devido à independência)} \newline
$$

Para transformações lineares da forma $W = aX + b$ e $Z = cY + d$:

$$
  E[W] = a \cdot E[X] + b = b \newline
  E[Z] = c \cdot E[Y] + d = d \newline
  Cov(W,Z) = a \cdot c \cdot Cov(X, Y) = 0 \newline
  Corr(W,Z) = 0
$$

Para rotações com ângulo θ:
$$
  W = 2 \cdot cos(θ) \cdot X - sin(θ) \cdot Y \newline
  Z = 2 \cdot sin(θ) \cdot X + cos(θ) \cdot Y
$$

## Metodologia

1. **Geração de dados**: 5.000 amostras de $X \approx Y \approx N(0, 1)$
2. **Aplicação de transformações**: 11 diferentes transformações (1.a a 1.k)
3. **Análise estatística**: Para cada par $(W,Z)$ resultante, calculou-se:
   - Coeficiente de correlação ($Corr$)
   - Covariância ($Cov$)
4. **Visualização**: Para cada caso, gerou-se três tipos de gráficos:
   - Gráfico de dispersão com distribuições marginais
   - Matriz de correlação
   - Matriz de covariância

## Como Executar

```bash
# em /002-list/q1

python -m venv .venv  
source .venv/bin/activate

pip install -r requirements.txt  

python main.py
```

## Resultados e Análise

### Estatísticas Obtidas

| Questão | Transformação | Correlação | Covariância |
|---------|---------------|------------|-------------|
| 1.a | Original X e Y | -0.0018 | -0.0018 |
| 1.b | W = 2X + 5, Z = Y | -0.0018 | -0.0036 |
| 1.c | W = 2X + 5, Z = Y + 3 | -0.0018 | -0.0036 |
| 1.d | W = 2(X + 5), Z = Y + 3 | -0.0018 | -0.0036 |
| 1.e | Rotação θ = 0 | -0.0018 | -0.0036 |
| 1.f | Rotação θ = π/4 | 0.5910 | 1.4755 |
| 1.g | Rotação θ = π/2 | 0.0018 | 0.0036 |
| 1.h | Rotação θ = 3π/4 | -0.5910 | -1.4755 |
| 1.i | Rotação com translação θ = π/4 | 0.5910 | 1.4755 |
| 1.j | Rotação após transformação linear + translação θ = π/4 | 0.5910 | 1.4755 |
| 1.k | Rotação após transformação linear + translação θ = 3π/4 | -0.5910 | -1.4755 |

### Análise dos Resultados

#### Casos 1.a-1.e: Independência Preservada

Correlação próxima de zero em todos os casos pois transformações lineares que não misturam $X$ e $Y$ preservam a independência.

|   |**1.a-1.e: Independência Preservada**|   |
|:-:|:----------------------------------------:|:-:|
|![1a Scatter](images/1a_scatter.png)|![1a Correlation](images/1a_correlation.png)|![1a Covariance](images/1a_covariance.png)|
|![1b Scatter](images/1b_scatter.png)|![1b Correlation](images/1b_correlation.png)|![1b Covariance](images/1b_covariance.png)|
|![1c Scatter](images/1c_scatter.png)|![1c Correlation](images/1c_correlation.png)|![1c Covariance](images/1c_covariance.png)|
|![1d Scatter](images/1d_scatter.png)|![1d Correlation](images/1d_correlation.png)|![1d Covariance](images/1d_covariance.png)|
|![1e Scatter](images/1e_scatter.png)|![1e Correlation](images/1e_correlation.png)|![1e Covariance](images/1e_covariance.png)|

#### Casos 1.f e 1.h: Introdução de Correlação

Correlação significativa ($|ρ| \approx 0.59$) para $θ = π/4$ e $θ = 3π/4$. Rotações que misturam $X$ e $Y$ criam dependência entre $W$ e $Z$. A covariância teórica é: 

$$
  Cov(W,Z) = 4·cos(θ)·sin(θ)·Var[X] - 2·cos²(θ)·Cov(X,Y) + 2·sin²(θ)·Cov(Y,X) - sin(θ)·cos(θ)·Var[Y]
$$

Simplificando com $Cov(X,Y)=0$, $Var[X]=Var[Y]=1$:
$$
  Cov(W,Z) = 4·cos(θ)·sin(θ) - sin(θ)·cos(θ) = 3·cos(θ)·sin(θ)
$$

|   |**1.f e 1.h: Introdução de Correlação**|   |
|:-:|:----------------------------------------:|:-:|
|![1f Scatter](images/1f_scatter.png)|![1f Correlation](images/1f_correlation.png)|![1f Covariance](images/1f_covariance.png)|
|![1g Scatter](images/1g_scatter.png)|![1g Correlation](images/1g_correlation.png)|![1g Covariance](images/1g_covariance.png)|
|![1h Scatter](images/1h_scatter.png)|![1h Correlation](images/1h_correlation.png)|![1h Covariance](images/1h_covariance.png)|

#### Casos 1.i-1.k: Invariância a Translações

Translações não afetam correlação/covariância pois $Cov(W+b, Z+d) = Cov(W,Z)$. Assim, as constantes aditivas não influenciam as medidas de dependência linear.

|   |**1.i-1.k: Invariância a Translações**|   |
|:-:|:----------------------------------------:|:-:|
|![1i Scatter](images/1i_scatter.png)|![1i Correlation](images/1i_correlation.png)|![1i Covariance](images/1i_covariance.png)|
|![1j Scatter](images/1j_scatter.png)|![1j Correlation](images/1j_correlation.png)|![1j Covariance](images/1j_covariance.png)|
|![1k Scatter](images/1k_scatter.png)|![1k Correlation](images/1k_correlation.png)|![1k Covariance](images/1k_covariance.png)|

## Conclusões

1. **Transformações lineares simples** (1.a-1.e) que não misturam X e Y preservam a independência, resultando em correlação/covariância próximas de zero.
2. **Rotações** (1.f, 1.g, 1.h) que misturam X e Y podem introduzir correlação entre as variáveis transformadas, dependendo do ângulo de rotação.
3. **Translações** (adição de constantes) não afetam correlação ou covariância, confirmando a propriedade de invariância dessas medidas a deslocamentos.

As imagens completas para todos os casos estão disponíveis na pasta `images/`.
