from datos.carga_de_datos import inicializar_matriz,crear_lista,cargar_datos
from datos.mostrar_los_datos import buscar_legajo,buscar_legajos
from utilidades.impresiones.imprimir_datos import imprimir_estudiantes_sin_promedio,imprimir_estudiante_sin_promedio
from utilidades.mayor_promedio_materias import mostrar_materias_mayor_promedio,mostrar_una_materia_mayor_promedio
from utilidades.calcular_materias import ver_promedios_de_estudiantes,calcular_calificaciones_repetidas
from utilidades.ordenar_estudiantes import mostrar_datos_ordenados
from utilidades.menu import menu

# calificaciones = inicializar_matriz(3, 5, 0)
# nombres = crear_lista(3, "")
# generos = crear_lista(3, "")
# legajos = crear_lista(3, 0)

################### HC

nombres = ["Lucia", "Bruno", "fransiscooooooo"]
generos = ["F", "M", "X"]
legajos = [12345, 12345, 34567]
promedios = [0] * 3
calificaciones = [
    [5, 5, 10, 10, 1],   
    [1, 6, 9, 9, 7],    
    [5, 3, 6, 6, 7]  
]

################### HC

# datos_cargados = False
datos_cargados = True
promedios = None
mensaje_error = "\nError: Primero debe cargar los datos. Seleccione la opcion 1 para ingresar todos los datos de los estudiantes. \ningrese 3 para calcular promedio (Luego de haber ingresado los datos de la orpcion 1)."

while True:
    opcion = menu("\nMENU PRINCIPAL\n1 - Cargar datos de estudiantes.\n2 - Mostrar todos los datos.\n3 - Ver promedios de estudiantes.\n4 - Mostrar datos ordenados por promedio del estudiante.\n5 - Mostrar materia/s con mayor promedio.\n6 - Buscar estudiante por legajo.\n7 - Mostrar calificaciones repetidas en una asignatura.\n8 - Salir del programa.")

    match opcion:
        case 1:
            cargar_datos(nombres, generos, legajos, calificaciones)
            datos_cargados = True
        case 2:
            if datos_cargados:
                imprimir_estudiantes_sin_promedio(nombres, generos, legajos, calificaciones)
            else:
                print(mensaje_error)
        case 3:
            if datos_cargados:
                promedios = ver_promedios_de_estudiantes(calificaciones)
            else:
                print(mensaje_error)
        case 4:
            if datos_cargados and promedios != None:
                mostrar_datos_ordenados(nombres, generos, legajos, promedios, calificaciones, orden = 2)
            else:
                print(mensaje_error)
        case 5:
            if datos_cargados:
                mostrar_materias_mayor_promedio(calificaciones)
            else:
                print(mensaje_error)
        case 6:
            if datos_cargados and promedios != None:
                buscar_legajo(nombres, generos, legajos, promedios, calificaciones)
            else:
                print(mensaje_error)
        case 7:
            if datos_cargados:
                calcular_calificaciones_repetidas(calificaciones,5)
            else:
                print(mensaje_error)
        case 8:
            print("Saliendo del programa...")
            break
        case _:
            print("Opcion invalida. Intente nuevamente.")