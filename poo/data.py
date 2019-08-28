class Data():
    """" Classe para representar uma data, com dia, mês e ano. """
    def __init__(self, dia, mes, ano):
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano

    def getDia(self):
        return self.__dia

    def setDia(self, dia):
        self.__dia = dia

    def getMes(self):
        return self.__mes

    def setMes(self, mes):
        self.__mes = mes

    def getAno(self):
        return self.__ano

    def setAno(self, ano):
        self.__ano = ano

    def __str__(self):
        return "{}/{}/{}".format(self.__dia, self.__mes, self.__ano)


if __name__ == "__main__":
    d = Data(20, 12, 2019)
    print(d.getDia())
    print(d.getMes())
    print(d.getAno())
    d.setDia(28)
    d.setMes(12)
    d.setAno(1981)
    print(d)
