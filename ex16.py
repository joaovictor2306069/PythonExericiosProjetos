import sympy as sp

# Definir variáveis de tempo
t = sp.Symbol('t')

# Definir funções para a quantidade de sal nos tanques A e B
A = sp.Function('A')(t)
B = sp.Function('B')(t)

# Definir as taxas de variação
dA_dt = sp.Eq(sp.diff(A, t), -8 * A / 10 + 3 * B / 20)
dB_dt = sp.Eq(sp.diff(B, t), 8 * A / 10 - 3 * B / 20 - 5 * B / 20)

# Resolver as equações diferenciais
sol = sp.dsolve((dA_dt, dB_dt))

# Substituir as condições iniciais
A_0 = 6  # kg de sal no tanque A no instante t=0
B_0 = 0  # kg de sal no tanque B no instante t=0

# Substituir as constantes
C1_C2_sol = sp.solve([sol[0].rhs.subs(t, 0) - A_0, sol[1].rhs.subs(t, 0) - B_0])
sol_A = sol[0].rhs.subs(C1_C2_sol)
sol_B = sol[1].rhs.subs(C1_C2_sol)

# Avaliar a solução em t=10
sal_A_10_min = sol_A.subs(t, 10)
sal_A_10_min.evalf(2)
