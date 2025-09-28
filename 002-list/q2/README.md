# Questão 2 - Análise de Distribuição Normal Bivariada

## Objetivo

Analisar uma distribuição normal bivariada com parâmetros específicos e comparar com os resultados obtidos na Questão 1.

## Parâmetros da Distribuição

- **Médias**: $μx = 5$, $μy = 3$
- **Matriz de covariância**: $P = [[4, 1.8], [1.8, 1]]$
- **Número de amostras**: $100000$

## Metodologia

1. **Geração de dados**: $100000$ amostras da distribuição normal bivariada
2. **Visualização**:
   - Gráfico 3D da função densidade de probabilidade (PDF)
   - Curvas de nível da PDF
   - Gráficos de dispersão das amostras
3. **Análise comparativa**:
   - Comparação com a transformação da Questão `1.j`
   - Ajuste da matriz de covariância para similaridade com Questão `1.k`

## Como Executar

```bash
# em /002-list/q2

python -m venv .venv  
source .venv/bin/activate

pip install -r requirements.txt  

python main.py
```

## Resultados e Análise

### 2.a) Gráfico 3D da PDF

![3D Plot](images_q2/2a_3d.png)

O gráfico 3D mostra a forma característica do "chapéu mexicano" da distribuição normal bivariada, centrado em ($5$, $3$).

### 2.b) Superfícies de Nível

![Contour Plot](images_q2/2b_contour.png)

As curvas de nível mostram elipses concêntricas, representando regiões de probabilidade constante. A orientação das elipses indica a correlação positiva entre $X$ e $Y$.

### 2.c) Comparação com Questão 1.j

![Comparison 1j](images_q2/2c_comparison_1j.png)

**Estatísticas comparativas:**
$$
  Corr = 0.5910, Cov = 1.4755 \text{ (Questão 1.j)} \newline
  Corr = 0.8998, Cov = 1.7982 \text{ (Questão 2)}
$$

A distribuição da Questão 2 mostra maior correlação que a transformação da Questão `1.j`, indicando que as transformações lineares com rotação produzem diferentes estruturas de dependência.

### 2.d) Ajuste para Similaridade com Questão 1.k

![Comparison 1k](images_q2/2d_comparison_1k.png)

**Matriz de covariância ajustada:**
$$
P_{\text{ajustado}} =
\begin{bmatrix}
3.004 & -1.476 \\
-1.476 & 1.002
\end{bmatrix}
$$

**Estatísticas da distribuição ajustada:**

$$
  Corr = -0.5910, Cov = -1.4755 \text{ (exatamente igual à Questão 1.k)}
$$

## Conclusões

1. **Representação visual**: Os gráficos 3D e de contorno mostram claramente a estrutura de covariância da distribuição normal bivariada.
2. **Comparação com transformações lineares**: A distribuição original (Questão 2) tem correlação diferente das transformações lineares com rotação (Questão 1.j), demonstrando que diferentes combinações de transformações podem produzir estruturas de dependência distintas.
3. **Flexibilidade da normal bivariada**: É possível ajustar a matriz de covariância para reproduzir exatamente as propriedades estatísticas de transformações lineares complexas.
4. **Verificação empírica**: As estatísticas amostrais concordam bem com os parâmetros teóricos, validando a metodologia de geração e análise.

As imagens completas estão disponíveis na pasta `images_q2/`.
