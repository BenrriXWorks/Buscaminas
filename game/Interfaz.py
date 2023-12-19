import tkinter as tk
from Timer import Timer
from src.Mapa.Mapa import MapaSingleton
from src.StateHandler.StateHandler import StateHandlerSingleton

class Interfaz:
    def __init__(self, root):
        self.root = root
        self.root.title("Buscaminas :)")

        self.dimensiones = (40, 40)

        # Configuración cronómetro
        self.cronometro_label = tk.Label(root, text="Tiempo: 0")
        self.cronometro_label.grid(row=0, column=0, sticky="e")

        # Área para el mapa
        self.porcentaje_tablero = 0.6  # Porcentaje del tamaño de la ventana
        self.tablero_frame = tk.Frame(root, bg="red")
        self.tablero_frame.grid(row=1, column=0, rowspan=self.dimensiones[1], columnspan=self.dimensiones[0], sticky="nsew")

        # Crear el mapa y empaquetarlo en el área del tablero
        self.mapa_singleton = MapaSingleton()
        self.mapa_singleton.create(self.tablero_frame, 10, 10, 10)  # Ajusta los parámetros según sea necesario
        self.mapa_singleton.pack(fill=tk.BOTH, expand=True)

        # Crear la instancia del manejador de estados
        self.state_handler = StateHandlerSingleton()
        self.state_handler.set_interface(self)

        # Crear instancia de la clase Timer
        self.timer = Timer(self.actualizar_cronometro)
        self.timer.root = self.root  # Pasar la referencia de la ventana a la instancia del temporizador

        # Dimensiones iniciales de la ventana
        self.inicializar_dimensiones()

    def inicializar_dimensiones(self):
        # Dimensiones iniciales de la ventana
        self.ancho_inicial = 800  # Establecer el ancho inicial deseado
        self.alto_inicial = 800  # Establecer el alto inicial deseado

        # Tamaño del cuadrado del estado del juego (ajustado para que sea cuadrado)
        self.porcentaje_estado = 0.1  # Ajusta el valor según sea necesario
        self.lado_estado = int(min(self.ancho_inicial, self.alto_inicial) * self.porcentaje_estado)

        # Crear el cuadrado del estado
        self.estado_frame = tk.Frame(self.root, bg="blue", bd=0, width=self.lado_estado, height=self.lado_estado)
        self.estado_frame.grid(row=0, column=0, sticky="n", padx=10, pady=10)  # Ajusta el espacio entre el cuadrado del estado y el cronómetro

        # ... (código existente)

        # Establecer el tamaño de la ventana
        self.root.geometry(f"{self.ancho_inicial}x{self.alto_inicial}")

        # Establecer el tamaño máximo y mínimo de la ventana igual al tamaño inicial
        self.root.maxsize(self.ancho_inicial, self.alto_inicial)
        self.root.minsize(self.ancho_inicial, self.alto_inicial)

        # Hacer que la ventana no sea redimensionable
        self.root.resizable(width=False, height=False)

    def actualizar_cronometro(self, elapsed_time):
        self.cronometro_label.config(text=f"Tiempo: {elapsed_time}")

    def inicializar_interfaz(self, rows, columns, bombs):
        # Aquí puedes usar rows, columns, y bombs según sea necesario
        # por ejemplo, podrías ajustar el tamaño del mapa o configurar el manejador de estados

        # Configurar el manejador de estados
        self.state_handler.setMapAttributes(rows, columns, bombs)

        # Otras configuraciones según sea necesario

        # Llamar a iniciar_cronometro después de ajustar el tamaño del área del tablero y el cuadrado del estado
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        self.root.grid_rowconfigure(0, weight=0)  # Peso 0 para evitar que el cuadrado del estado afecte la posición del cronómetro

        # Iniciar el temporizador después de que la ventana principal se haya iniciado
        self.timer.start()

        # Iniciar el bucle principal de la interfaz
        self.root.mainloop()
    
    def update_interface(self):
        # Lógica para obtener la ruta de la imagen del manejador de estados
        image_path = self.state_handler.get_image_path()

        # Actualizar la imagen en el cuadrado azul usando un Label
        image = tk.PhotoImage(file=image_path)
        
        # Crear un Label en lugar de un Frame para mostrar la imagen
        image_label = tk.Label(self.root, image=image, bg="blue", bd=0)
        image_label.grid(row=0, column=0, sticky="n", padx=10, pady=10)
        
        # Actualizar la referencia al Label en la interfaz
        self.estado_frame = image_label


