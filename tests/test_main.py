import sys
import os

# Asegurar que el directorio src esté en el path de importación
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src"))
)

from main import GestorTareas


def test_agregar_tarea():
  gestor = GestorTareas()
  gestor.agregar_tarea("Prueba unitaria", "Descripción de prueba")

  assert len(gestor.tareas) == 1
  assert gestor.tareas[0].titulo == "Prueba unitaria"
  assert gestor.tareas[0].completada is False


def test_multiples_tareas():
  gestor = GestorTareas()
  gestor.agregar_tarea("Tarea 1")
  gestor.agregar_tarea("Tarea 2")

  assert len(gestor.tareas) == 2
  assert gestor.tareas[0].id == 1
  assert gestor.tareas[1].id == 2