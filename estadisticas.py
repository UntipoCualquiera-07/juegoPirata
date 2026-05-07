import pandas as pd

class Estadisticas:
    def __init__(self):
        self.__dtaFrame = None
    def guardaDatos(self, listaJugadores):
        nombres = []
        edades = []
        codigos = []
        tiempos = []
        posiciones = []
        for jugador in listaJugadores:
            codigos.append(jugador.codigo)
            nombres.append(jugador.nombre)
            edades.append(jugador.edad)
            tiempos.append(jugador.tiempo)
            posiciones.append(jugador.pos)
        self.__dtaFrame = pd.DataFrame(
            {
                "CODIGO": codigos,
                "NOMBRE":nombres,
                "EDAD":edades,
                "POSICION":posiciones,
                "TIEMPO PARTIDA": tiempos,
            }
        )
        self.__dtaFrame.to_excel("Estadisticas.xlsx", sheet_name="jugadores", index=False)