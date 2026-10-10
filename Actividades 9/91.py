# Entrada de datos
precio = float(input("Precio del artículo: "))
unidades = int(input("Unidades: "))
descuento_porcentaje = float(input("Porcentaje de descuento: "))

# Procesamiento
subtotal = precio * unidades
descuento = subtotal * (descuento_porcentaje / 100)
base_imponible = subtotal - descuento
iva = base_imponible * 0.21
total = base_imponible + iva

# Salida con formato de dos decimales
print(f"Subtotal: {subtotal:.2f} €")
print(f"Descuento: {descuento:.2f} €")
print(f"IVA (21%): {iva:.2f} €")
print(f"Total: {total:.2f} €")

# Estructura de selección simple
if total > 50.00:
    print("El pedido supera el umbral: Envío gratuito.")