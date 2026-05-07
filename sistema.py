import random as rm
from colorama import Fore

class Sistema:
    @staticmethod
    def validaEntrada(modo, mensaje, min = 0, max = 0):
        if modo == "strMin":
            while True:
                valor = input(f"{mensaje}: ")
                if min <= len(valor):
                    break
        elif modo == "intMin":
            while True:
                try:
                    valor = int(input(f"{mensaje}: "))
                    if min <= valor <= max:
                        break
                except ValueError:
                    print("Debe ingresar un número.")
        return valor
    @staticmethod
    def generaID(listaJugadores):
        igual = True
        while igual:
            codigo = f"C{rm.randint(1,999):03}"
            igual = False
            for jugador in listaJugadores:
                if jugador.codigo == codigo:
                    igual = True
                    break
        return codigo
    @staticmethod
    def banner(texto):
        print(Fore.CYAN + "=" * 60)
        print(Fore.MAGENTA + f"{texto.center(60)}")
        print(Fore.CYAN + "=" * 60)
    @staticmethod
    def caja(texto):
        lineas = texto.split("\n")
        ancho = max(len(linea) for linea in lineas) + 4
        print(Fore.BLUE + "╔" + "═" * ancho + "╗")
        for l in lineas:
            print(Fore.BLUE + f"║  {l.ljust(ancho-2)}║")
        print(Fore.BLUE + "╚" + "═" * ancho + "╝")
    @staticmethod
    def titulo(texto):
        print(Fore.GREEN + "\n" + "◆" * 50)
        print(Fore.YELLOW + texto.center(50))
        print(Fore.GREEN + "◆" * 50 + "\n")
    @staticmethod
    def calculaDuracion(segundos):
        segundos = int(segundos.total_seconds())
        hora = 0
        minutos = 0
        while segundos>=3600:
            hora+=1
            segundos-=3600
        while segundos>=60:
            minutos+=1
            segundos-=60
        return f"{hora} horas, {minutos} minutos y {segundos} segundos"