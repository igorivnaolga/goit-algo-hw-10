import random
import scipy.integrate as spi

def f(x):
    return x ** 2
    
def monte_carlo_integral(a, b, num_experiments):
    """Estimate the integral of f(x) from a to b using Monte Carlo."""
    total = 0

    for _ in range(num_experiments):
        x = random.uniform(a, b)
        total += f(x)
    return (b - a) * total / num_experiments

a = 0
b = 2
num_experiments = 100000

# Monte Carlo integration
estimated_area = monte_carlo_integral(a, b, num_experiments)
print(f"Monte Carlo estimate of integral from {a} to {b}: {estimated_area}")


# Getting exact integral
def f(x):
    return x**2

a = 0  
b = 2 

# Integral
result, error = spi.quad(f, a, b)

print("Integral: ", result, error)

