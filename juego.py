class Juego:

    def crear_tablero(self):
        return [[" " for _ in range(3)] for _ in range(3)]

    def __init__(self):
        self.tablero = self.crear_tablero()     
        self.turno_actual = "X"
        self.finalizado = False

    def realizar_movimiento(self, fila, columna):

        if self.finalizado:
            raise ValueError("La partida ha finalizado")

        if self.tablero[fila][columna] != " ":
            raise ValueError("Casilla ocupada")

        self.tablero[fila][columna] = self.turno_actual

        if self.hay_ganador() or self.es_empate():
            self.finalizado = True
            return

        self.turno_actual = "O" if self.turno_actual == "X" else "X"

        

    def verificar_filas(self):

        for fila in self.tablero:
            if fila[0] != " " and fila[0] == fila[1] == fila[2]:
                return True

        return False
    
    def verificar_columnas(self):

        for columna in range(3):

            if (
                self.tablero[0][columna] != " "
                and self.tablero[0][columna]
                == self.tablero[1][columna]
                == self.tablero[2][columna]
            ):
                return True

        return False
    
    def verificar_diagonales(self):

        if (
            self.tablero[0][0] != " "
            and self.tablero[0][0]
            == self.tablero[1][1]
            == self.tablero[2][2]
        ):
            return True

        if (
            self.tablero[0][2] != " "
            and self.tablero[0][2]
            == self.tablero[1][1]
            == self.tablero[2][0]
        ):
            return True

        return False


    def hay_ganador(self):

        return (
            self.verificar_filas()
            or self.verificar_columnas()
            or self.verificar_diagonales())

    def es_empate(self):

        if self.hay_ganador():
            return False

        for fila in self.tablero:
            if " " in fila:
                return False

        return True

    def reiniciar(self):

        self.tablero = self.crear_tablero()

        self.turno_actual = "X"
        self.finalizado = False