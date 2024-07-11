import random # Importación de librería random
import csv 
from Examen_Trasversal_Funciones_MarcoEspinoza import menu, validacion ,asignar_sueldo_aleatorio, clasificar_sueldos, ver_estadisticas, reporte_sueldos, salir_del_programa


# se crea un ciclo while para que el menú se muestre continuamente
while True:
    menu()
    opcion = int(input("Ingrese una opción: "))
    if validacion(opcion):
        if opcion == 1:
            asignar_sueldo_aleatorio()
        if opcion == 2:
            clasificar_sueldos()
        if opcion == 3:
            ver_estadisticas()
        if opcion == 4:
            reporte_sueldos()
        if opcion == 5:
            salir_del_programa()
            break
        
        