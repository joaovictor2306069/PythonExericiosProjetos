import math
from decimal import Decimal, getcontext

# Define a precisão desejada (por exemplo, 10 casas decimais)
getcontext().prec = 10

def calcular_incerteza_densidade(m, V, sigma_m, sigma_V):
    # Converte entradas para Decimal
    m = Decimal(m)
    V = Decimal(V)
    sigma_m = Decimal(sigma_m)
    sigma_V = Decimal(sigma_V)

    # Calcula a densidade
    rho = m / V

    # Calcula as derivadas parciais
    d_rho_d_m = 1 / V
    d_rho_d_V = -m / (V ** 2)

    # Calcula a incerteza na densidade
    termo1 = (d_rho_d_m * sigma_m) ** 2
    termo2 = (d_rho_d_V * sigma_V) ** 2
    sigma_rho = (termo1 + termo2).sqrt()

    return rho, sigma_rho

# Exemplo de uso
massa = 31.54 # em gramas
volume = 15.90 # em cm³
sigma_m = 0.01  # incerteza na massa em gramas
sigma_V = 0.19  # incerteza no volume em cm³

# Cálculo da densidade e sua incerteza
densidade, incerteza_densidade = calcular_incerteza_densidade(massa, volume, sigma_m, sigma_V)
print(f"Densidade = {densidade:.4f} g/cm³, Incerteza = {incerteza_densidade:.4f} g/cm³")
