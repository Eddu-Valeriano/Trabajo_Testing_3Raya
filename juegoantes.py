class Juego:

    def __init__(self):
        self.tablero = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]

        self.turno_actual = "X"
        self.finalizado = False

    def realizar_movimiento(self, fila, columna):

        if self.finalizado:
            raise ValueError("La partida ha finalizado")

        if self.tablero[fila][columna] != " ":
            raise ValueError("Casilla ocupada")

        self.tablero[fila][columna] = self.turno_actual

        if self.turno_actual == "X":
            self.turno_actual = "O"
        else:
            self.turno_actual = "X"

    def hay_ganador(self):

        # Filas
        for fila in self.tablero:
            if fila[0] != " " and fila[0] == fila[1] == fila[2]:
                return True

        # Columnas
        for columna in range(3):
            if (
                self.tablero[0][columna] != " "
                and self.tablero[0][columna]
                == self.tablero[1][columna]
                == self.tablero[2][columna]
            ):
                return True

        # Diagonal principal
        if (
            self.tablero[0][0] != " "
            and self.tablero[0][0]
            == self.tablero[1][1]
            == self.tablero[2][2]
        ):
            return True

        # Diagonal secundaria
        if (
            self.tablero[0][2] != " "
            and self.tablero[0][2]
            == self.tablero[1][1]
            == self.tablero[2][0]
        ):
            return True

        return False

    def es_empate(self):

        if self.hay_ganador():
            return False

        for fila in self.tablero:
            if " " in fila:
                return False

        return True

    def reiniciar(self):

        self.tablero = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]

        self.turno_actual = "X"
        self.finalizado = False