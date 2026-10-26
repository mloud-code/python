# Actividad 1

def mostrar_menu():
    """Muestra el menu de opciones"""
    print("1. Cine (10 euros, 2 horas)")
    print("2. Comer (20 euros, 2 horas)")
    print("3. Museo (5 euros, 3 horas)")
    print("4. Deporte (0 euros, 1 hora)")
    print("5. Casa (0 euros, 2 horas)")
    print("0. Salir")

def comprobar_dinero(precio, dinero_que_tengo):
    """Mira si tengo dinero suficiente"""
    if dinero_que_tengo >= precio:
        return True
    else:
        return False

def comprobar_tiempo(horas, tiempo_que_tengo):
    """Mira si tengo tiempo suficiente"""
    if tiempo_que_tengo >= horas:
        return True
    else:
        return False

def ver_resumen(lista, dinero_g, tiempo_g, dinero_s, tiempo_s):
    """Muestra los resultados del dia"""
    print("--- RESUMEN ---")
    print("Actividades:", lista)
    print("Dinero gastado:", dinero_g)
    print("Dinero que queda:", dinero_s)
    print("Tiempo gastado:", tiempo_g)
    print("Tiempo que queda:", tiempo_s)


dinero_actual = -1
while dinero_actual < 0:
    dinero_actual = float(input("Cuanto dinero tienes? "))

tiempo_actual = -1
while tiempo_actual < 0:
    tiempo_actual = float(input("Cuanto tiempo tienes? "))

actividades = []
gasto_d = 0
gasto_t = 0
opcion = "99"

while opcion != "0":
    mostrar_menu()
    opcion = input("Elige (0-5): ")

    precio = 0
    duracion = 0
    nombre = ""
    opcion_correcta = True

    if opcion == "1":
        nombre = "Cine"
        precio = 10
        duracion = 2
    elif opcion == "2":
        nombre = "Comer"
        precio = 20
        duracion = 2
    elif opcion == "3":
        nombre = "Museo"
        precio = 5
        duracion = 3
    elif opcion == "4":
        nombre = "Deporte"
        precio = 0
        duracion = 1
    elif opcion == "5":
        nombre = "Casa"
        precio = 0
        duracion = 2
    elif opcion == "0":
        opcion_correcta = False
    else:
        print("Opcion mala")
        opcion_correcta = False

    if opcion_correcta == True:
        tengo_dinero = comprobar_dinero(precio, dinero_actual)
        tengo_tiempo = comprobar_tiempo(duracion, tiempo_actual)

        if tengo_dinero == True and tengo_tiempo == True:
            print("Actividad añadida")
            dinero_actual = dinero_actual - precio
            tiempo_actual = tiempo_actual - duracion
            
            gasto_d = gasto_d + precio
            gasto_t = gasto_t + duracion
            
            actividades.append(nombre)
        else:
            print("No puedes hacer esto")

ver_resumen(actividades, gasto_d, gasto_t, dinero_actual, tiempo_actual)