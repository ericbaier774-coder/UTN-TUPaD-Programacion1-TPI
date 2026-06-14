#Eric Baier / Trabajo Practico Integrador / Programacion 1
#UTN / 2026

#Desarollo total de las funciones en main.py por decision de la catedra

#Importaciones
import csv
import os

ARCHIVO = "datos.csv"


# --------------------------------------------------
# VALIDACIONES
# --------------------------------------------------

#Normalizacion del texto a comparar
def normalizar_texto(texto):
    """
    Convierte:
    argentina -> Argentina
    AMERICA -> America
    aRgEnTiNa -> Argentina
    """
    return texto.strip().capitalize()

#Que el texto ingresado este correcto
def pedir_texto(mensaje):
    """
    Solicita un texto no vacío.
    """
    while True:
        dato = input(mensaje).strip()

        if dato == "":
            print("\nERROR: No se permiten campos vacíos.")
            print("1 - Reintentar")
            print("2 - Volver al menú")

            opcion = input("Opción: ")

            if opcion == "2":
                return None

        else:
            return normalizar_texto(dato)

#Que el int ingresado este correcto
def pedir_entero_positivo(mensaje):
    """
    Solicita un número entero positivo.
    """
    while True:

        dato = input(mensaje).strip()

        if dato == "":
            print("\nERROR: No se permiten campos vacíos.")
            print("1 - Reintentar")
            print("2 - Volver al menú")

            opcion = input("Opción: ")

            if opcion == "2":
                return None

            continue

        try:

            numero = int(dato)

            if numero <= 0:
                print("\nERROR: Debe ingresar un número mayor que cero.")
                continue

            return numero

        except ValueError:
            print("\nERROR: Debe ingresar un número entero válido.")

#Que el rango de busqueda sea correcto
def pedir_rango(texto):
    
    while True:

        minimo = pedir_entero_positivo(
            f"{texto} mínima: "
        )

        if minimo is None:
            return None, None

        maximo = pedir_entero_positivo(
            f"{texto} máxima: "
        )

        if maximo is None:
            return None, None

        if minimo <= maximo:
            return minimo, maximo

        print(
            f"\nERROR: La {texto.lower()} mínima "
            f"no puede ser mayor que la máxima."
        )

# --------------------------------------------------
# CARGA CSV
# --------------------------------------------------

def cargar_paises():
    """
    Lee el archivo CSV y devuelve una lista de diccionarios.
    """

    paises = []

    if not os.path.exists(ARCHIVO):
        return paises

    try:

        with open(ARCHIVO, "r", encoding="utf-8") as archivo:

            lector = csv.DictReader(archivo)

            for fila in lector:

                try:

                    pais = {
                        "nombre": normalizar_texto(fila["nombre"]),
                        "poblacion": int(fila["poblacion"]),
                        "superficie": int(fila["superficie"]),
                        "continente": normalizar_texto(fila["continente"])
                    }

                    paises.append(pais)

                except (ValueError, KeyError):
                    print(
                        "Advertencia: Se encontró una fila con formato incorrecto y fue ignorada."
                    )

    except FileNotFoundError:
        print("ERROR: No se encontró el archivo.")

    except PermissionError:
        print("ERROR: No hay permisos para leer el archivo.")

    except Exception as error:
        print(f"ERROR inesperado: {error}")

    return paises


# --------------------------------------------------
# GUARDAR CSV
# --------------------------------------------------

def guardar_paises(paises):
    """
    Sobrescribe el archivo CSV.
    """

    try:

        with open(ARCHIVO, "w", newline="", encoding="utf-8") as archivo:

            campos = [
                "nombre",
                "poblacion",
                "superficie",
                "continente"
            ]

            escritor = csv.DictWriter(
                archivo,
                fieldnames=campos
            )

            escritor.writeheader()

            for pais in paises:
                escritor.writerow(pais)

        print("\nDatos guardados correctamente.")

    except PermissionError:
        print("ERROR: No tiene permisos para escribir el archivo.")

    except Exception as error:
        print(f"ERROR inesperado: {error}")

# --------------------------------------------------
# VISUALIZAR CSV
# --------------------------------------------------

def visualizar_csv():
    """
    Muestra el contenido del CSV en formato de tabla.
    """

    paises = cargar_paises()

    if len(paises) == 0:
        print("\nNo hay datos para mostrar.")
        return

    # Encabezado tipo planilla
    print("\n" + "=" * 80)
    print(f"{'NOMBRE':<20}{'POBLACION':<20}{'SUPERFICIE':<20}{'CONTINENTE':<20}")
    print("=" * 80)

    try:
        for pais in paises:
            print(
                f"{pais['nombre']:<20}"
                f"{pais['poblacion']:<20}"
                f"{pais['superficie']:<20}"
                f"{pais['continente']:<20}"
            )

    except KeyError:
        print("\nERROR: El archivo contiene datos con formato inválido.")

    except Exception as error:
        print(f"\nERROR inesperado al mostrar datos: {error}")

    print("=" * 80)

# --------------------------------------------------
# ALTA DE PAISES NUEVOS
# --------------------------------------------------

def alta():
    """
    Agrega un nuevo país al archivo CSV.
    """

    paises = cargar_paises()

    print("\n=== ALTA DE PAÍS ===")

    nombre = pedir_texto("Ingrese nombre del país: ")

    if nombre is None:
        return

    # Verificar si ya existe
    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            print("\nERROR: El país ya existe.")
            return

    poblacion = pedir_entero_positivo(
        "Ingrese población: "
    )

    if poblacion is None:
        return

    superficie = pedir_entero_positivo(
        "Ingrese superficie: "
    )

    if superficie is None:
        return

    continentes_validos = [
        "America",
        "Europa",
        "Asia",
        "Africa",
        "Oceania"
    ]

    while True:

        continente = pedir_texto(
            "Ingrese continente: "
        )

        if continente is None:
            return

        if continente not in continentes_validos:

            print("\nERROR: Continente inválido.")

            print("\nContinentes permitidos:")
            for c in continentes_validos:
                print("-", c)

            print("\n1 - Reintentar")
            print("2 - Volver al menú")

            opcion = input("Opción: ")

            if opcion == "2":
                return

        else:
            break

    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }

    paises.append(nuevo_pais)

    guardar_paises(paises)

    print("\nPaís agregado correctamente.")

# --------------------------------------------------
# MODIFICACION DE PAISES NUEVOS
# --------------------------------------------------

def modificacion():
    """
    Actualiza población y superficie de un país.
    """

    paises = cargar_paises()

    if len(paises) == 0:
        print("\nNo hay países cargados.")
        return

    nombre_buscado = pedir_texto(
        "Ingrese el nombre del país a modificar: "
    )

    if nombre_buscado is None:
        return

    encontrado = False

    for pais in paises:

        if pais["nombre"].lower() == nombre_buscado.lower():

            encontrado = True

            print("\nDatos actuales:")
            print(f"País: {pais['nombre']}")
            print(f"Población: {pais['poblacion']}")
            print(f"Superficie: {pais['superficie']}")

            nueva_poblacion = pedir_entero_positivo(
                "Nueva población: "
            )

            if nueva_poblacion is None:
                return

            nueva_superficie = pedir_entero_positivo(
                "Nueva superficie: "
            )

            if nueva_superficie is None:
                return

            pais["poblacion"] = nueva_poblacion
            pais["superficie"] = nueva_superficie

            guardar_paises(paises)

            print("\nPaís modificado correctamente.")
            break

    if not encontrado:
        print("\nNo se encontró el país.")

# --------------------------------------------------
# BUSQUEDA DE PAISES EN LISTADO
# --------------------------------------------------

def busqueda():
    """
    Busca países por coincidencia parcial o exacta.
    """

    paises = cargar_paises()

    if len(paises) == 0:
        print("\nNo hay países cargados.")
        return

    texto = pedir_texto(
        "Ingrese país a buscar: "
    )

    if texto is None:
        return

    resultados = []

    for pais in paises:

        if texto.lower() in pais["nombre"].lower():
            resultados.append(pais)

    if len(resultados) == 0:
        print("\nNo se encontraron resultados.")
        return

    print("\nRESULTADOS")

    for pais in resultados:

        print("-" * 40)
        print(f"Nombre: {pais['nombre']}")
        print(f"Población: {pais['poblacion']}")
        print(f"Superficie: {pais['superficie']}")
        print(f"Continente: {pais['continente']}")

# --------------------------------------------------
# FILTRO DE BUSQUEDA
# --------------------------------------------------

def filtro():
    """
    Filtra países por continente, población o superficie.
    """

    paises = cargar_paises()

    if len(paises) == 0:
        print("\nNo hay países cargados.")
        return

    print("\nFILTROS")
    print("1 - Continente")
    print("2 - Rango de población")
    print("3 - Rango de superficie")

    opcion = input("Opción: ").strip()

    resultados = []

    # -------------------------
    # FILTRO POR CONTINENTE
    # -------------------------
    if opcion == "1":

        continente = pedir_texto("Ingrese continente: ")

        if continente is None:
            return

        for pais in paises:
            if pais["continente"].lower() == continente.lower():
                resultados.append(pais)

    # -------------------------
    # FILTRO POR POBLACIÓN
    # -------------------------
    elif opcion == "2":

        minimo, maximo = pedir_rango("Población")

        if minimo is None:
            return

        for pais in paises:
            if minimo <= pais["poblacion"] <= maximo:
                resultados.append(pais)

    # -------------------------
    # FILTRO POR SUPERFICIE
    # -------------------------
    elif opcion == "3":

        minimo, maximo = pedir_rango("Superficie")

        if minimo is None:
            return

        for pais in paises:
            if minimo <= pais["superficie"] <= maximo:
                resultados.append(pais)

    else:
        print("\nOpción inválida.")
        return

    # -------------------------
    # RESULTADOS
    # -------------------------
    if len(resultados) == 0:
        print("\nNo hay resultados para el filtro seleccionado.")
        return

    print("\nRESULTADOS")

    for pais in resultados:
        print("-" * 40)
        print(f"Nombre: {pais['nombre']}")
        print(f"Población: {pais['poblacion']}")
        print(f"Superficie: {pais['superficie']}")
        print(f"Continente: {pais['continente']}")

# --------------------------------------------------
# ORDEN DE VISUALIZACION
# --------------------------------------------------

def orden():

    paises = cargar_paises()

    if len(paises) == 0:
        print("\nNo hay países cargados.")
        return

    print("\nORDENAR POR")
    print("1 - Nombre")
    print("2 - Población")
    print("3 - Superficie")

    criterio = input("Opción: ")

    print("\nSENTIDO")
    print("1 - Ascendente")
    print("2 - Descendente")

    sentido = input("Opción: ")

    reverse = sentido == "2"

    if criterio == "1":

        paises_ordenados = sorted(
            paises,
            key=lambda pais: pais["nombre"],
            reverse=reverse
        )

    elif criterio == "2":

        paises_ordenados = sorted(
            paises,
            key=lambda pais: pais["poblacion"],
            reverse=reverse
        )

    elif criterio == "3":

        paises_ordenados = sorted(
            paises,
            key=lambda pais: pais["superficie"],
            reverse=reverse
        )

    else:
        print("\nOpción inválida.")
        return

    for pais in paises_ordenados:

        print("-" * 40)
        print(f"Nombre: {pais['nombre']}")
        print(f"Población: {pais['poblacion']}")
        print(f"Superficie: {pais['superficie']}")
        print(f"Continente: {pais['continente']}")

# --------------------------------------------------
# ESTADISTICAS
# --------------------------------------------------

def estadisticas():

    paises = cargar_paises()

    if len(paises) == 0:
        print("\nNo hay países cargados.")
        return

    mayor_poblacion = max(
        paises,
        key=lambda pais: pais["poblacion"]
    )

    menor_poblacion = min(
        paises,
        key=lambda pais: pais["poblacion"]
    )

    suma_poblacion = 0
    suma_superficie = 0

    continentes = {}

    for pais in paises:

        suma_poblacion += pais["poblacion"]
        suma_superficie += pais["superficie"]

        continente = pais["continente"]

        if continente in continentes:
            continentes[continente] += 1
        else:
            continentes[continente] = 1

    promedio_poblacion = (
        suma_poblacion / len(paises)
    )

    promedio_superficie = (
        suma_superficie / len(paises)
    )

    print("\nESTADÍSTICAS")

    print(
        f"\nMayor población: "
        f"{mayor_poblacion['nombre']} "
        f"({mayor_poblacion['poblacion']})"
    )

    print(
        f"Menor población: "
        f"{menor_poblacion['nombre']} "
        f"({menor_poblacion['poblacion']})"
    )

    print(
        f"\nPromedio de población: "
        f"{promedio_poblacion:.2f}"
    )

    print(
        f"Promedio de superficie: "
        f"{promedio_superficie:.2f}"
    )

    print("\nCantidad de países por continente:")

    for continente, cantidad in continentes.items():

        print(
            f"{continente}: {cantidad}"
        )

# --------------------------------------------------
# MENU
# --------------------------------------------------

def menu():

    while True:

        print("\n" + "═" * 60)
        print("GESTIÓN DE PAÍSES".center(60))
        print("═" * 60)

        print("1 - Visualizacion del listado")
        print("2 - Alta de país")
        print("3 - Modificar país")
        print("4 - Buscar país")
        print("5 - Filtrar países")
        print("6 - Ordenar países")
        print("7 - Estadísticas")
        print("8 - Salir")

        print("═" * 60)

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            visualizar_csv()

        elif opcion == "2":
            alta()

        elif opcion == "3":
            modificacion()

        elif opcion == "4":
            busqueda()

        elif opcion == "5":
            filtro()

        elif opcion == "6":
            orden()

        elif opcion == "7":
            estadisticas()

        elif opcion == "8":
            print("\nPrograma finalizado.")
            break

        else:
            print("\nOpción inválida.")

menu()
