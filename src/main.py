import sys

from colorama import Fore, Style, init
from pydantic import BaseModel, Field

# Consolas Windows (cp1252) no pueden imprimir caracteres especiales
if hasattr(sys.stdout, "reconfigure"):
  sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# Inicializar colorama para la consola
init(autoreset=True)


class Tarea(BaseModel):
  id: int
  titulo: str
  descripcion: str = Field(default="")
  completada: bool = False


class GestorTareas:

  def __init__(self):
    self.tareas = []
    self._contador_id = 1

  def agregar_tarea(self, titulo: str, descripcion: str = ""):
    nueva_tarea = Tarea(
        id=self._contador_id, titulo=titulo, descripcion=descripcion
    )
    self.tareas.append(nueva_tarea)
    self._contador_id += 1
    print(
        f"{Fore.GREEN}✔ Tarea '{titulo}' agregada con éxito.{Style.RESET_ALL}"
    )

  def listar_tareas(self):
    if not self.tareas:
      print(f"{Fore.YELLOW}No hay tareas registradas.{Style.RESET_ALL}")
      return

    print(f"\n{Fore.CYAN}=== LISTA DE TAREAS ==={Style.RESET_ALL}")
    for t in self.tareas:
      estado = (
          f"{Fore.GREEN}[Completada]{Style.RESET_ALL}"
          if t.completada
          else f"{Fore.RED}[Pendiente]{Style.RESET_ALL}"
      )
      print(f"ID: {t.id} | {t.titulo} {estado}")
      if t.descripcion:
        print(f"   Descripción: {t.descripcion}")


if __name__ == "__main__":
  gestor = GestorTareas()
  gestor.agregar_tarea(
      "Aprender Python", "Estudiar estructuras de datos y POO."
  )
  gestor.agregar_tarea("Hacer compras", "Comprar leche, café y pan.")
  gestor.listar_tareas()