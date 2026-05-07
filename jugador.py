class Jugador:
    def __init__(self):
        self.__codigo:str = None
        self.__nombre:str = None
        self.__edad:str = None
        self.__pos:int = 0
        self.__condicion:str = "vivo"
        self.__emoji:str = None
        self.__tiempo:str = None
        self.__saltaTurno = False
        self.__startTime = None
    @property
    def codigo(self): 
        return self.__codigo
    @codigo.setter
    def codigo(self, codigo): 
        self.__codigo = codigo
    @property
    def nombre(self): 
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre): 
        self.__nombre = nombre
    @property
    def edad(self): 
        return self.__edad
    @edad.setter
    def edad(self, edad): 
        self.__edad = edad
    @property
    def pos(self): 
        return self.__pos
    @pos.setter
    def pos(self, pos): 
        self.__pos = pos
    @property
    def condicion(self): 
        return self.__condicion
    @condicion.setter
    def condicion(self, condicion): 
        self.__condicion = condicion
    @property
    def emoji(self): 
        return self.__emoji
    @emoji.setter
    def emoji(self, emoji): 
        self.__emoji = emoji
    @property
    def tiempo(self):
        return self.__tiempo
    @tiempo.setter
    def tiempo(self, time:str):
        self.__tiempo = time
    @property
    def saltaTurno(self): 
        return self.__saltaTurno
    @saltaTurno.setter
    def saltaTurno(self, valor): 
        self.__saltaTurno = valor
    @property
    def startTime(self): 
        return self.__startTime
    @startTime.setter
    def startTime(self, v): 
        self.__startTime = v
    def __str__(self):
        return f"Codigo: {self.codigo}\nNombre: {self.nombre}\nEdad: {self.edad}\nPosición: {self.pos}\nCondición: {self.condicion}\nEmoji: {self.emoji}"