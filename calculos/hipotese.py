import numpy as np
from scipy.stats import t

# Amostra de Dados

x = [8, 9, 5, 7, 8, 12, 6, 9, 6, 10]


# Média da Amostra de Dados

x_bar = np.mean(x)
print('A média de infrações foi: ', x_bar)


# Desvio Padrão Amostral

desvioPadrao = np.std(x, ddof=1)
print("Desvio Padrão Amostral: ", desvioPadrao)


# Função para cálculo do valor de "t"

def calc_t_value(x, u0, s, n):
    calc1 = x - u0
    calc2 = s / np.sqrt(n)
    calc3 = calc1 / calc2
    return calc3


# Valor de "t"

t_value = calc_t_value(x_bar, 7, desvioPadrao, len(x))
print('O valor de "t" é:', t_value)


# Probabilidade de T ser maior que um valor "tezinho"

df = len(x) - 1  # graus de liberdade
p = t.cdf(t_value, df)
print('A Probabilidade da Distribuição T ser maior que tezinho é:', p)
