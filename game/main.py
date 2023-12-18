import tkinter as tk
from src.Mapa.Mapa import MapaSingleton
import sys


class MinesweeperApp:
    def __init__(self, master, rows, columns, bombs):
        self.master = master
        self.master.title("💥 B U S C A M I N A S  III 💥")

        self.mapa = MapaSingleton()
        self.mapa.create(rows, columns, bombs)

        self.create_widgets()

    def create_widgets(self):
        for row in range(self.mapa.rows):
            for col in range(self.mapa.columns):
                button = tk.Button(self.master, text="", width=3, height=3)
                button.grid(row=row, column=col, sticky="nsew")
                button.bind("<Button-1>", lambda event, r=row, c=col: self.cell_clicked(r, c))
                button.bind("<Button-3>", lambda event, r=row, c=col: self.cell_right_clicked(r, c))

    def cell_clicked(self, row, col):
        accion = MapaSingleton.ACCION_REVELAR
        self.realizar_accion(accion, row, col)

    def cell_right_clicked(self, row, col):
        accion = MapaSingleton.ACCION_MARCAR
        self.realizar_accion(accion, row, col)

    def realizar_accion(self, accion, row, col):
        if self.mapa.realizarAccion(accion, row, col) == False:
            self.show_game_over_message("Perdiste")
            self.master.quit()
        elif self.mapa.getRevealedNumber() == self.mapa.rows * self.mapa.columns - len(self.mapa._MapaSingleton__firstCellPtr.bombPositions):
            self.show_game_over_message("Ganaste")
            self.master.quit()
        else:
            self.update_ui()

    def update_ui(self):
        for row in range(self.mapa.rows):
            for col in range(self.mapa.columns):
                celda = self.mapa.__at(row, col)
                text = celda.show() if celda.state == MapaSingleton.ACCION_REVELAR else ""
                self.master.grid_slaves(row=row, column=col)[0].config(text=text)

    def show_game_over_message(self, message):
        popup = tk.Toplevel(self.master)
        popup.title("Resultado")
        label = tk.Label(popup, text=message)
        label.pack()
        button = tk.Button(popup, text="Cerrar", command=popup.destroy)
        button.pack()

    def handle_window_close(self):
        # Manejar cierre de la ventana principal
        # Puedes agregar lógica adicional aquí si es necesario
        self.master.destroy()
    
    def cell_clicked(self, row, col):
        print(f"Celda clickeada: {row}, {col}")
        accion = MapaSingleton.ACCION_REVELAR
        self.realizar_accion(accion, row, col)


def main():
    root = tk.Tk()

    # Leer los argumentos
    if len(sys.argv) != 4:
        print("La llamada al programa es $ ./main.py <rows> <columns> <bombs>")
        return 1

    # Crear la aplicación
    try:
        rows, columns, bombs = map(int, sys.argv[1:])
        minesweeper_app = MinesweeperApp(root, rows, columns, bombs)
    except ValueError as e:
        print("Entrada invalida")
        print(e)
        return

    # Configurar el manejo de cierre de ventana
    root.protocol("WM_DELETE_WINDOW", minesweeper_app.handle_window_close)

    root.mainloop()


if __name__ == "__main__":
    main()
