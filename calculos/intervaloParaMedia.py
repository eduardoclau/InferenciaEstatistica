import math

# Se o desvio padrão FOR CONHECIDO


def conf_interval_media(desvio_padrao, media, n, level):
    # valor crítico da distribuição normal padrão
    z = {0.90: 1.645, 0.95: 1.96, 0.99: 2.576}[level]
    intervalo_de_confianca = z * (desvio_padrao / math.sqrt(n))
    limite_inferior = media - intervalo_de_confianca
    limite_superior = media + intervalo_de_confianca
    return limite_inferior, limite_superior


resultado = conf_interval_media()
print('Caso o Desvio Padrão CONHECIDO:  ', resultado)


# Se o desvio padrão for DESCONHECIDO

def conf_interval_media_desvio_desconhecido(s, media, n, t):
    intervalo_de_confianca = t * (s / math.sqrt(n))
    limite_inferior = media - intervalo_de_confianca
    limite_superior = media + intervalo_de_confianca
    return limite_inferior, limite_superior


resultado2 = conf_interval_media_desvio_desconhecido()
print('Caso o Desvio Padrão DESCONHECIDO:   ', resultado2)


# Margem de erro

def margem_de_erro(t, s, n):
    calc1 = t
    calc2 = s
    calc3 = n**(1/2)
    calc4 = calc2 / calc3
    margemDeErro = calc1 * calc4
    return margemDeErro


resultado3 = margem_de_erro()
print('Margem de Erro:  ', resultado3)
