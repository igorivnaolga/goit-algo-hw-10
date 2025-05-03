# goit-algo-hw-10

## Task 1: Production Optimization

A company produces two types of beverages: "Lemonade" and "Fruit Juice". The production of these beverages requires various ingredients and a limited amount of equipment. The goal is to maximize the total production given the limited resources.

Conditions of the task:

"Lemonade" is made from Water, Sugar, and Lemon Juice.

"Fruit Juice" is made from Fruit Puree and Water.

Resource constraints:

100 units of Water

50 units of Sugar

30 units of Lemon Juice

40 units of Fruit Puree

Producing 1 unit of Lemonade requires:

2 units of Water

1 unit of Sugar

1 unit of Lemon Juice

Producing 1 unit of Fruit Juice requires:

2 units of Fruit Puree

1 unit of Water

Using PuLP, create a model that determines how many units of "Lemonade" and "Fruit Juice" should be produced to maximize the total number of products, while respecting the resource constraints.

Write a program using PuLP that maximizes the total production of "Lemonade" and "Fruit Juice", given the limitations on ingredient availability.

## Task 2: Definite Integral Estimation

Your second task is to compute the value of a definite integral using the Monte Carlo method.

📖 You can choose any function you like.

Let’s use this function and plot it:

python
Copy
Edit
import matplotlib.pyplot as plt
import numpy as np

# Define the function and integration bounds

def f(x):
return x \*\* 2

a = 0 # Lower limit
b = 2 # Upper limit

# Create a range of x values

x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Create the plot

fig, ax = plt.subplots()

# Plot the function

ax.plot(x, y, 'r', linewidth=2)

# Fill the area under the curve

ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Set up the graph

ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Add vertical lines and a title

ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title(f'Integration graph of f(x) = x^2 from {a} to {b}')
plt.grid()
plt.show()
You will get a visual representation of the integral (the shaded gray area under the curve).

Part 1:
Compute the integral using the Monte Carlo method — in other words, estimate the area under the curve (the shaded area).

Part 2:
Verify the result to confirm the accuracy of the Monte Carlo method. Compare it with:

Analytical solution of the integral

quad function from scipy.integrate

Make conclusions based on the comparison.

## Conclusion Task 2

In our Monte Carlo simulation with 100,000 random points, the estimated result is typically very close to the exact value (e.g., 2.66), though it may slightly vary each run due to its randomness.
