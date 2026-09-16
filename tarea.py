import os

def leer_cliente():
    os.system('cls')
    nombre = input("Ingrese el nombre del cliente: ")
    return nombre

def leer_productos():
    os.system('cls')
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad: "))
    porcentaje = float(input("Ingrese el porcentaje de descuento: "))
    return precio, cantidad, porcentaje

def calcular_subtotal(cantidad, precio):
    subtotal = cantidad * precio
    return subtotal

def calcular_total_productos(cantidad, precio):
    subtotal = cantidad * precio
    return subtotal

def calcular_descuento(subtotal, porcentaje):
    descuento = subtotal * (porcentaje / 100)
    return descuento

def calcular_total_impuesto(subtotal, impuesto):
    total_impuesto = subtotal * (impuesto / 100)
    return total_impuesto

def calcular_total(cantidad, precio, porcentaje, impuesto):
    subtotal = calcular_subtotal(cantidad, precio)
    # Usando calcular_total_productos() como indica el diagrama
    total_prod = calcular_total_productos(cantidad, precio)
    descuento = calcular_descuento(subtotal, porcentaje)
    iva = calcular_total_impuesto(subtotal, impuesto)
    total = (subtotal - descuento) + iva
    return subtotal, descuento, iva, total

def mostrar_factura(nombre, cantidad, precio, porcentaje, impuesto, subtotal, descuento, iva, total):
    os.system('cls')
    print("="*45)
    print("               FACTURA                  ")
    print("="*45)
    print(f"Cliente: {nombre}")
    print(f"Cantidad: {cantidad}")
    print(f"Precio unitario: ${precio:.2f}")
    print(f"Porcentaje de descuento: {porcentaje}%")
    print(f"Porcentaje de impuesto (IVA): {impuesto}%")
    print("-" * 45)
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Descuento: -${descuento:.2f}")
    print(f"IVA: +${iva:.2f}")
    print(f"TOTAL A PAGAR: ${total:.2f}")
    print("="*45)

def main():
    os.system('cls')
    nombre = leer_cliente()
    precio, cantidad, porcentaje = leer_productos()
    
    # Parámetro de impuesto necesario para la factura final
    impuesto = float(input("Ingrese el porcentaje de impuesto (IVA): "))
    
    subtotal, descuento, iva, total = calcular_total(cantidad, precio, porcentaje, impuesto)
    
    mostrar_factura(nombre, cantidad, precio, porcentaje, impuesto, subtotal, descuento, iva, total)

if __name__ == "__main__":
    main()