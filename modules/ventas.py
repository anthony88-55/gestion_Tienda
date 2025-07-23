import json
import time
from .productos import acceder_a_datos_json
from config import ruta_products_registrados,ruta_ventas
"""Módulo ventas.py:

Función realizar_venta(**kwargs) que registre ventas (producto, cantidad, cliente).

Validar stock antes de vender (manejar errores)."""

#Crea un contador utilizado como id de la factura
def crear_contador(inicio):
    
    
    #inicializa la variable contador con el valor ingresado
    contador = inicio
    
    #Funcion anidada que se encarga de la logica de la venta como ver si existe el producto
    #si hay las unidades necesarias en stock, 
    def realizar_ventas(**datos_venta):
        
        try:
            #Accede a la variable contador de la funcion mas cercana
            nonlocal contador
            productos_registrados = acceder_a_datos_json(ruta_products_registrados)
            
            #valida si los productos de la venta existen en los productos de registrados
            if datos_venta["Producto"] in productos_registrados:
            
                #itera sobre la variable productos_registrados
             for clave, valor in productos_registrados.items():
                
                    #Valida que la clave sea la misma tanto en los datos los prodeuctos registrados como en los datos de la venta
                    if clave.lower() == datos_venta["Producto"].lower():
                    
                        #Este condicional verifica que las unidades pedidas por el cliente si las haya en el stock
                        if valor["Stock"] < datos_venta["Cantidad"]:
                        
                            #Notifica que no hay la cantidad solicitada y muestra cuantas unidades hay en stock
                            print(f"No hay esa cantidad de productos en {clave}. En stock tenemos {valor["Stock"]}")
                        
                        #Se ejecuta en caso de que si haya las unidades solicitadas
                        else:
                            #Notifica que si tenemos las unidades
                            print("Si tenemos esas unidades de", clave)
                        
                            #Actualiza la variable con los nuevos cambios en el stock
                            productos_registrados.update({clave: {"Precio":valor["Precio"], "Stock":valor["Stock"] - datos_venta["Cantidad"]}})
                            
                            
                            #Actualiza los datos del archivo porductos_registrados
                            with open(ruta_products_registrados, 'w') as archivo:
                                json.dump(productos_registrados, archivo, indent=4)                          
                             
        
                            # Aumentamos el contador por cada llamada de la funcion principal
                            contador += 1
                            
                            #Accede a la funcincion acceder_a_datos_json para obtener los datos del archivo registro_ventas.json
                            registro_ventas = acceder_a_datos_json(ruta_ventas)

                            #Variable que almacena la fecha actual en que se hizo la compra
                            fecha = time.strftime("%Y-%m-%d", time.localtime())
                            
                            #Variable que almacena la hora actual en la que se hizo la compra
                            hora = time.strftime("%H:%M:%S", time.localtime())
                            
                            #Calcula el precio de la compra
                            precio_total = (valor["Precio"] * datos_venta["Cantidad"])
                            
                            #Actualiza la varible con los nuevos datos
                            registro_ventas.update({contador: {"Producto": datos_venta["Producto"], "Cantidad": datos_venta["Cantidad"],"Total": [precio_total * 0.8," Con descuento"]  if precio_total > 15000 else precio_total , "Cliente": datos_venta["Cliente"], "Fecha": fecha, "Hora": hora}})
                            

                            #Escribe en el archvo registro_ventas.json los nuevos datos junto con los datos antiguos
                            with open(ruta_ventas, 'w') as archivo:
                                json.dump(registro_ventas, archivo, indent=4)
                            
                             #Devolvemos la variable registro_ventas con la venta hecha
                            return contador, datos_venta["Producto"], datos_venta["Cantidad"], str(precio_total * 0.8) + " Se le aplico un descuento del 20%" if precio_total > 15000 else precio_total , datos_venta["Cliente"], fecha, hora

            #Se ejecuta si el nombre del producto solcitado por el cliente no existe en el catalogo
            else:
            
                #Notifica que producto no existe
                print("El producto", datos_venta["Producto"], "no existe")
                
        except TypeError as e:
            print("Por favor ingresa bien los datos. Estamos esperando datos tipo **kwargs (clave - valor)", e)
            
     
        except Exception as e:
            print(f"A ocurrido un error: {e}")   
       
    
    #Devolvemos la funcion 
    return realizar_ventas


#Funcion para acceder al ultimo valor del archivo registro_ventas.json
def obtener_ultimo_valor_de_ventas():
    
    try:
        #Leemos los datos del archivo json y los almacenamos en la variable
        registro_ventas = acceder_a_datos_json(ruta_ventas)
    
        #Accedemos al ultimo valor del diccionario como tupla
        utimo_valor = next(reversed(registro_ventas.items()))
    
        #convierte el valor en entero y lo vuelve a almacenar
        utimo_valor = int(utimo_valor[0])
        
        #Devolvemos la clave del ultimo valor que funciona como un id de la venta
        return utimo_valor
    #Manela la excepcion cuando el archivo no tiene ningun dato para iterar
    except StopIteration:
        
        #Establecemos el valor 0 por defecto
        ultimo_valor = 0
        
        return ultimo_valor



if __name__ == "__main__":
    #Almacenamos el valor que devuelve la funcion
    ultimo_valor = obtener_ultimo_valor_de_ventas()
    operacion = crear_contador(obtener_ultimo_valor_de_ventas())
    try:
        contador, nombre, cantidad, total, cliente, fecha, hora = operacion(Producto="Leche", Cantidad = 7, Cliente = "Daniela Carolina")
        print(
        f"""Venta realizada:
    
        Factura NO: #{contador}
        Nombre del producto: {nombre}
        Cantidad:  {cantidad}
        Total a pagar: ${total}
        Pagado por: {cliente}
        
        Fecha de facturacion: {fecha} {hora}
    
        """
    )
    except TypeError:
        print("Sin factura")





            