def calcular_precio_venta(costo, porcentaje):
    """Calcula el precio de venta de un producto basado en su costo y el porcentaje de ganancia deseado."""
    ganancia = costo * (porcentaje / 100)
    precio_final = costo + ganancia
    return precio_final


def procesar_negocio():
    """Procesa la información de un negocio, calculando la inversión total, el precio de venta total y la ganancia neta."""
    inversion_total = 0
    precio_venta_total = 0
    cant_productos = 0

    while True:
        try:
            cant = input("¿Cuántos productos desea vender?: ")
            cant_productos = int(cant)
            if cant_productos < 1:
                print("Error. Ingrese una cantidad mayor a 0.")
            else:
                break
        except ValueError:
            print("Error. Dato no válido. Ingrese un número entero.")

    for i in range(cant_productos):
        print(f"--- Producto {i+1} ---")
        
        nombre_producto = input("Nombre del producto: ")
        
        while True:
            try:
                costo = float(input("Costo del producto (USD): "))
                if costo <= 0:
                    print("Error. El costo debe ser mayor a 0.")
                else:
                    break
            except ValueError:
                print("Error. Ingrese un número válido para el costo.")
                
        inversion_total = (inversion_total + costo)

        while True:
            try:
                porcentaje = float(input("¿Porcentaje de ganancia deseado? (Ej: 20): "))
                if porcentaje <= 0:
                    print("Error. El porcentaje debe ser mayor a 0.")
                elif porcentaje > 100:
                    print("Error. El porcentaje no puede ser mayor a 100.")
                else:
                    break
            except ValueError:
                print("Error. Ingrese un número válido.")
                      

        precio_individual = calcular_precio_venta(costo, porcentaje)
        precio_venta_total = (precio_venta_total + precio_individual)
        ganancia_individual = (precio_individual - costo)
        print(f"{nombre_producto} se debería vender a: {precio_individual} $")
        print(f"Ganancia de este producto: {ganancia_individual} $")

    print("========RESULTADO GENERAL===========")
    print(f"La inversión total es de: {inversion_total} $")
    print(f"Las ventas totales serán de: {precio_venta_total} $")
    
    ganancia_neta_total = precio_venta_total - inversion_total
    print(f"Y su ganancia neta total es de: {ganancia_neta_total} $")
    print("====================================")


def menu_principal():
    """Función principal que inicia el programa y permite al usuario calcular negocios múltiples."""
    print("=== Cuentas para el Emprendimiento ===")
    
    while True:
        procesar_negocio()
        continuar = input("¿Desea calcular otro negocio? (S/N): ").lower()
        
        if continuar == "s":
             print("Iniciando una nueva simulación de negocio")
        elif continuar == "n":
            print("¡Gracias por usar el sistema! Éxitos en tu negocio.")
            break

menu_principal()