import unittest
from juego import Juego


class TestJuego(unittest.TestCase):

    def test_x_debe_iniciar_la_partida(self):
        juego = Juego()
        self.assertEqual(juego.turno_actual, "X")

    def test_crear_tablero_vacio(self):
        juego = Juego()

        self.assertEqual(len(juego.tablero), 3)
    
    def test_registrar_movimiento(self):
        juego = Juego()

        juego.realizar_movimiento(0, 0)

        self.assertEqual(juego.tablero[0][0], "X")

    def test_no_permitir_casilla_ocupada(self):
        juego = Juego()

        juego.realizar_movimiento(0, 0)

        with self.assertRaises(ValueError):
            juego.realizar_movimiento(0, 0)

    def test_cambiar_turno(self):
        juego = Juego()

        juego.realizar_movimiento(0, 0)

        self.assertEqual(juego.turno_actual, "O")

    def test_detectar_victoria_horizontal(self):
        juego = Juego()

        juego.tablero = [
            ["X", "X", "X"],
            ["O", " ", "O"],
            [" ", " ", " "]
        ]
        
        self.assertTrue(juego.hay_ganador())

    def test_detectar_victoria_vertical(self):
        juego = Juego()

        juego.tablero = [
            ["O", "X", " "],
            ["O", "X", " "],
            ["O", " ", "X"]
        ]

        self.assertTrue(juego.hay_ganador())

    def test_detectar_victoria_diagonal(self):
        juego = Juego()

        juego.tablero = [
            ["X", "O", " "],
            [" ", "X", "O"],
            [" ", " ", "X"]
        ]

        self.assertTrue(juego.hay_ganador())

    def test_detectar_empate(self):
        juego = Juego()

        juego.tablero = [
            ["X", "O", "X"],
            ["X", "O", "O"],
            ["O", "X", "X"]
        ]

        self.assertTrue(juego.es_empate())


    def test_reiniciar_partida(self):
        juego = Juego()

        juego.realizar_movimiento(0, 0)

        juego.reiniciar()

        self.assertEqual(juego.tablero[0][0], " ")


if __name__ == "__main__":
    unittest.main()