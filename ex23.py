from decimal import Decimal, getcontext

# Define a precisão desejada (por exemplo, 10 casas decimais)
getcontext().prec = 10

def calcular_volume_incerteza_esfera(D, sigma_D):
    # Converte entradas para Decimal
    D = Decimal(D)
    sigma_D = Decimal(sigma_D)

    # Calcular o raio
    r = D / 2

    # Volume da esfera
    V = (Decimal(4) / Decimal(3)) * Decimal('3.141592653589793') * r**3

    # Derivada do volume em relação ao diâmetro
    dV_dD = (Decimal(4) / Decimal(3)) * Decimal('3.141592653589793') * (r**2)

    # Cálculo da incerteza
    incerteza_volume = abs(dV_dD) * sigma_D

    return V, incerteza_volume

# Dados
diametro = 2.03  # cm
sigma_diametro = 0.01 / 2  # Exemplo de incerteza (metade da menor divisão)

# Cálculo do volume e incerteza
volume, incerteza = calcular_volume_incerteza_esfera(diametro, sigma_diametro)
print(f"Volume da esfera: {volume:.4f} cm³, Incerteza: {incerteza:.4f} cm³")



