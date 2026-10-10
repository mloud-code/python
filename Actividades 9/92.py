# Variable inicial
duracion_total = 7384

# Procesamiento matemático estricto
horas = duracion_total // 3600
segundos_restantes = duracion_total % 3600

minutos = segundos_restantes // 60
segundos = segundos_restantes % 60

# Salida
print(f"{horas} horas, {minutos} minutos y {segundos} segundos.")