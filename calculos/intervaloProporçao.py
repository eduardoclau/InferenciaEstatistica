import math


def conf_interval_prop(p, n, level):
    # valor crítico da distribuição normal padrão
    z = {0.90: 1.645, 0.95: 1.96, 0.99: 2.576}[level]
    interval = z * math.sqrt(p * (1 - p) / n)
    lower_bound = p - interval
    upper_bound = p + interval
    return lower_bound, upper_bound


resultado = conf_interval_prop()
print(resultado)
