from cx_Freeze import setup, Executable

executables = [Executable("Pokesudoku.py")]

setup(
    name="Pokesudoku",
    version="1.0",
    description="Juego de palabras cruzadas de pokemon",
    executables=executables
)
