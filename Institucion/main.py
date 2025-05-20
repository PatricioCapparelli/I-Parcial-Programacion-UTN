from datos.carga_de_datos import inicializar_matriz, cargar_datos, crear_lista
from datos.mostrar_los_datos import imprimir_datos, encontrar_legajos
from utilidades.calcular_promedio import ver_promedios_de_estudiantes
from utilidades.ordenar_estudiantes import mostrar_datos_ordenados
from utilidades.mayor_promedio_materias import mostrar_materias_mayor_promedio

calificaciones = inicializar_matriz(3, 5, 0)
nombres = crear_lista(3, "")
generos = crear_lista(3, "")
legajos = crear_lista(3, 0)

################### HC

# nombres = [''] * 3
# generos = [''] * 3
# legajos = [0] * 3
# promedios = [0] * 3

# nombres = ["Ana", "Bruno", "Carlaaaaaaa"]
# generos = ["F", "M", "F"]
# legajos = [12345, 12345, 34567]
# calificaciones = [
#     [10, 10, 10, 10, 9],   
#     [10, 10, 8, 9, 10],    
#     [10, 10, 10, 10, 10]  
# ]

################### HC

# datos_cargados = False
datos_cargados = True
promedios = None
mensaje_error = "\nError: Primero debe cargar los datos. Seleccione la opcion 1 para ingresar todos los datos de los estudiantes. \ningrese 3 para calcular promedio (Luego de haber ingresado los datos de la orpcion 1)."

while True:
    print("\nMENU PRINCIPAL")
    print("1 - Cargar datos de estudiantes.")
    print("2 - Mostrar todos los datos.")
    print("3 - Ver promedios de estudiantes.")
    print("4 - Mostrar datos ordenados por promedio del estudiante.")
    print("5 - Mostrar materia/s con mayor promedio.")
    print("6 - Buscar estudiante por legajo.")
    print("7 - Salir")
    opcion = input("Seleccione opcion: ")

    match opcion:
        case '1':
            cargar_datos(nombres, generos, legajos, calificaciones)
            datos_cargados = True
        case '2':
            if datos_cargados:
                imprimir_datos(nombres, generos, legajos, calificaciones)
            else:
                print(mensaje_error)
        case '3':
            if datos_cargados:
                promedios = ver_promedios_de_estudiantes(calificaciones)
            else:
                print(mensaje_error)
        case '4':
            if datos_cargados and promedios != None:
                mostrar_datos_ordenados(nombres, generos, legajos, promedios, calificaciones, orden=2)
            else:
                print(mensaje_error)
        case '5':
            if datos_cargados:
                mostrar_materias_mayor_promedio(calificaciones)
            else:
                print(mensaje_error)
        case '6':
            if datos_cargados and promedios != None:
                encontrar_legajos(nombres, generos, legajos, promedios, calificaciones)
            else:
                print(mensaje_error)

        case '7':
            print("Saliendo del programa...")
            break

        case _:
            print("Opcion invalida. Intente nuevamente.")