# Estado inicial
plazas_disponibles = 12

# Asignaciones aumentadas
plazas_disponibles -= 3  # Se reservan 3
plazas_disponibles += 1  # Se cancela 1

print(f"Plazas finales disponibles: {plazas_disponibles}")

# Expresión condicional (Operador ternario)
estado_aula = "Hay plazas" if plazas_disponibles > 0 else "Completo"
print(estado_aula)