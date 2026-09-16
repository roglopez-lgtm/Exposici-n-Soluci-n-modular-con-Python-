import os

def leer_cliente():
    os.system('cls')
    nombre = input("Ingrese el nombre del cliente: ")
    return nombre

def leer_productos():
    os.system('cls')
    n = int(input("¿Cuántos productos desea registrar?: "))
    
    lista_productos = []
    for i in range(n):
        print(f"\n--- Producto {i+1} ---")
        precio = float(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad: "))
        porcentaje = float(input("Ingrese el porcentaje de descuento (%): "))
        lista_productos.append((precio, cantidad, porcentaje))
        
    impuesto = float(input("\nIngrese el porcentaje de impuesto (IVA): "))
    return lista_productos, impuesto

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

def calcular_total(lista_productos, impuesto):
    subtotal_general = 0
    descuento_general = 0
    
    for precio, cantidad, porcentaje in lista_productos:
        # Usando las funciones del diagrama
        sub_prod = calcular_subtotal(cantidad, precio)
        # O utilizando calcular_total_productos según el diagrama:
        # sub_prod = calcular_total_productos(cantidad, precio)
        
        desc = calcular_descuento(sub_prod, porcentaje)
        
        subtotal_general += sub_prod
        descuento_general += desc
        
    iva = calcular_total_impuesto(subtotal_general, impuesto)
    total = (subtotal_general - descuento_general) + iva
    return subtotal_general, descuento_general, iva, total

def mostrar_factura(nombre, lista_productos, impuesto, subtotal, descuento, iva, total):
    os.system('cls')
    print("="*50)
    print("                 FACTURA GENERAL                ")
    print("="*50)
    print(f"Cliente: {nombre}")
    print("-" * 50)
    print(f"{'Cant':<6} | {'Precio':<10} | {'Subtotal':<10}")
    print("-" * 50)
    
    for precio, cantidad, porcentaje in lista_productos:
        sub_prod = calcular_total_productos(cantidad, precio)
        print(f"{cantidad:<6} | ${precio:<9.2f} | ${sub_prod:<9.2f}")
        
    print("-" * 50)
    print(f"Subtotal acumulado:     ${subtotal:.2f}")
    print(f"Descuento total:       -${descuento:.2f}")
    print(f"IVA ({impuesto}%):          +${iva:.2f}")
    print(f"TOTAL A PAGAR:         ${total:.2f}")
    print("="*50)

def main():
    os.system('cls')
    nombre = leer_cliente()
    lista_productos, impuesto = leer_productos()
    
    subtotal, descuento, iva, total = calcular_total(lista_productos, impuesto)
    
    mostrar_factura(nombre, lista_productos, impuesto, subtotal, descuento, iva, total)

if __name__ == "__main__":
    main()
