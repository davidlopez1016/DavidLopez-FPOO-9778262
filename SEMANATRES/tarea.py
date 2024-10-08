# definición de la clase Tarea
class Tarea:
    def __init__(self, id, titulo, calificacion, categoria):
        self.id = id
        self.titulo = titulo
        self.calificacion = calificacion
        self.categoria = self.clasificar_categoria(categoria)

    def clasificar_categoria(self, categoria):
        categorias = {1: 'quiz', 2: 'parcial', 3: 'trabajo'}
        return categorias.get(categoria, 'desconocida')

    def __str__(self):
        return f"ID: {self.id}, Título: {self.titulo}, Calificación: {self.calificacion}, Categoría: {self.categoria}"

# función para registrar tareas
def registrar_tareas():
    tareas = []
    while True:
        id = input("Ingrese el ID de la tarea: ")
        titulo = input("Ingrese el título de la tarea: ")
        calificacion = float(input("Ingrese la calificación de la tarea (0 a 5): "))
        categoria = int(input("Ingrese la categoría de la tarea (1: quiz, 2: parcial, 3: trabajo): "))
        
        tarea = Tarea(id, titulo, calificacion, categoria)
        tareas.append(tarea)
        
        continuar = input("¿Desea ingresar otra tarea? (s/n): ")
        if continuar.lower() != 's':
            break

    return tareas

# función para imprimir la lista de tareas
def imprimir_tareas(tareas):
    print("\nLista de Tareas Registradas:")
    for tarea in tareas:
        print(tarea)


if __name__ == "__main__":
    tareas = registrar_tareas()
    imprimir_tareas(tareas)
