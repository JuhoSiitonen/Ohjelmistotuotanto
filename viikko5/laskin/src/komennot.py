
class Summa:
    def __init__(self, sovelluslogiikka, io):
        self.sovelluslogiikka = sovelluslogiikka
        self.io = io

    def suorita(self):
        luku = int(self.io())
        self.sovelluslogiikka.plus(luku)

class Erotus:
    def __init__(self, sovelluslogiikka, io):
        self.sovelluslogiikka = sovelluslogiikka
        self.io = io

    def suorita(self):
        luku = int(self.io())
        self.sovelluslogiikka.miinus(luku)

class Nollaus:
    def __init__(self, sovelluslogiikka, io):
        self.sovelluslogiikka = sovelluslogiikka
        self.io = io

    def suorita(self):
        self.sovelluslogiikka.nollaa()

class Kumoa:
    def __init__(self, sovelluslogiikka, io):
        self.sovelluslogiikka = sovelluslogiikka
        self.io = io

    def suorita(self):
        self.sovelluslogiikka.kumoa()
    



