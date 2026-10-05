# Gestor de Tareas (Python + PIP)

Proyecto simple de gestión de tareas utilizado para el TP
**"Administradores de Paquetes y GitHub Actions"**.

## 1. Administrador de paquetes elegido: PIP

| Pregunta | Respuesta |
| --- | --- |
| ¿Para qué sirve? | Instalar, actualizar y desinstalar paquetes de Python, y resolver sus dependencias. |
| ¿En qué lenguaje/ecosistema se utiliza? | Python (funciona en Windows, Linux y macOS). |
| ¿De dónde obtiene los paquetes? | De [PyPI](https://pypi.org/) (Python Package Index), el repositorio oficial de la comunidad Python. |

### Paquetes instalados

- **pydantic** → valida y modela los datos de cada tarea.
- **colorama** → colorea la salida por consola.
- **requests** → cliente HTTP (dependencia declarada en el proyecto).
- **pytest** → framework de pruebas automáticas.

### Comandos utilizados

```bash
# Crear entorno virtual
python -m venv .venv

# Activar el entorno virtual (Windows)
.venv\Scripts\activate

# Instalar las dependencias declaradas en requirements.txt
pip install -r requirements.txt

# Instalar un paquete puntual
pip install pydantic==2.13.5

# Listar paquetes instalados
pip list
```

El archivo que registra las dependencias del proyecto es **`requirements.txt`**.

## 2. Cómo ejecutar el proyecto

```bash
python src/main.py
```

## 3. Cómo ejecutar las pruebas

```bash
pytest -v
```

Salida esperada:

```
tests/test_main.py::test_agregar_tarea PASSED
tests/test_main.py::test_multiples_tareas PASSED
========================= 2 passed in 0.19s =========================
```

## 4. GitHub Actions

El pipeline está en [`.github/workflows/ci.yml`](.github/workflows/ci.yml) y se
ejecuta automáticamente en cada **push** al repositorio. Pasos:

1. Descargar el código del repositorio (`actions/checkout`).
2. Preparar el entorno: instalar Python 3.14 (`actions/setup-python`).
3. Instalar las dependencias (`pip install -r requirements.txt`).
4. Ejecutar las pruebas automáticas (`pytest -v`).
5. Finalizar en verde si todo pasó, o en rojo si alguna prueba falló.

Estado del pipeline:

![CI](https://github.com/ginterthiago/Python-y-requirements/actions/workflows/ci.yml/badge.svg)

## 5. Estructura del proyecto

```
.
├── .github/workflows/ci.yml   # Pipeline de GitHub Actions
├── src/main.py                # Código fuente
├── tests/test_main.py         # Pruebas automáticas (pytest)
├── requirements.txt           # Dependencias (PIP)
└── README.md
```
