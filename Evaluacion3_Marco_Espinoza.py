import csv # se importa la librería csv
continuar = True # se define la variable continuar
def menu (): # se define la función menu
    print("Bienvenido al Sistema de Gestión de Inventario")
    print("")
    print("Seleccione una opción: ") # se agrega un mensaje para seleccionar una opción
    print("1. Agregar producto al inventario") # se agrega la opción de agregar un producto
    print("2. Leer el inventario") # se agrega la opción de leer el inventario
    print("3. Clasificar productos y generar archivo de texto") # se agrega la opción de clasificar productos
    print("4. Salir") # se agrega la opción de salir
    global opcion # se define la variable global opcion
    
    # se agrega un ciclo while para validar la opción ingresada
    while True:
        try:
            opcion = int(input("Ingrese la opción [1 a 4]: "))
            if opcion >= 1 or opcion <= 4:
                break
        except ValueError:
            print("Opción inválida. Intente de nuevo.")

# se define la función agregar_producto   
def agregar_producto():
    print("")
    print("Agregar producto")
    print("")
    global nombre
    global id
    global categoria
    global precio
    nombre = input("Ingrese el nombre del producto: ") # se solicita el nombre del producto
    id = input("Ingrese el id del producto: ") # se solicita el id del producto
    categoria = input("Ingrese la categoria del producto [Electronica, Textil y Calzado]: ") # se solicita la categoría del producto
    precio = float(input("Ingrese el precio del producto: ")) # se solicita el precio del producto
    
    # Proceso de creado del csv y agregar los productos en el inventario
    with open("inventario.csv", "a", newline="") as inventario:# se crea un archivo csv llamado inventario
        escritor_beca = csv.writer(inventario) # se crea un objeto writer
        escritor_beca.writerow([nombre, id, categoria, precio]) # se escribe la primera fila del archivo
    print("Producto agregado exitosamente")
    print("")

def leer_invetario(): # se define la función leer_inventario
    print("")
    print("Leer inventario")
    print("")
    # se abre el archivo csv en modo lectura
    with open("inventario.csv", "r") as inventario:
        lector = csv.reader(inventario)
        for linea in lector:
            print(linea) # se imprime la línea
    print("")
    
def clasificar_productos(): # se define la función clasificar_productos
    print("")
    print("Clasificar productos")
    print("")
    # se abre el archivo csv en modo lectura
    with open("inventario.csv", "r") as inventario:
        lector = csv.reader(inventario)
        # se crean listas vacías para cada categoría
        electronica = []
        textil = []
        calzado = []
        for linea in lector:
            if linea[2] == "Electronica": # si la categoría es Electrónica
                electronica.append(linea) # se agrega a la lista de electrónica
            elif linea[2] == "Textil": # si la categoría es Textil
                textil.append(linea) # se agrega a la lista de textil
            elif linea[2] == "Calzado": # si la categoría es Calzado
                calzado.append(linea) # se agrega a la lista de calzado
    # se crea un archivo de texto para cada categoría
    with open("clasificacion_productos.txt", "w") as archivo:
        archivo.write("Productos de Electrónica: \n")
        for producto in electronica:
            archivo.write(str(producto) + "\n")
        archivo.write("\n")
        archivo.write("Productos de Textil: \n")
        for producto in textil:
            archivo.write(str(producto) + "\n")
        archivo.write("\n")
        archivo.write("Productos de Calzado: \n")
        for producto in calzado:
            archivo.write(str(producto) + "\n")
    print("Archivos de texto generados exitosamente")
    print("")
    
def salir(): # se define la función salir
    global continuar
    print("Gracias por utilizar el Sistema de Gestión de Inventario")
    print("¡Hasta luego!")
    continuar = False # se cambia la variable continuar a False
    
    
    
# se crea un ciclo while para que el menú se muestre continuamente
while continuar == True:
    menu() # se llama a la función menu
    if opcion == 1:
        agregar_producto() # se llama a la función agregar_producto
    elif opcion == 2:
        leer_invetario() # se llama a la función leer_inventario
    elif opcion == 3:
        clasificar_productos() # se llama a la función clasificar_productos
    elif opcion == 4:
        salir() # se llama a la función salir

        


