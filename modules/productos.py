import json
from config import ruta_products_registrados
"""unciones para:

Agregar productos (nombre, precio, stock).

Buscar por nombre o rango de precios (*args para filtros).

Ordenar productos por precio/nombre (usando sorted + lambda)."""


#funcion para acceder a los datos del archivo productos_registrados.json
def acceder_a_datos_json(ruta_products_registrados):
    with open(ruta_products_registrados, 'r') as archivo:
        productos = json.load(archivo)
        
    return productos

#Funcion para agregar productos al archivo
def agregar_productos(nombre, precio, stock):
    try:
        
        #Instanciamos la variable como tipo diccionario que almacenara
        productos = {}
        
        #llama la funcion que accede a los datos del archivo json que tiene los productos registrados
        productos = acceder_a_datos_json(ruta_products_registrados)
        
        
        #Actualiza la variable productos con los nuevos productos ingresados por el usuario
        productos.update({nombre: {"Precio": precio,"Stock": stock}})
        
        #Escribe en el archivo los  datos de la variblae productos en formato json (indent=4)
        with open(ruta_products_registrados, 'w') as archivo:
            json.dump(productos, archivo, indent=4)
        
        #Devuelve todos los datos
        return productos

    #Seccion de manejo de errores

    #Meneja error de tipo de dato
    except TypeError:
        print("Tipo de dato incorrecto")
    
    
    #Maneja error cuando no encuentre el archivo
    except FileNotFoundError:
         print("no se encontro el archivo")
         
    #Manejo de cualquier error no registrado
    except Exception as e:
        print("Ha ocurrido un error", e)
    

#Funcion para buscar productos por nombre o precio
def buscar_nombre_precio(precio_desde = 0, precio_hasta = 0, *nombre):
    
    #instancia la variable como None
    filtro_encontrado = None
    
    #Llama la funcion que accede a los datos del archivo que almacena los datos (productos_registrados.json)
    productos = acceder_a_datos_json(ruta_products_registrados)
    
    #Condicion que verifica si las dos variable de los precio siguen siendo 0
    if precio_desde == 0 and precio_hasta == 0:
        
        #Bucle que itera sobre la variable que almacena los datos de los productos
        for clave, valor in productos.items():
            
            #Verifica si la clave esta en la la variable nombre
            if clave in nombre:
                #muestra los datos que tengan esa misma clave(en este caso el nombre del producto)
                print(f"{clave} | Precio: {valor['Precio']} | Stock: {valor['Stock']}")
                
                #Actualiza el valor de la variable a True
                filtro_encontrado = True
        #Condicional si la variable no es verdadera
        if not filtro_encontrado:
            
            #Aviso de que no se encontrarion coincidencias con ese nombre
            print("No se encontraron coincidencias")
            
            #Se actualiza con el valor por defecto
            filtro_encontrado = None
            
    #condicional para cuando el principal no se cumpla
    else:
        
        #Bucle que itera sobre la variable que almacena los datos de los productos
        for clave, valor in productos.items():
            
            #Condicional que filtra los datos por un rango de precio
            if (valor['Precio'] >= precio_desde) and (valor['Precio'] <= precio_hasta):
                
                #Muestra los datos que cumplan la condicion
                print(f"{clave} | Precio: {valor['Precio']} | Stock: {valor['Stock']}")
                
                #Se le asigna True a la variable 
                filtro_encontrado = True
                
        #Condicional si la variable no es verdadera
        if not filtro_encontrado:

            #Aviso de que no se encontrarion coincidencias con ese nombre
            print("No se encontraron coincidencias")
            filtro_encontrado = None
        

#Funcion para ordenar los productos ya sea por precio o por nombre (1 para Precio ó 2 para Nombre)
def ordenar_producto(tipo_orden):
    
    try:
        #Accede a los datos de los productos registrados
        productos = acceder_a_datos_json(ruta_products_registrados)
        
        print("Los datos se ordenaron por", "Precio" if tipo_orden == 1 else "Nombre" )
        
        #tipo_orden == 1 significa ordenar por precio
        if tipo_orden == 1:
            #Ordena el diccionario de productos con sorted y una funcion lambda que ordena los datos por precio
            ordenados_precio = dict(sorted(productos.items(), key = lambda item: item[1]["Precio"]))
            
            #Accede a las claves y los valores del diccionario ordenado por precio
            for clave, valor in ordenados_precio.items():
                #Imprime cada uno de los valores 
                print(f"{clave} | Precio: {valor['Precio']} | Stock: {valor['Stock']}")
                
        #tipo_orden == 1 significa ordenar por nombre
        elif tipo_orden == 2:
            
            #Ordena el diccionario de productos con sorted y una funcion lambda que ordena los datos por precio
            ordenados_nombre = dict(sorted(productos.items(), key = lambda item: item[0]))
            
            #Accede a las claves y los valores del diccionario ordenado por precio
            for clave, valor in ordenados_nombre.items():
                
                #Imprime cada uno de los valores
                print(f"{clave} | Precio: {valor['Precio']} | Stock: {valor['Stock']}")
        #Si el valor de la variable es mayor a dos entonces genera una excepción informando que no se puede ordenar por ese valor
        elif tipo_orden > 2:
            raise print("No se puede ordenar por el valor ingresado")
    #Excepción para tipo de datos incorrecto
    except TypeError:
        print("¡Ingrese un número entero por favor!")
    
    finally:
        print("Los datos ya fueron organizados")
        
        
if __name__ == "__main__":
    """productos = {}
    agregar_productos(productos, "Pimenton", 200, 5)

    agregar_productos("Azucar", 800, 5)
    agregar_productos( "Leche", 3000, 5)
    agregar_productos("Arroz", 1300, 10,0)




    ordenar_producto(productos, [2, 3, 4])"""
    buscar_nombre_precio(0,3000)

    #ordenar_producto(1)
    #print(agregar_productos("Aji", 200, 5))
