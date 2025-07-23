from config import ruta_products_registrados, ruta_ventas
from .productos import acceder_a_datos_json


# Funcion que genera reporte de los productos, espera variable detalle(sencillo ó detallado) precio_max para filtrar hasta el precio maximo que se indique
def generar_reporte_productos(**detalle_reporte):

    try:
        # Accede a los datos de los productos registrados
        productos = acceder_a_datos_json(ruta_products_registrados)

        # Condicional que verifica si el valor de la variable detalle_reporte con la clave detalle es igual a sencillo
        if detalle_reporte["detalle"].lower() == "sencillo":

            # Muestra que el reporte que se esta generando es sencillo
            print("Reporte sencillo generado: ")

            # Bucle para acceder a los datos
            for clave, valor in productos.items():

                # Condicional que verifica si el precio del producto es menor o igual al el precio maximo ingresado
                if valor["Precio"] <= detalle_reporte["precio_max"]:

                    # Mustra solo la clave (el nombre del producto) ya que es un reporte sencillo
                    print(clave)

        # sino se cumple la primera condicion entonces este condicional verifica si en la varable detalle_reporte con la clave detalle es igual a detallado
        elif detalle_reporte["detalle"].lower() == "detallado":

            # Informa que se esta generando el informe detalldo
            print("Reporte detallado generado: ")

            # Fila de titulos
            print("Nombre | Precio | Cantidad")

            # Bucle para acceder a los valores
            for clave, valor in productos.items():

                # Vericia que el precio de los productos sea menor o igual al valor de la variable precio_max
                if valor["Precio"] <= detalle_reporte["precio_max"]:

                    # Muestra los datos que cumplan la condicion
                    print(f"{clave} | {valor["Precio"]} | {valor["Stock"]}")

        # Sino se cumplen las dos condiciones se ejecuta esta condicion
        else:

            # Lanza una exepcion
            raise Exception("El tipo de detalle ingresado no existe")

    # Manejo de cualquier error
    except Exception as e:
        print(f"Error al generar el reporte: {e}")


# Funcion para generar reporte de ventas, la primera variable debe tener el valor Diario o Mensual
# La segunda variable se espera que tenga fecha_desde, fecha_hasta o agrupar_cliente
def reporte_ventas(*filtro, **agrupacion):

    try:

        # Accede a los dartos del archivo registro_ventas.json
        registro_ventas = acceder_a_datos_json(ruta_ventas)

        # Condicional que verifica si la palabra Diario existe en la variable filtro
        if "Diario" in filtro:

            # Inicializamos la variable como una lista vacia
            fecha_actual = []

            # Bucle que itera sobre la variable que almacena los datos de las ventas
            for venta in registro_ventas.values():

                # Condicional que toma el numero del dia de la fecha por medio de slicing
                # Verifica si ese numero no existe en la variable fecha actual
                if venta["Fecha"][8:] not in fecha_actual:

                    # Agrega de ultimo el valor que no existe
                    fecha_actual.append(venta["Fecha"][8:])

            # Vefica que esos datos esten en la variable agrupacion
            if "fecha_desde" in agrupacion or "fecha_hasta" in agrupacion:

                # Itera sobre la variable tipo lista fecha_actual
                for fecha in fecha_actual:

                    # Muestra el valor de la variable fecha
                    print("Dia:", fecha)

                    # Itera sobre la variable que almacena todos los datos de las ventas (solo itera el valor)
                    for venta in registro_ventas.values():

                        # Condicional que verifica que el dia de la venta sea igual al dia que se esta iterando
                        # Tambien verifica si la fecha de venta es mayor o igual a la fecha ingresada y si la fecha de venta
                        # Es menor o igual a la fecha ingresada por el ususario
                        if (
                            venta["Fecha"][8:] == fecha
                            and venta["Fecha"] >= agrupacion["fecha_desde"]
                            and venta["Fecha"] <= agrupacion["fecha_hasta"]
                        ):
                            
                            # Si se cumple la condicion imprime los datos
                            print(
                                f"""
                                    Producto: {venta["Producto"]}
                                    Cantidad: {venta["Cantidad"]}
                                    Cliente: {venta["Cliente"]}
                                    """
                            )
                            
            # Si la primera condicion no se cumple entonces se ejecuta esta
            # Verifica si agrupar_cliente existe en la varible agrupacion
            elif "agrupar_cliente" in agrupacion:

                #bucle para iterar sobre las fechas almacenadas
                for fecha in fecha_actual:
                    
                    #Muestra el dia qu esta iterando
                    print("Dia:", fecha)
                    
                    ##Bucle anidado que itera sobre la variable que tiene los datos de las ventas
                    for venta in registro_ventas.values():

                        # Condicional que verifica que los ultimos digitos de la fecha de venta del producto sea igual al valor de fecha en esa iteracion
                        #Verifica que el valor de la variable venta en la posicion cliente sea igual al valor de la variable agrupacion en la posicion agrupar_cliente
                        if (
                            venta["Fecha"][8:] == fecha
                            and venta["Cliente"] == agrupacion["agrupar_cliente"]
                        ):
                            
                            #Si se cumple la condicion muestra los datos
                            print(
                                f"""
                                    Producto: {venta["Producto"]}
                                    Cantidad: {venta["Cantidad"]}
                                    Cliente: {venta["Cliente"]}
                                    """
                            )
                            
        #Si no se cumple la primera condicion entonces se ejecuta esta
        #Verifica que la palabra Mensual este en filtro
        elif "Mensual" in filtro:
            
            #Instancia la variable fecha actual como una lista vacia
            fecha_actual = []
            
            # Itera sobre la variable que tiene todos los registros de las ventas
            for venta in registro_ventas.values():
                
                #Por medio de slicing accede al valor del mes de la fecha y verifica si ese valo esta en la variable fecha_actual
                if venta["Fecha"][5:7] not in fecha_actual:
                    
                    #Si la condicion se cumple agrega a la ultima posicion la fecha en la lista
                    fecha_actual.append(venta["Fecha"][5:7])
            
            # Condicion que verifica si la clave agrupar_cliente existe en agrupacion
            if "agrupar_cliente" in agrupacion:

                # Itera sobre la fecha actual
                for fecha in fecha_actual:
                    
                    #Muesta el valor de la variable fecha que esta iterando 
                    print("Mes:", fecha)
                    
                    #Itera sobre la variable que tiene todos los registros de las ventas
                    for venta in registro_ventas.values():

                        #Condicional que valida si el mes es igual al valor de la variable fecha
                        #Tambien verifica si el nombre del cliente es igual al nombre que el usuario ingreso
                        if (
                            venta["Fecha"][5:7] == fecha
                            and venta["Cliente"] == agrupacion["agrupar_cliente"]
                        ):
                            
                            # Muestra los datos 
                            print(
                                f"""
                                    Producto: {venta["Producto"]}
                                    Cantidad: {venta["Cantidad"]}
                                    Cliente: {venta["Cliente"]}
                                    """
                            )
                            
            # Verifica si las dos claves estan en la variable agrupacion
            elif "fecha_desde" in agrupacion or "fecha_hasta" in agrupacion:
                
                #Itera sobre la vable fecha actual
                for fecha in fecha_actual:
                    
                    #Muestra el el mes que esta iterando
                    print("Mes:", fecha)
                    
                    #Iterador para los datos de las ventas
                    for venta in registro_ventas.values():
                        
                        #Condicional que valida si el mes es igual al valor de la variable fecha
                        #Tambien verifica si la fecha de la venta esta entre el rango ingresado por el usuario
                        if (
                            venta["Fecha"][5:7] == fecha
                            and venta["Fecha"] >= agrupacion["fecha_desde"]
                            and venta["Fecha"] <= agrupacion["fecha_hasta"]
                        ):
                            print(
                                f"""
                                    Producto: {venta["Producto"]}
                                    Cantidad: {venta["Cantidad"]}
                                    Cliente: {venta["Cliente"]}
                                    """
                            )
    #Manejo de errores
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    # productos  = {'Pimenton': {'Precio': 200, 'Stock': 5}, 'Azucar': {'Precio': 800, 'Stock': 5}, 'Leche': {'Precio': 3000, 'Stock': 5}, 'Arroz': {'Precio': 1300, 'Stock': 10}}
    generar_reporte_productos(detalle="sencillo", precio_max= 800)

    # filtroDiario("Diario", agrupar_cliente = "Daniel armesto")
    # filtroDiario("Diario", fecha_desde = "2025-07-16", fecha_hasta = "2025-07-18")
    #filtroDiario("Mensual", agrupar_cliente = "Daniel armesto")
    #reporte_ventas("Mensual", fecha_desde="2025-07-16", fecha_hasta="2025-09-18")
