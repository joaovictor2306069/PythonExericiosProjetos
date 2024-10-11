import math
from decimal import Decimal, getcontext


getcontext().prec = 10

def calcular_incerteza_volume(D, L, sigma_D, sigma_L):

    D = Decimal(D)
    L = Decimal(L)
    sigma_D = Decimal(sigma_D)
    sigma_L = Decimal(sigma_L)

    # Calcula o volume do cilindro
    r = D / 2
    volume = Decimal('3.141592653589793') * (r ** 2) * L  # Volume do cilindro


    termo1 = (Decimal('3.141592653589793') * (r ** 2) * L).sqrt() * sigma_D
    termo2 = (Decimal('3.141592653589793') * (D / 2) ** 2).sqrt() * sigma_L

    incerteza_volume = (termo1 ** 2 + termo2 ** 2).sqrt()

    return volume, incerteza_volume

materiais = [
    {'D': 1.95, 'L': 4.0, 'sigma_D': 0.05, 'sigma_L': 0.05},  # Material 1
    {'D': 1.90, 'L': 4.05, 'sigma_D': 0.05, 'sigma_L': 0.05}, # Material 2
    {'D': 1.92, 'L': 4.00, 'sigma_D': 0.05, 'sigma_L': 0.05}, # Material 3
    {'D': 1.93, 'L': 4.05, 'sigma_D': 0.05, 'sigma_L': 0.05}, # Material 4
    {'D': 1.63, 'L': 7.62, 'sigma_D': 0.05, 'sigma_L': 0.05}, # Material 5
]

# Cálculo para cada material
for i, material in enumerate(materiais, start=1):
    volume, incerteza = calcular_incerteza_volume(
        material['D'],
        material['L'],
        material['sigma_D'],
        material['sigma_L']
    )
    print(f"Material {i}: Volume = {volume:.4f} cm³, Incerteza = {incerteza:.4f} cm³")






