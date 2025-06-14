from datos.carga_de_datos import inicializar_matriz,crear_lista,cargar_datos
from datos.mostrar_los_datos import buscar_legajo,buscar_legajos
from utilidades.impresiones.imprimir_datos import imprimir_estudiantes_sin_promedio,imprimir_estudiante_sin_promedio
from utilidades.mayor_promedio_materias import mostrar_materias_mayor_promedio,mostrar_una_materia_mayor_promedio
from utilidades.calcular_materias import ver_promedios_de_estudiantes,calcular_calificaciones_repetidas
from utilidades.ordenar_estudiantes import mostrar_datos_ordenados
from utilidades.menu import menu

# calificaciones = inicializar_matriz(30, 5, 0)
# nombres = crear_lista(30, "")
# generos = crear_lista(30, "")
# legajos = crear_lista(30, 0)

################## HC

nombres = ["Lucia", "Bruno", "fransisco","franco","Pedro",
        "Jose", "Chavela", "Joaquin","Franchezca","Dilan",
        "Mauro", "Isaias", "Antonio","Elena","Rocio",
        "Jeremias", "Federico", "Zoe","Daniela","Daniel",
        "Augusto", "Maximo", "Isabela","Julia","Ramiro",
        "Ezequiel", "Sofia", "Clara","Bautista","Denise",]

generos = ["M", "F", "X", "X", "F", "M", "M", "X", "F", "F",
        "X", "M", "F", "X", "M", "F", "M", "X", "X", "F",
        "M", "X", "F", "M", "X", "F", "M", "X", "F", "M"]

legajos = [10001, 10002, 10003, 10004, 10005, 10006, 10007, 10008, 10009, 10010,
        10011, 10012, 10013, 10014, 10015, 10016, 10017, 10018, 10019, 10020,
        10021, 10022, 10023, 10024, 10025, 10026, 10027, 10028, 10029, 10030]

promedios = [7.3, 4.8, 6.1, 9.2, 5.5, 8.7, 3.4, 6.9, 7.0, 4.2,
            5.8, 6.5, 2.9, 8.3, 9.0, 4.7, 7.6, 3.8, 6.0, 5.1,
            8.0, 7.9, 4.4, 6.7, 5.9, 3.6, 7.2, 6.3, 8.1, 4.6]

calificaciones = [
    [7, 8, 10, 9, 6],
    [4, 6, 9, 7, 7],
    [5, 3, 6, 8, 7],
    [6, 4, 7, 5, 9],
    [8, 6, 6, 7, 4],
    [7, 5, 8, 6, 5],
    [5, 7, 9, 6, 8],
    [6, 8, 7, 5, 6],
    [4, 6, 6, 7, 9],
    [9, 5, 7, 8, 6],
    [6, 7, 6, 6, 7],
    [5, 6, 5, 7, 6],
    [8, 5, 7, 5, 7],
    [7, 6, 6, 8, 5],
    [6, 5, 5, 6, 8],
    [5, 5, 6, 7, 6],
    [7, 6, 7, 5, 6],
    [6, 6, 6, 6, 6],
    [8, 7, 5, 7, 6],
    [7, 6, 8, 5, 7],
    [6, 5, 7, 6, 7],
    [7, 5, 6, 7, 6],
    [5, 6, 7, 6, 6],
    [6, 7, 5, 7, 6],
    [5, 6, 6, 6, 7],
    [6, 5, 6, 7, 6],
    [7, 6, 5, 6, 7],
    [6, 6, 7, 5, 6],
    [5, 7, 6, 6, 6],
    [6, 6, 6, 6, 6]
]


datos_cargados = True
################## HC

# datos_cargados = False
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