import pulp

# Create a maximization problem
model = pulp.LpProblem("Maximize Beverage Production", pulp.LpMaximize)

# Define Decision Variables
L = pulp.LpVariable('Lemonade', lowBound=0, cat='Integer') # number of units of Lemonade product
J = pulp.LpVariable('Juice', lowBound=0, cat='Integer') # number of units of Juice product

# Objective Function Total Products
model += L + J, "Total Products"

# Add Resource Constraints
model += 2 * L + 1 * J <= 100  # Water constraint
model += 1 * L <= 50  # Sugar constraint
model += 1 * L <= 30  # Lemon Juice constraint
model += 2 * J <= 40  # Fruit puree constraint


# Solve model
model.solve()

# Results
print("Lemonade:", L.varValue)
print("Juice:", J.varValue)
print("Total production:", pulp.value(model.objective))
