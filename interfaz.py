import tkinter as tk
from tkinter import messagebox

from juego import Juego


class InterfazJuego:

    def __init__(self, ventana):

        self.ventana = ventana
        self.ventana.title("Tres en Raya - TDD")

        self.juego = Juego()

        self.botones = []

        self.crear_tablero()

        boton_reiniciar = tk.Button(
            ventana,
            text="Reiniciar",
            command=self.reiniciar
        )

        boton_reiniciar.grid(
            row=3,
            column=0,
            columnspan=3,
            sticky="nsew"
        )

    def crear_tablero(self):

        for fila in range(3):

            fila_botones = []

            for columna in range(3):

                boton = tk.Button(
                    self.ventana,
                    text="",
                    width=8,
                    height=4,
                    font=("Arial", 18),
                    command=lambda f=fila, c=columna:
                    self.jugar(f, c)
                )

                boton.grid(
                    row=fila,
                    column=columna
                )

                fila_botones.append(boton)

            self.botones.append(fila_botones)

    def jugar(self, fila, columna):

        try:

            simbolo = self.juego.turno_actual

            self.juego.realizar_movimiento(
                fila,
                columna
            )

            self.botones[fila][columna].config(
                text=simbolo
            )

            if self.juego.hay_ganador():

                messagebox.showinfo(
                    "Fin del juego",
                    f"Ganó {simbolo}"
                )

            elif self.juego.es_empate():

                messagebox.showinfo(
                    "Fin del juego",
                    "Empate"
                )

        except ValueError as error:

            messagebox.showwarning(
                "Error",
                str(error)
            )

    def reiniciar(self):

        self.juego.reiniciar()

        for fila in range(3):

            for columna in range(3):

                self.botones[fila][columna].config(
                    text=""
                )


def iniciar_juego():

    ventana = tk.Tk()

    InterfazJuego(ventana)

    ventana.mainloop()