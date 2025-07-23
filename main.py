from importaciones import *


operacion = None
acceder_a_datos_json(ruta_ventas)
while operacion != 0:

    print("Hola!. ¿Que operacion quieres realizar el dia de hoy?")
    print(
    """
Menú: 
0. Salir del programa
1. Registrar productos
2. Filtrar producto por nombre o precio
 (si va a filtrar por nombre no ingrese ningún precio)
3. Ordenar producto (Por Nombre o Precio)
4. Realizar venta
5. Generar reporte de los productos
6. Generar reporte de ventas
"""
)

    operacion = int(input("Ingresa el numero de la operación: "))


    match operacion:
    
        case 1 :
            try:
                nombre_producto = input("\nIngresa el nombre del producto: ")
                precio = int(input("Ingresa el precio: "))
                stock = int(input("Ingresa la cantidad de unidades: "))
                datos = agregar_productos(nombre_producto, precio, stock)
        
            except Exception as e:
                print("Error en la operacion", e)
            else:
                print("Producto guardado correctamtente\n\n")
                
        case 2:
        
            try:
                tipo_filtro = int(input("\n1. Para filtrar por nombre\n2. Para filtrar por precio\n\nTipo de filtro: "))
                print("\n")

                if tipo_filtro == 1:
                    nombre_producto = input("Ingresa el nombre del producto que quieres buscar: ")
                    buscar_nombre_precio(0, 0, nombre_producto)
                elif tipo_filtro == 2:
                    precio_desde = int(input("Precio desde: "))
                    precio_hasta = int(input("Precio hasta: "))
                    print("\n")
                    buscar_nombre_precio(precio_desde, precio_hasta)
                
            except Exception as e:
                print("\nError en la operacion:",e)
            else:
                print("\nOperacion exitosa\n\n")
        case 3:
            
            try:
            
                tipo_orden = int(input("\n1. Ordenar por Precio\n2. Odenar por Nombre\n\nTipo de orden: "))
                print("\n")

                if tipo_orden == 1:
            
                    ordenar_producto(tipo_orden)
            
                elif tipo_orden == 2:
            
                    ordenar_producto(2)
        
            except Exception as e:
                print("\nError en la operacion:",e)
            else:
                print("\nOperacion exitosa\n\n")
            
        case 4:
            try:
                producto_vendido = input("\nIngresa el nombre del producto: ")
                cantidad = int(input("Cantidad de unidades: "))
                nombre_cliente = input("Ingrese el nombre del cliente: ")
            
                print("\n")
            
                ultimo_id = obtener_ultimo_valor_de_ventas()
                operacion = crear_contador(ultimo_id)

                contador, nombre, cantidad, total, cliente, fecha, hora = operacion(Producto=producto_vendido, Cantidad = cantidad, Cliente = nombre_cliente)
        
                print(
                f"""\nVenta realizada:
    
                Factura NO: #{contador}
                Nombre del producto: {nombre}
                Cantidad:  {cantidad}
                Total a pagar: ${total}
                Pagado por: {cliente}
        
                Fecha de facturacion: {fecha} {hora}
    
                """)
            except Exception as e:
                print("\nError en la operación")
            else:
                print("\nOperacion exitosa\n\n")
            
        case 5:
        
            try:
                tipo_detalle_reporte = int(input("\n1. Para reportes sencillo\n2. Para reportes detallados\n\nIngrese el tipo de reporte: "))
                precio_maximo = int(input("Ingresa el precio máximo para filtrar: "))
                print("\n")
            
                if tipo_detalle_reporte == 1:
                
                    generar_reporte_productos(detalle="sencillo", precio_max= precio_maximo)  
                
                elif tipo_detalle_reporte == 2:
                
                    generar_reporte_productos(detalle="detallado", precio_max= precio_maximo)  

            except Exception as e:
            
                print("\nError en la operación")
            else:
                print("\nOperacion exitosa\n\n")
            
        case 6:
            try: 
                tipo_reporte = int(input("\n1. Para reporte Diario\n2. Para reporte Mensual\n\nTipo de reporte: "))
                tipo_filtro_fc = int(input("\n1. Para agrupar por nombre de cliente\n2. Para agrupar por fechas\n\nTipo de agrupación: "))
        
                print("\n")
        
                if tipo_reporte == 1 and tipo_filtro_fc == 1:
                    agrupar_cliente = input("Ingresa el nombre del cliente a buscar: ")
                    print("\n")
                    reporte_ventas("Diario", agrupar_cliente = agrupar_cliente)
            
                elif tipo_reporte == 1 and tipo_filtro_fc == 2:
                    fecha_desde = input("Ingresa la fecha desde: ")
                    fecha_hasta = input("Ingresa la fecha hasta: ")
                    print("\n")
            
                    reporte_ventas("Diario", fecha_desde= fecha_desde, fecha_hasta=fecha_hasta)
            
                elif tipo_reporte == 2 and tipo_filtro_fc == 1:
            
                    agrupar_cliente = input("Ingresa el nombre del cliente a buscar: ")
                    print("\n")
                    reporte_ventas("Mensual", agrupar_cliente = agrupar_cliente)
        
                elif tipo_reporte == 2 and tipo_filtro_fc == 2:
                    fecha_desde = input("Ingresa la fecha desde: ")
                    fecha_hasta = input("Ingresa la fecha hasta: ")
                    print("\n")
            
                    reporte_ventas("Mensual", fecha_desde= fecha_desde, fecha_hasta=fecha_hasta)
            
                else:
                    print("Ingresaste un dato no válido")
                
            except Exception as e:
                print("\nError en la operacion:", e)
            else:
                print("Operacion exitosa\n\n")
        case 0:
            print("\nSaliendo del programa...")
        case _:
            print("Esa operacion no existe")
            