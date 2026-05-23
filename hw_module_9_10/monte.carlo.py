import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

def f(x):
    return np.sin(x) + 1

a = 0           # нижня межа
b = np.pi       # верхня межа
N = 100000
y_max = 2       # макс значення при sin 1

x_rand = np.random.uniform(a, b, N)
y_rand = np.random.uniform(0, y_max, N)

under_curve = y_rand < f(x_rand)
N_under = np.sum(under_curve)

S = (b - a) * y_max

integral_mc = S * (N_under / N)
integral_quad, error_quad = quad(f, a, b)

print(f"---Результати:---")
print(f"Метод Монте-Карло (N={N}):           {integral_mc:.6f}")
print(f"quad (SciPy):                           {integral_quad:.6f}")
print(f"Абсолютна похибка методу Монте-Карло:   {abs(integral_mc - integral_quad):.6f}")

# Створення графіка
plt.figure(figsize=(10, 6))
x_plot = np.linspace(-0.5, np.pi + 0.5, 400)
plt.plot(x_plot, f(x_plot), 'g', linewidth=2, label='$f(x) = \\sin(x) + 1$')

N_visual = 2500
plt.scatter(x_rand[:N_visual], y_rand[:N_visual], c=under_curve[:N_visual],
            cmap='coolwarm', s=2, alpha=0.6, label='Random points')

plt.axvline(x=a, color='gray', linestyle='--')
plt.axvline(x=b, color='gray', linestyle='--')
plt.xlim([-0.3, np.pi + 0.3])
plt.ylim([0, y_max + 0.3])
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title(f'Метод Монте-Карло для f(x) = sin(x) + 1\nMC: {integral_mc:.4f} vs quad (SciPy): {integral_quad:.4f}')
plt.grid(True)
plt.show()