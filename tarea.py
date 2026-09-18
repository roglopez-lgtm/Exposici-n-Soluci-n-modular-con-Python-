import os  # Importamos el módulo os para poder limpiar la consola con os.system('cls')

def leer_cliente():
    # Limpia la pantalla y solicita el nombre del cliente
    os.system('cls')
    nombre = input("Ingrese el nombre del cliente: ")
    return nombre

def leer_productos():
    # Solicita la cantidad de productos a registrar, y para cada uno pide:
    # precio, cantidad y porcentaje de descuento. También solicita el IVA general.
    # Retorna una lista de tuplas con los datos de los productos y el porcentaje de impuesto.
    os.system('cls')
    n = int(input("¿Cuántos productos desea registrar?: "))
    
    lista_productos = []
    for i in range(n):
        print(f"\n--- Producto {i+1} ---")
        precio = float(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad: "))
        porcentaje = float(input("Ingrese el porcentaje de descuento (%): "))
        # Guardamos cada producto como un grupo dentro de la lista
        lista_productos.append((precio, cantidad, porcentaje))
        
    impuesto = float(input("\nIngrese el porcentaje de impuesto (IVA): "))
    return lista_productos, impuesto

def calcular_subtotal(cantidad, precio):
    # Calcula y retorna el subtotal individual de un producto multiplicando cantidad por precio.
    subtotal = cantidad * precio
    return subtotal

def calcular_total_productos(lista_productos):
    # NUEVO MÓDULO (CAMBIO #1): Recorre la lista de productos y acumula 
    # todos los subtotales antes de aplicar descuentos e impuestos.
    subtotal_acumulado = 0
    for precio, cantidad, porcentaje in lista_productos:
        sub_prod = calcular_subtotal(cantidad, precio)
        subtotal_acumulado += sub_prod
    return subtotal_acumulado

def calcular_descuento(subtotal, porcentaje):
    # Calcula el monto de descuento en base al subtotal y el porcentaje indicado.
    descuento = subtotal * (porcentaje / 100)
    return descuento

def calcular_total_impuesto(subtotal, impuesto):
    # NUEVO MÓDULO (CAMBIO #2): Calcula el valor monetario del impuesto (IVA) 
    # aplicado sobre el subtotal general.
    total_impuesto = subtotal * (impuesto / 100)
    return total_impuesto

def calcular_total(lista_productos, impuesto):
    # Recorre todos los productos para acumular descuentos,
    # utiliza las funciones auxiliares y determina el total final a pagar.
    subtotal_general = calcular_total_productos(lista_productos)
    descuento_general = 0
    
    for precio, cantidad, porcentaje in lista_productos:
        sub_prod = calcular_subtotal(cantidad, precio)
        desc = calcular_descuento(sub_prod, porcentaje)
        descuento_general += desc
        
    iva = calcular_total_impuesto(subtotal_general, impuesto)
    total = (subtotal_general - descuento_general) + iva
    return subtotal_general, descuento_general, iva, total

def mostrar_factura(nombre, lista_productos, impuesto, subtotal, descuento, iva, total):
    # Muestra en pantalla la factura con un formato estructurado y tabular utilizando f-strings.
    os.system('cls')
    print("="*50)
    print("                    FACTURA GENERAL                     ")
    print("="*50)
    print(f"Cliente: {nombre}")
    print("-" * 50)
    print(f"{'Cant':<6} | {'Precio':<10} | {'Subtotal':<10}")
    print("-" * 50)
    
    # Imprime el detalle de cada producto registrado
    for precio, cantidad, porcentaje in lista_productos:
        sub_prod = calcular_subtotal(cantidad, precio)
        print(f"{cantidad:<6} | ${precio:<9.2f} | ${sub_prod:<9.2f}")
        
    print("-" * 50)
    print(f"Subtotal acumulado:     ${subtotal:.2f}")
    print(f"Descuento total:       -${descuento:.2f}")
    print(f"IVA ({impuesto}%):          +${iva:.2f}")
    print(f"TOTAL A PAGAR:        ${total:.2f}")
    print("="*50)

def main():
    # Función principal que coordina el flujo completo del programa de facturación.
    os.system('cls')
    nombre = leer_cliente()
    lista_productos, impuesto = leer_productos()
    
    # Realiza los cálculos matemáticos necesarios
    subtotal, descuento, iva, total = calcular_total(lista_productos, impuesto)
    
    # Genera y muestra la factura final en consola
    mostrar_factura(nombre, lista_productos, impuesto, subtotal, descuento, iva, total)

if __name__ == "__main__":
    main()
