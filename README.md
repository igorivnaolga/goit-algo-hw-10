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

Part 1:
Compute the integral using the Monte Carlo method — in other words, estimate the area under the curve (the shaded area).

Part 2:
Verify the result to confirm the accuracy of the Monte Carlo method. Compare it with:

Analytical solution of the integral quad function from scipy.integrate

Make conclusions based on the comparison.

## Conclusion Task 2

In our Monte Carlo simulation with 100,000 random points, the estimated result is typically very close to the exact value (e.g., 2.66), though it may slightly vary each run due to its randomness.
