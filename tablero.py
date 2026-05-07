import random as rm
from colorama import Fore

class Tablero:
    def __init__(self):
        self.__listaCasillas = []
    def generaTablero(self):
        for _ in range(30):
            self.__listaCasillas.append(rm.randint(0, 1))
    def obtenerCasilla(self, pos:int):
        return self.__listaCasillas[pos]
    def mostrarTablero(self, jugadores:list):
        print(Fore.CYAN + "\n" + "═" * 60)
        print(Fore.YELLOW + "📍 TABLERO DE JUEGO".center(60))
        print(Fore.CYAN + "═" * 60)
        tablero = ""
        for i in range(0, 31):
            jugadores_en_casilla = []
            for jugador in jugadores:
                if jugador.pos == i:
                    jugadores_en_casilla.append(f"{jugador.nombre[0]}{jugador.emoji}")
            jugador_str = ", ".join(jugadores_en_casilla)
            if i == 0:
                contenido = f"INICIO {('(' + jugador_str + ')') if jugador_str else ''}"
            elif i == 30:
                contenido = f"META {('(' + jugador_str + ')') if jugador_str else ''}"
            else:
                contenido = f"{str(i).rjust(2)} {jugador_str}"
            tablero += Fore.BLUE + f"[{contenido}] "
        print(tablero)
        print(Fore.CYAN + "═" * 60)
    def __str__(self):
        texto = ""
        for i, c in enumerate(self.__listaCasillas):
            casilla = i + 1
            if 5 <= casilla <= 10:
                texto += f"Casilla {casilla}: Trampa de Arena\n" if c == 1 else f"Casilla {casilla}: Nada\n"
            elif 11 <= casilla <= 18:
                texto += f"Casilla {casilla}: Cañonazo\n" if c == 1 else f"Casilla {casilla}: Nada\n"
            elif 19 <= casilla <= 24:
                texto += f"Casilla {casilla}: Cofre de oro\n" if c == 1 else f"Casilla {casilla}: Nada\n"
            elif 25 <= casilla <= 29:
                texto += f"Casilla {casilla}: Kraken\n" if c == 1 else f"Casilla {casilla}: Nada\n"
            else:
                texto += f"Casilla {casilla}: Nada\n"
        return texto