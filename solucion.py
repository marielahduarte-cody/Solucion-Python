import os

def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

def ingresa_cliente():
    limpiar_pantalla()
    nombre_cliente = input("Ingrese el nombre del cliente: ").strip()
    print(f"\nCliente registrado: {nombre_cliente}")
    input("\nPresione Enter para continuar...")
    return nombre_cliente

def ingresar_productos():
    limpiar_pantalla()
    lista_productos = []
    print("=== REGISTRO DE PRODUCTOS ===")
    
    while True:
        nombre = input("\nNombre del producto (o 'fin' para terminar): ").strip()
        if nombre.lower() == 'fin':
            break
            
        try:
            precio_base = float(input("Precio unitario: $"))
            cantidad = int(input("Cantidad: "))
            precio_final = calcular_precio_promocional(precio_base, cantidad)
            
            lista_productos.append({
                'nombre': nombre,
                'precio': precio_final,
                'cantidad': cantidad
            })
        except ValueError:
            print("Error: Ingrese un precio o cantidad válida.")
            
    return lista_productos

def calcular_precio_promocional(precio_base, cantidad):
    """CAMBIO #2: Determina precio especial si alcanza el mínimo."""
    MINIMO_PROMOCIONAL = 5
    DESCUENTO_PROMO = 0.15 
    
    if cantidad >= MINIMO_PROMOCIONAL:
        precio_especial = precio_base * (1 - DESCUENTO_PROMO)
        print(f"  ¡Promoción aplicada! Precio unitario especial: ${precio_especial:.2f}")
        return precio_especial
    return precio_base

def calcular_subtotal(precio, cantidad):
    return precio * cantidad

def calcular_descuento(subtotal, porcentaje):
    return subtotal * (porcentaje / 100)

def calcular_total_productos(lista_productos):
    """CAMBIO #1: Acumula los subtotales de la lista de productos."""
    subtotal_acumulado = 0
    for prod in lista_productos:
        subtotal_acumulado += calcular_subtotal(prod['precio'], prod['cantidad'])
    return subtotal_acumulado

def calcular_total(subtotal_acumulado, porcentaje_desc, tasa_impuesto):
    descuento = calcular_descuento(subtotal_acumulado, porcentaje_desc)
    monto_con_descuento = subtotal_acumulado - descuento
    iva = monto_con_descuento * (tasa_impuesto / 100)
    total = monto_con_descuento + iva
    return total, subtotal_acumulado, descuento, iva

def main():
    cliente = ""
    productos = []

    while True:
        limpiar_pantalla()
        print("-" * 47)
        print("=============== Venta de productos ==============")
        print(f" Cliente actual: {cliente if cliente else 'No registrado'}")
        print("-" * 47)
        print("Menu de opciones: ")
        print("1. Leer cliente")
        print("2. Ingresar productos y facturar")
        print("3. Salir")
        print("-" * 47)
        
        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Error: Ingrese un número válido.")
            input("\nPresione Enter para continuar...")
            continue

        match opcion:
            case 1:
                cliente = ingresa_cliente()
            case 2:
                productos = ingresar_productos()
                if productos:
                    subtotal_acumulado = calcular_total_productos(productos)

                    porcentaje_desc = 10.0  
                    tasa_iva = 15.0         
                    
                    total, subtotal, desc, iva = calcular_total(
                        subtotal_acumulado, porcentaje_desc, tasa_iva
                    )
                    print("\n" + "="*30 + " RESUMEN FACTURA " + "="*30)
                    print(f"Subtotal Acumulado: ${subtotal:.2f}")
                    print(f"Descuento ({porcentaje_desc}%): -${desc:.2f}")
                    print(f"IVA ({tasa_iva}%): +${iva:.2f}")
                    print(f"TOTAL A PAGAR: ${total:.2f}")
                    input("\nPresione Enter para regresar al menú...")
                else:
                    print("\nNo se registraron productos.")
                    input("\nPresione Enter para continuar...")
            case 3:
                print("Saliendo del programa...")
                break
            case _:
                print("Opción inválida.")
                input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    main()