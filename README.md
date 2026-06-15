# Gestión de Países — TPI Programación I

**Universidad Tecnológica Nacional — Tecnicatura Universitaria en Programación**
Materia: Programación I | Año: 2026 | Docente Tutor: Cinthia Rigoni
LINK VIDEO: https://youtu.be/WXtZsZ4dIts

---

## Descripción

Sistema de gestión de datos de países desarrollado en Python como Trabajo Práctico Integrador de la materia Programación I. El programa permite administrar un registro de países almacenado en un archivo CSV, ofreciendo operaciones de alta, modificación, búsqueda, filtrado, ordenamiento y estadísticas a través de un menú interactivo por consola.

Los datos estan en el archivo `datos.csv` ubicado en la raíz del proyecto, que se crea automáticamente al agregar el primer país.

---

## Requisitos

- Python 3.8 o superior
- No requiere librerías externas (solo módulos estándar: `csv`, `os`)

---

## Instrucciones de uso

**1. Clonar el repositorio**
```bash
git clone https://github.com/ericbaier774-coder/UTN-TUPaD-Programacion1-TPI.git
cd UTN-TUPaD-Programacion1-TPI
```

**2. Ejecutar el programa**
```bash
python main.py
```

**3. Navegar el menú**

Al iniciar, se muestra el menú principal. Ingresá el número de la opción deseada y presioná Enter.

════════════════════════════════════════════════════════════

GESTIÓN DE PAÍSES

════════════════════════════════════════════════════════════

1 - Visualizacion del listado

2 - Alta de país

3 - Modificar país

4 - Buscar país

5 - Filtrar países

6 - Ordenar países

7 - Estadísticas

8 - Salir

════════════════════════════════════════════════════════════

Seleccione una opción:

---

## Ejemplos de entradas y salidas

### Alta de un país
=== ALTA DE PAÍS ===

Ingrese nombre del país: argentina

Ingrese población: 45000000

Ingrese superficie: 2780400

Ingrese continente: america
Datos guardados correctamente.

País agregado correctamente.
> El programa normaliza el texto automáticamente: `argentina` se guarda como `Argentina`, `america` como `America`.

---

### Búsqueda por nombre
Ingrese país a buscar: arg
RESULTADOS
Nombre: Argentina

Población: 45000000

Superficie: 2780400

Continente: America
> La búsqueda es parcial: `arg` encuentra `Argentina`.

---

### Filtro por rango de población
FILTROS

1 - Continente

2 - Rango de población

3 - Rango de superficie

Opción: 2

Población mínima: 10000000

Población máxima: 100000000
RESULTADOS
Nombre: Argentina

Población: 45000000

Superficie: 2780400

Continente: America
Nombre: España

Población: 47350000

Superficie: 505990

Continente: Europa

---

### Estadísticas
ESTADÍSTICAS
Mayor población: Brasil (215000000)

Menor población: Uruguay (3500000)
Promedio de población: 62500000.00

Promedio de superficie: 1450000.00
Cantidad de países por continente:

America: 3

Europa: 2

Asia: 1

---

### Validación de entrada incorrecta
Ingrese población: abc

ERROR: Debe ingresar un número entero válido.
Ingrese población: -5

ERROR: Debe ingresar un número mayor que cero.
Ingrese población:

ERROR: No se permiten campos vacíos.

1 - Reintentar

2 - Volver al menú


> **Nota:** El código se desarrolló en un único archivo `main.py` por requerimiento de la cátedra. La arquitectura habitual recomendaría separar el proyecto en módulos (validaciones, persistencia, operaciones, menú).

---

## Funcionalidades

| Opción | Función | Descripción |
|--------|---------|-------------|
| 1 | Visualizar listado | Muestra todos los países en formato de tabla |
| 2 | Alta | Agrega un nuevo país validando todos los campos |
| 3 | Modificar | Actualiza población y superficie de un país existente |
| 4 | Buscar | Búsqueda por nombre (parcial o exacta, sin distinguir mayúsculas) |
| 5 | Filtrar | Filtra por continente, rango de población o rango de superficie |
| 6 | Ordenar | Ordena por nombre, población o superficie en forma ascendente o descendente |
| 7 | Estadísticas | Muestra máximos, mínimos, promedios y conteo por continente |
| 8 | Salir | Cierra el programa |

---

## Integrantes

| Nombre | Rol |
|--------|-----|
| Eric Baier | Desarrollo completo |

---

## Docente Tutor

Cinthia Rigoni — Programación I — UTN TUPaD 2026
