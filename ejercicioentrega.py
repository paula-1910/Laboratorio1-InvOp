from pyomo.environ import *

# 1. Crear el modelo
model = ConcreteModel()

# 2. Definir las variables
model.x1 = Var(within=NonNegativeReals)  # Litros de Verde Manzana
model.x2 = Var(within=NonNegativeReals)  # Litros de Verde Pino

# 3. Definir la función objetivo
model.obj = Objective(expr=1.0 * model.x1 + 1.20 * model.x2, sense=maximize)

# 4. Definir las restricciones
model.res_azul = Constraint(expr=0.3 * model.x1 + 0.5 * model.x2 <= 20)
model.res_amarillo = Constraint(expr=0.7 * model.x1 + 0.5 * model.x2 <= 28)
model.res_limite_manzana = Constraint(expr=model.x1 <= 30)

# 5. Resolver el problema
solver = SolverFactory('glpk', executable='C:\glpk-4.65\w64\glpsol.exe')  
solver.solve(model)

# 6. Mostrar resultados
print(f"Litros Verde Manzana (x1): {value(model.x1)} L")
print(f"Litros Verde Pino (x2): {value(model.x2)} L")
print(f"Beneficio Total: {value(model.obj)} €")