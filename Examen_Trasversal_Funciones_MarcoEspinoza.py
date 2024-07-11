import random # se importa la librería random
import csv # se importa la librería csv


def menu (): # se define la función menu
    print("Bienvenido al Sistema de Analisis de Datos")
    print("")
    print("Seleccione una opción: ") # se agrega un mensaje para seleccionar una opción
    print("1. Asignar sueldo aleatorio") # se agrega la opción de agregar sueldo aleatorio
    print("2. Clasificar sueldos") # se agrega la opción de clasificar sueldos
    print("3. Ver estadisticas") # se agrega la opción de ver estadisticas
    print("4. Reporte de sueldos") # se agrega la opción de reporte de sueldos
    print("5. Salir del programa") # se agrega la opción de salir del programa
    
def validacion (a):
        try:
            if a >= 1 and a <= 5 and a != 0:
                return True
            else:
                print("")
                return False 
        except ValueError:
            print("Opción inválida. Intente de nuevo.")
            
# se define la función asignar_sueldo_aleatorio           
def asignar_sueldo_aleatorio():
    print("")
    print("Asignar sueldo aleatorio")
    print("")
    global trabajadores_diccionario # se define la variable trabajadores_diccionario
    # se define una lista de trabajadores
    trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"] 
    # se define un diccionario basado en la lista de trabajadores
    trabajadores_diccionario = {trabajador: 0 for trabajador in trabajadores}
    for i in trabajadores_diccionario: # Recorrido de diccionario
        sueldo = random.randint(300000, 2500000) # Asignación de sueldo aleatorio
        trabajadores_diccionario[i] = sueldo # Asignación de sueldo a trabajador
    print("Sueldos asignados exitosamente")
    print("")
    

# se define la función clasificar_sueldos       
def clasificar_sueldos():
    print("")
    print("Clasificar sueldos")
    print("")
    global total_sueldos, menos_800000, entre_800000_2000000, mas_2000000
    # se definen las variables cantidad_de_sueldos, total_sueldos, menos_800000, entre_800000_2000000, mas_2000000
    
    # Sueldos menores a 800.000
    menos_800000 = []  # Creación de lista vacía
    for nombre, sueldo in trabajadores_diccionario.items(): # Recorrido de diccionario
        if sueldo < 800000: # Condición de sueldo menor a 800.000
            menos_800000.append((nombre, sueldo)) # Agregar a lista
    print("Sueldos menores a $800.000: ") # Impresión de sueldos menores a 800.000
    print(f"Total: {len(menos_800000)} personas") # Impresión de total de personas
    print("")
    for nombre, sueldo in menos_800000: # Recorrido de lista
        print(f"{nombre}: ${sueldo}")   # Impresión de nombre y sueldo
    print("")
    
    # Sueldos entre 800.000 y 2.000.000
    entre_800000_2000000 = [] # Creación de lista vacía
    for nombre, sueldo in trabajadores_diccionario.items(): # Recorrido de diccionario
        if sueldo >= 800000 and sueldo <= 2000000: # Condición de sueldo entre 800.000 y 2.000.000
            entre_800000_2000000.append((nombre, sueldo)) # Agregar a lista
    print("Sueldos entre $800.000 y $2.000.000: ") # Impresión de sueldos entre 800.000 y 2.000.000
    print(f"Total: {len(entre_800000_2000000)} personas") # Impresión de total de personas
    print("")
    for nombre, sueldo in entre_800000_2000000: # Recorrido de lista
        print(f"{nombre}: ${sueldo}") # Impresión de nombre y sueldo
    print("")
    
    # Sueldos mayores a 2.000.000
    mas_2000000 = [] # Creación de lista vacía
    for nombre, sueldo in trabajadores_diccionario.items(): # Recorrido de diccionario
        if sueldo > 2000000: # Condición de sueldo mayor a 2.000.000
            mas_2000000.append((nombre, sueldo)) # Agregar a lista
    print("Sueldos mayores a $2.000.000: ") # Impresión de sueldos mayores a 2.000.000
    print(f"Total: {len(mas_2000000)} personas") # Impresión de total de personas
    print("")
    for nombre, sueldo in mas_2000000: # Recorrido de lista
        print(f"{nombre}: ${sueldo}") # Impresión de nombre y sueldo
    print("")
    
    # Total de sueldos
    total_sueldos = 0
    for nombre, sueldo in trabajadores_diccionario.items(): # Recorrido de diccionario
        total_sueldos += sueldo # Asignación de total de sueldos
    print(f"Total de sueldos: ${total_sueldos}")
    

# se define la función ver_estadisticas  
def ver_estadisticas():
    print("")
    print("Ver estadisticas")
    print("")
    print("Estadísticas de sueldos: ")
    global mas_alto, mas_bajo
    mas_alto = max(trabajadores_diccionario.values()) # Definición de sueldo más alto
    mas_bajo = min(trabajadores_diccionario.values()) # Definición de sueldo más bajo
    print("El sueldo mas alto es de: $", mas_alto) # Impresión de sueldo más alto
    print("El sueldo mas bajo es de: $",mas_bajo)  # Impresión de sueldo más bajo
    print("El promedio de sueldos es de: $",total_sueldos/10) # Impresión de promedio de sueldos
    
# se define la función reporte_sueldos   
def reporte_sueldos():
    print("")
    print("Reporte de sueldos")
    print("")
    print("Reporte de sueldos: ")
    
    # Creación de archivo csv
    with open("Reporte_sueldos.csv", "w", newline="") as reporte_sueldos: # Creación de archivo csv
        escritor_reporte = csv.writer(reporte_sueldos) # Creación de objeto writer
        escritor_reporte.writerow(["Nombre", "Sueldo Bruto", "Descuento Salud", "Descuento AFP", "Sueldo Líquido"]) # Escritura de fila en archivo
    
        for nombre, sueldo in trabajadores_diccionario.items(): # Recorrido de diccionario
            descuento_salud = sueldo * 0.07 # Cálculo de descuento de salud
            descuento_salud = round(descuento_salud, 2) # Redondeo de descuento de salud
            descuento_AFP = sueldo * 0.12 # Cálculo de descuento de AFP
            descuento_AFP = round(descuento_AFP, 2) # Redondeo de descuento de AFP
            sueldo_liquido = sueldo - descuento_salud - descuento_AFP # Cálculo de sueldo líquido
            escritor_reporte.writerow([nombre, sueldo, descuento_salud, descuento_AFP, sueldo_liquido]) # Escritura de fila en archivo   
    print("Reporte de sueldos creado exitosamente")
    print("")               


# se define la función salir_del_programa        
def salir_del_programa():
    print("")
    print("Saliendo del programa...")
    print("")
    print("Gracias por utilizar el Sistema de Analisis de Datos")
    print("")
    print("Desarrollado por Marco Espinoza")
    print("Rut: 21.507.158-8")

    

