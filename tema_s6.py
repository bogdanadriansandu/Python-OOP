"""
Creati o clasa cinema in care sa stocati atributele si metodele de care e nevoie ca sa puteti sa gestiona un sistem de
tip cinema (acestea vor fi implementate la alegerea voastra). Clasa nu va avea constructor.

Creati cel putin 5 metode de test si 10 atribute.

Apelati pe rand fiecare dintre metodele create si respectiv printati  pe ecran toate valorile atributelor pentru
fiecare obiect. Printarea se va face cu formatare si, pentru o complexitate mai mare, puteti sa puneti toate obiectele
instantiate intr-o lista pe care sa o parcurgeti cu un for (si astfel sa faceti printarea pentru toate elementele
concomitent). Repetati actiunea cu while si respectiv cu foreach. Rulati codul.

Modificati clasa prin adaugarea unui constructor care sa primeasca doi parametri care sa populeze, la alegere, doua
dintre atributele definite in clasa. Rulati codul. Ce observati?

Faceti modificarile necesare astfel incat sistemul sa nu mai returneze eroare.

Modificati constructorul astfel incat sa controlati valorile care sunt salvate in fiecare atribut. Spre exemplu: daca
se incearca salvarea numarului de locuri pentru cinema cu un numar mai mare de 500 sa se printeze pe ecran  o eroare.
Rulati codul din nou si introduceti o valoare care sa nu respecte conditia definita in constructor (ex: un numar de
locuri mai mare decat 500). Ce observati?
"""


class Cinema:
    def __init__(self, capacitate=0, nr_sali=1):
        self.capacitate = capacitate
        self.nr_sali = nr_sali
        if capacitate > 500:
            raise ValueError("Eroare: Capacitatea nu poate fi mai mare de 500 locuri.")
        if nr_sali > 7:
            raise ValueError("Eroare: Nu pot fi mai mult de 7 sali in fiecare locatie")

    nume_cinema = ''
    nr_spectatori = 0
    nr_bilete_vandute = 0
    pret_bilet = 0
    gen_film = ''
    durata_film = ''
    reducere = 0
    adresa_cinema = ''
    nume_sala = ''
    nume_film = ''
    filme = []

    @classmethod
    def get_adresa_cinema(cls):
        return cls.adresa_cinema

    def ruleaza_film(self, nume_sala, nume_film, durata_film):
        self.nume_sala = nume_sala
        self.nume_film = nume_film
        self.durata_film = durata_film
        print(f"In sala {self.nume_sala} ruleaza filmul {self.nume_film} cu o durata de {self.durata_film} minute.")

    def vinde_bilete(self, nr_bilete_vandute):
        if nr_bilete_vandute > 0 and nr_bilete_vandute <= self.capacitate - self.nr_spectatori:
            self.nr_bilete_vandute = nr_bilete_vandute
            self.nr_spectatori += nr_bilete_vandute
            print(f"Nr bilete vandute: {self.nr_bilete_vandute}")
        else:
            print("Nu sunt suficiente locuri disponibile sau numarul de bilete este invalid.")

    def calculeaza_cost_bilete(self, nr_bilete_vandute, pret_bilet, reducere=0):
        if nr_bilete_vandute > 0 and pret_bilet > 0:
            self.nr_bilete_vandute = nr_bilete_vandute
            self.reducere = reducere
            self.pret_bilet = pret_bilet
            return self.nr_bilete_vandute * self.pret_bilet * (1 - self.reducere)
        else:
            return "Numarul de bilete sau pretul biletului sunt invalide."

    def afiseaza_gen_film(self, nume_film, gen_film):
        self.nume_film = nume_film
        self.gen_film = gen_film
        print(f"Genul filmului {self.nume_film} este: {self.gen_film}")

    def afiseaza_filme(self, nume_cinema, filme):
        self.nume_cinema = nume_cinema
        self.filme = filme
        print(f"La cinema {nume_cinema} ruleaza urmatoarele filme: {filme}")


luceafarul = Cinema(400, 1)
patria = Cinema(450, 1)
cinema_mall = Cinema(500, 4)

print(Cinema.get_adresa_cinema())

luceafarul.ruleaza_film('Sala mare', 'Avatar 2', '150 minute')
luceafarul.vinde_bilete(84)
print(luceafarul.calculeaza_cost_bilete(26, 29))
luceafarul.afiseaza_gen_film('Dune', 'SF')
luceafarul.afiseaza_filme("Luceafarul", ['Star Trek', 'Titanic', 'Inception', 'Barbie'])

# print(f"Atribute cinema {luceafarul.nume_cinema}: nume_cinema = {luceafarul.nume_cinema}, nume_sala = "
#       f"{luceafarul.nume_sala}, nume_film = {luceafarul.nume_film}, durata_film = {luceafarul.durata_film}, "
#       f"nr_bilete_vandute = {luceafarul.nr_bilete_vandute}, adresa_cinema = {luceafarul.adresa_cinema}, "
#       f"pret_bilet = {luceafarul.pret_bilet}, reducere = {luceafarul.reducere}, gen film = {luceafarul.gen_film}, "
#       f"filme = {luceafarul.filme}")

patria.ruleaza_film('Sala Iorga', 'Avenger 2', '125 minute')
patria.vinde_bilete(43)
print(patria.calculeaza_cost_bilete(126, 25))
patria.afiseaza_gen_film('Barbie', 'comedie')
patria.afiseaza_filme("Patria", ['Star Trek', 'Avatar', 'Star Wars', '2 lozuri', 'Barbie'])

# print(f"Atribute cinema {patria.nume_cinema}: nume_cinema = {patria.nume_cinema}, nume_sala = "
#       f"{patria.nume_sala}, nume_film = {patria.nume_film}, durata_film = {patria.durata_film}, "
#       f"nr_bilete_vandute = {patria.nr_bilete_vandute}, adresa_cinema = {patria.adresa_cinema}, "
#       f"pret_bilet = {patria.pret_bilet}, reducere = {patria.reducere}, gen film = {patria.gen_film}, "
#       f"filme = {patria.filme}")

cinema_mall.ruleaza_film('Sala 1', 'Team building', '98 minute')
cinema_mall.vinde_bilete(112)
print(cinema_mall.calculeaza_cost_bilete(112, 33))
cinema_mall.afiseaza_gen_film('Team building', 'comedie')
cinema_mall.afiseaza_filme("Cinema Mall", ['Team building', 'Taxi', 'Nunta pe bani', 'Barbie', 'Rambo'])

# print(f"Atribute cinema {cinema_mall.nume_cinema}: nume_cinema = {cinema_mall.nume_cinema}, nume_sala = "
#       f"{cinema_mall.nume_sala}, nume_film = {cinema_mall.nume_film}, durata_film = {cinema_mall.durata_film}, "
#       f"nr_bilete_vandute = {cinema_mall.nr_bilete_vandute}, adresa_cinema = {cinema_mall.adresa_cinema}, "
#       f"pret_bilet = {cinema_mall.pret_bilet}, reducere = {cinema_mall.reducere}, gen film = {cinema_mall.gen_film}, "
#       f"filme = {cinema_mall.filme}")

lista_cinematografe = [luceafarul, patria, cinema_mall]

# cu for
for index in range(len(lista_cinematografe)):
    cinema = lista_cinematografe[index]

    print(f'Obiectul {index + 1} are urmatoarele atribute cu valorile: ')
    for atribut, valoare in vars(cinema).items():
        print(f'{atribut} = {valoare}')

# cu while
i = 0

while i < len(lista_cinematografe):
    cinema = lista_cinematografe[i]

    print(f'Obiectul {i + 1} are urmatoarele atribute cu valorile: ')
    for atribut, valoare in vars(cinema).items():
        print(f'{atribut} = {valoare}')
    i += 1

# cu foreach
for cinema in lista_cinematografe:
    print(f'Obiectul {lista_cinematografe.index(cinema) + 1} are urmatoarele atribute cu valorile: ')
    for atribut, valoare in vars(cinema).items():
        print(f'{atribut} = {valoare}')

try:
    cinema_4 = Cinema(600, 3)
except ValueError as e:
    print(e)

try:
    cinema_5 = Cinema(380, 9)
except ValueError as e:
    print(e)

try:
    cinema_6 = Cinema(650, 12)
except ValueError as e:
    print(e)

cinema_7 = Cinema()
print("cinema_7:", cinema_7.capacitate, "locuri", cinema_7.nr_sali, "sala(i)")
