# 🎮 Tres en Raya (Tic Tac Toe) - Aplicando TDD

## 📌 Descripción

Este proyecto consiste en el desarrollo del juego Tres en Raya (Tic Tac Toe) utilizando la metodología TDD (Test Driven Development).

El proyecto fue desarrollado en Python y cuenta con una interfaz gráfica creada con Tkinter.

La implementación siguió el ciclo:

RED → GREEN → REFACTOR

---

## 🎯 Objetivos

- Aplicar la metodología TDD.
- Implementar pruebas unitarias.
- Desarrollar la lógica del juego.
- Construir una interfaz gráfica.
- Garantizar la calidad mediante cobertura de pruebas.

---

## 🛠️ Tecnologías utilizadas

- Python 3
- Tkinter
- unittest
- coverage

---

## 📂 Estructura del proyecto

TicTacToe-TDD/

├── juego.py

├── interfaz.py

├── main.py

├── test_juego.py

└── README.md

---

## 🚀 Instalación

1. Clonar el repositorio.

2. Ingresar a la carpeta del proyecto.

3. Instalar Coverage.

```bash
pip install coverage
```

---

## ▶️ Ejecutar el juego

```bash
python main.py
```

---

## 🧪 Ejecutar las pruebas

```bash
python -m unittest test_juego.py
```

---

## 📊 Ejecutar la cobertura de pruebas

```bash
coverage run -m unittest test_juego.py

coverage report
```

Para generar el reporte visual:

```bash
coverage html
```

---

## 🔴🟢🔵 Aplicación de TDD

### 🔴 RED

Se diseñaron pruebas unitarias antes de implementar el código.

### 🟢 GREEN

Se implementó el código mínimo necesario para que las pruebas pasaran.

### 🔵 REFACTOR

Se optimizó el código eliminando duplicidad y mejorando la organización.

---

## 📋 Funcionalidades implementadas

- Creación del tablero.
- Gestión de turnos.
- Registro de movimientos.
- Validación de casillas ocupadas.
- Detección de ganador.
- Detección de empate.
- Reinicio de partida.
- Interfaz gráfica.
- Control de errores.

---

## 👨‍💻 Autor(es)

Proyecto académico desarrollado para el curso: Testing, Implantación y Mantenimiento de Sistemas.

- _Calla Martinez Miguel_
- _Valeriano Cuba Eddu_
