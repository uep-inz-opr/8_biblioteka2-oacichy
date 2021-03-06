import ast

class Egzemplarz():
    def __init__ (self, tytul, autor, rok_wyd, wypozyczony):
        self.tytul = tytul
        self.autor = autor
        self.rok_wyd = rok_wyd
        self.wypozyczony = wypozyczony
    def dodaj(self, egzemplarze):
        egzemplarze.append(Egzemplarz(self.tytul, self.autor, self.rok_wyd, self.wypozyczony))
        return True
    def wypozycz(tytul, egzemplarze):
        for i in range(len(egzemplarze)):
            temp = egzemplarze[i]
            if tytul == temp.tytul and temp.wypozyczony == False:
                temp.wypozyczony = True
                return True
        return False
    def oddaj(tytul, egzemplarze):
        for i in range(len(egzemplarze)):
            temp = egzemplarze[i]
            if tytul == temp.tytul and temp.wypozyczony == True:
                temp.wypozyczony = False
                return True
        return False


class Czytelnik():
    def __init__(self, nazwisko):
        self.nazwisko = nazwisko
    def dodaj(self, czytelnicy):
        czytelnicy.append(Czytelnik(self.nazwisko))

class Wypozyczone():
    def __init__(self, nazwisko, tytul):
        self.nazwisko = nazwisko
        self.tytul = tytul
    def dodaj(self, wypozyczenia):
        wypozyczenia.append(Wypozyczone(self.nazwisko, self.tytul))
    def czywypozyczone(nazwisko, tytul, wypozyczenia):
        for i in range(len(wypozyczenia)):
            temp = wypozyczenia[i]
            if nazwisko == temp.nazwisko and tytul == temp.tytul:
                return True
        return False
    def czymoznawypozyczyc(nazwisko, wypozyczenia):
        licznik = 0
        for i in range(len(wypozyczenia)):
            temp = wypozyczenia[i]
            if nazwisko == temp.nazwisko:
                licznik = licznik + 1
        if licznik > 2:
            return False
        else: 
            return True
    def oddaj(nazwisko, tytul, wypozyczenia):
        for i in range(len(wypozyczenia)):
            temp = wypozyczenia[i]
            if nazwisko == temp.nazwisko and tytul == temp.tytul:
                del wypozyczenia[i]
                return True
        return False


def czyjestwliscie(czytelnicy, nazwisko):
    for i in range(len(czytelnicy)):
        temp = czytelnicy[i]
        if nazwisko == temp.nazwisko:
            return True
    return False
    
czytelnicy = []
egzemplarze = []
wyniki = []
wypozyczenia = []

n = input()
for i in range(0, int(n)):
    temp = eval(input())
    if temp[0] == "dodaj":
        dodaj = Egzemplarz.dodaj((Egzemplarz(temp[1], temp[2], temp[3], False)), egzemplarze)
        wyniki.append(dodaj)
    if temp[0] == "wypozycz":
        czyjuzjest = czyjestwliscie(czytelnicy, temp[1])
        if czyjuzjest is False:
            Czytelnik.dodaj((Czytelnik(temp[1])), czytelnicy)
        czymoznawypozyczyc = Wypozyczone.czymoznawypozyczyc(temp[1], wypozyczenia)
        if czymoznawypozyczyc is True:
            czywypozyczone = Wypozyczone.czywypozyczone(temp[1], temp[2], wypozyczenia)
            if czywypozyczone == False:
                wypozycz = Egzemplarz.wypozycz(temp[2], egzemplarze)
                wyniki.append(wypozycz)
                if wypozycz == True:
                    Wypozyczone.dodaj(Wypozyczone(temp[1], temp[2]), wypozyczenia)
            else:
                wyniki.append(False)
        else:
            wyniki.append(False)
    if temp[0] == "oddaj":
        czywypozyczone = Wypozyczone.czywypozyczone(temp[1], temp[2], wypozyczenia)
        if czywypozyczone == False:
            wyniki.append(czywypozyczone)
        else:
            oddaj = Wypozyczone.oddaj(temp[1], temp[2], wypozyczenia)
            Egzemplarz.oddaj(temp[2], egzemplarze)
            wyniki.append(oddaj)


for i in range(len(wyniki)):
    temp = wyniki[i]
    print(temp)

