# Estado inicial (Denegado)
esta_matriculada = True
autorizacion_especial = False
edad = 17

# Expresión booleana
puede_acceder = (esta_matriculada and edad >= 18) or autorizacion_especial
print(f"Intento 1 - Acceso permitido: {puede_acceder}")

# Cambio de valores para forzar el acceso (Aprobado)
edad = 18 
# También serviría: autorizacion_especial = True

puede_acceder = (esta_matriculada and edad >= 18) or autorizacion_especial
print(f"Intento 2 - Acceso permitido: {puede_acceder}")