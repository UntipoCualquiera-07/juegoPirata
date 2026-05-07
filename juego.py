import pandas as pd
import random as rm
from colorama import Fore
from datetime import datetime
from jugador import Jugador
from tablero import Tablero
from sistema import Sistema
from estadisticas import Estadisticas
from graficas import Graficas

class Juego:
    def __init__(self):
        self.juegoTerminado = False
        self.__dtaFrame = self.verificarDatos()
        if self.__dtaFrame is None:
            self.crearNuevoJuego()
        else:
            self.cargarDatos()
            self.__tablero = Tablero()
            self.__tablero.generaTablero()

    def crearNuevoJuego(self):
        self.juegoTerminado = False
        self.__dtaFrame = pd.DataFrame(columns=["CODIGO","NOMBRE","EDAD","POSICION","TIEMPO PARTIDA"])
        self.__dtaFrame.to_excel("Estadisticas.xlsx", sheet_name="jugadores", index=False)
        self.__listaJugadores = []
        self.__tablero = Tablero()
        self.__tablero.generaTablero()
        print(Fore.GREEN + "🔄 Nuevo juego iniciado. Estadísticas y gráficas reiniciadas.\n")
        print(self.__tablero)

    def verificarDatos(self):
        try:
            df = pd.read_excel("Estadisticas.xlsx", sheet_name="jugadores")
            if df.empty:
                return None
            return df
        except FileNotFoundError:
            return None

    def cargarDatos(self):
        self.__listaJugadores = []
        dtaFrame = self.__dtaFrame
        self.crearNuevoJuego()
        listaEmojis = ["🚀", "⚓", "🏴‍☠️", "🗺️", "💰", "🏝️", "⛵"]
        for i, fila in dtaFrame.iterrows():
            jugador = Jugador()
            jugador.codigo = fila["CODIGO"]
            jugador.nombre = fila["NOMBRE"]
            jugador.edad = fila["EDAD"]
            jugador.tiempo = fila.get("TIEMPO PARTIDA", None)
            jugador.pos = 0
            jugador.condicion = "vivo"
            jugador.emoji = rm.choice(listaEmojis)
            self.__listaJugadores.append(jugador)
        print(f"{len(self.__listaJugadores)} jugadores cargados desde el archivo.")

    def añadirJugadores(self):
        listaEmojis = ["🚀", "⚓", "🏴‍☠️", "🗺️", "💰", "🏝️", "⛵"]
        emoji = rm.choice(listaEmojis)
        nombre = Sistema.validaEntrada("strMin", "Ingrese nombre del jugador", 2)
        edad = Sistema.validaEntrada("intMin", "Ingrese su edad", 8, 90)
        jugador = Jugador()
        jugador.nombre = nombre
        jugador.edad = edad
        jugador.codigo = Sistema.generaID(self.__listaJugadores)
        jugador.emoji = emoji
        self.__listaJugadores.append(jugador)
        Sistema.caja(str(jugador))
    
    def iniciarJuego(self):
        if self.__listaJugadores is None or len(self.__listaJugadores) < 2:
            print(Fore.RED + "Debe haber al menos 2 jugadores.")
            return
        print(self.__tablero)
        for jugador in self.__listaJugadores:
            jugador.pos = 0
            jugador.condicion = "vivo"
            jugador.startTime = datetime.now()
        sigue = True
        while sigue:
            self.__tablero.mostrarTablero(self.__listaJugadores)
            for jugador in self.__listaJugadores:
                if jugador.saltaTurno:
                    print(Fore.BLUE + f"💥 {jugador.nombre} pierde este turno por el cañonazo")
                    jugador.saltaTurno = False
                    continue
                if jugador.condicion == "pierde":
                    continue
                opc = input(f"\n{jugador.nombre} ({jugador.emoji}) ¿tirar dados? (y/n): ").lower()
                if opc == "n":
                    final = datetime.now()
                    jugador.condicion = "pierde"
                    jugador.tiempo = Sistema.calculaDuracion(final - jugador.startTime)
                    print(Fore.RED + f"{jugador.nombre} pierde la partida.")
                else:
                    dado = rm.randint(1, 6)
                    print(f"{jugador.nombre} avanza {dado} espacios")
                    jugador.pos += dado
                    self.validaEvento(jugador)
                if jugador.condicion == "gana":
                    print(Fore.GREEN + f"🎉 ¡{jugador.nombre} ha GANADO!")
                    final = datetime.now()
                    jugador.tiempo = Sistema.calculaDuracion(final - jugador.startTime)
                    for j in self.__listaJugadores:
                        if j != jugador and j.condicion == "vivo":
                            j.condicion = "pierde"
                            j.tiempo = Sistema.calculaDuracion(final - j.startTime)
                    self.juegoTerminado = True
                    sigue = False
                    break
            if not self.juegoTerminado:
                vivos = []
                for j in self.__listaJugadores:
                    if j.condicion in ["vivo", "gana"]:
                        vivos.append(j)
                if len(vivos) == 1:
                    final = datetime.now()
                    print(Fore.GREEN + f"\n🏆 {vivos[0].nombre} ha ganado por ser el único superviviente.")
                    vivos[0].tiempo = Sistema.calculaDuracion(final - vivos[0].startTime)
                    self.juegoTerminado = True
                    break
        self.crearEstadisticas()
    
    def validaEvento(self, jugador:Jugador):
        final = datetime.now()
        pos = jugador.pos
        if pos >= 30:
            jugador.pos = 30
            jugador.condicion = "gana"
            jugador.tiempo = Sistema.calculaDuracion(final - jugador.startTime)

            print(Fore.GREEN + f"🏁 ¡{jugador.nombre} llegó a la META!")
            return
        evento = self.__tablero.obtenerCasilla(pos)
        if evento == 0:
            print("No pasa nada :)")
        else:
            if 5 <= pos+1 <= 10:
                jugador.pos = max(0, jugador.pos - 2)
                print(Fore.RED + f"⚠️ Trampa de Arena: {jugador.nombre} retrocede 2 casillas")
            elif 11 <= pos+1 <= 18:
                jugador.saltaTurno = True
                print(Fore.BLUE + f"💥 Cañonazo! {jugador.nombre} perderá su próximo turno")
            elif 19 <= pos+1 <= 24:
                jugador.pos += 4
                print(Fore.YELLOW + f"💰 Cofre del oro! {jugador.nombre} avanza +4")
            elif 25 <= pos+1 <= 29:
                print(Fore.MAGENTA + f"🐙 Kraken! {jugador.nombre} enfrenta su destino…")
                opc = input("¿Tirar dado? (y/n): ").lower()
                if opc != "y":
                    jugador.condicion = "pierde"
                    jugador.tiempo = Sistema.calculaDuracion(final - jugador.startTime)
                    print(Fore.RED + f"{jugador.nombre} perdió.")
                    return
                dado = rm.randint(1, 6)
                print(f"Dado: {dado}")
                if dado % 2 == 0:
                    jugador.pos = 0
                    print(Fore.CYAN + f"{jugador.nombre} vuelve al inicio")
                else:
                    jugador.condicion = "pierde"
                    jugador.tiempo = Sistema.calculaDuracion(final - jugador.startTime)
                    print(Fore.RED + f"{jugador.nombre} fue devorado por el Kraken 💀")
        print(f"📍 Nueva posición: {jugador.pos}")

    def crearEstadisticas(self):
        e = Estadisticas()
        e.guardaDatos(self.__listaJugadores)

    def mostrarGrafica(self):
        df = self.verificarDatos()
        if df is None or df.empty:
            print(Fore.RED + "❌ No hay estadísticas para mostrar.")
            return
        self.__dtaFrame = df
        g = Graficas()
        g.barras(self.__dtaFrame)

    def mostrarReglas(self):
        Sistema.titulo("📘 INSTRUCCIONES")
        print("""
                1. Crear un nuevo juego (necesario para iniciar).
                2. Registrar mínimo 2 jugadores.
                3. El tablero tiene trampas, cofres y el Kraken.
                4. El objetivo es llegar a la casilla 30.
                5. Si dices 'n' durante tu turno, abandonas la partida.
                """)

    def menu(self):
        opc = 0
        while opc != 6:
            Sistema.banner("🏴‍☠️ EL TESORO PIRATA 🕹️")
            print(Fore.CYAN + "1." + Fore.WHITE + " Instrucciones")
            print(Fore.CYAN + "2." + Fore.WHITE + " Ingresar jugador")
            print(Fore.CYAN + "3." + Fore.WHITE + " Nuevo juego")
            print(Fore.CYAN + "4." + Fore.WHITE + " Iniciar juego")
            print(Fore.CYAN + "5." + Fore.WHITE + " Ver estadísticas")
            print(Fore.CYAN + "6." + Fore.WHITE + " Salir")
            try:
                opc = int(input(Fore.YELLOW + "\nSeleccione una opción: "))
            except:
                print(Fore.RED + "Opción no válida.")
                continue
            match opc:
                case 1: self.mostrarReglas()
                case 2: self.añadirJugadores()
                case 3: self.crearNuevoJuego()
                case 4: self.iniciarJuego()
                case 5: self.mostrarGrafica()
                case 6: Sistema.banner("👋 Saliendo del juego...")
                case _: print(Fore.RED + "Opción inválida")