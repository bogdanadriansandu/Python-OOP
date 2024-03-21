# Pilonii OOP

# ABSTRACTIZARE
# Clasa abstractă FormaGeometrica
# Conține un field PI=3.14
# Conține o metodă abstractă aria (opțional)
# Conține o metodă a clasei descrie() - aceasta printează pe ecran ‘Cel mai probabil am colturi’

from abc import ABC, abstractmethod


class FormaGeometrica(ABC):
    PI = 3.14

    @abstractmethod
    def aria(self):
        pass

    @classmethod
    def descrie(cls):
        print("Cel mai probabil am colturi")


# MOSTENIRE
# Clasa Pătrat - moștenește FormaGeometrica
# constructor pentru latură

class Patrat(FormaGeometrica):
    def __init__(self, latura):
        self.__latura = latura

    # ENCAPSULARE
    # latura este proprietate privată
    # Implementează getter, setter, deleter pentru latură
    # Implementează metoda cerută de interfață (opțional, doar dacă ai ales să implementezi metoda abstractă aria)

    def get_latura(self):
        return self.__latura

    def set_latura(self, latura):
        self.__latura = latura

    def del_latura(self):
        self.__latura = None

    def aria(self):
        return self.__latura ** 2


# Clasa Cerc - moștenește FormaGeometrica
# constructor pentru rază
# raza este proprietate privată
# Implementează getter, setter, deleter pentru rază
""" Implementează metoda cerută de interfață - în calcul folosește field PI mostenit din clasa părinte (opțional, doar
dacă ai ales să implementezi metoda abstractă aria) """


class Cerc(FormaGeometrica):
    def __init__(self, raza):
        self.__raza = raza

    def get_raza(self):
        return self.__raza

    def set_raza(self, raza):
        self.__raza = raza

    def del_raza(self):
        self.__raza = None

    def aria(self):
        return self.PI * self.__raza ** 2

    # POLYMORFISM
    # Definește o nouă metodă descrie - printează ‘Eu nu am colturi’
    # Creează un obiect de tip Pătrat și joacă-te cu metodele lui
    # Creează un obiect de tip Cerc și joacă-te cu metodele lui

    def descrie(self):
        print('Eu nu am colturi')


patrat = Patrat(7)

print(patrat.get_latura())
print(f"Aria patrat: {patrat.aria()}")
patrat.set_latura(9)
print(patrat.get_latura())
print(f"Aria patrat: {patrat.aria()}")
patrat.descrie()
patrat.del_latura()
print(patrat.get_latura())

try:
    print(f"Aria patrat: {patrat.aria()}")
except TypeError:
    print("Latura a fost stearsa, nu se poate calcula aria patratului.")

cerc = Cerc(5)

print(cerc.get_raza())
print(f"Aria cerc: {cerc.aria()}")
cerc.set_raza(10)
print(cerc.get_raza())
print(f"Aria cerc: {cerc.aria()}")
cerc.descrie()
cerc.del_raza()
print(cerc.get_raza())

try:
    print(f"Aria cerc: {cerc.aria()}")
except TypeError:
    print("Raza a fost stearsa, nu se poate calcula aria cercului.")