import self


class GrafMacierzSasiedztwa:
    def __init__(self, liczba_wiercholkow):
        self.A = liczba_wiercholkow
        self.macierz = [[0 for _ in range(self.A)] for _ in range(self.A)]

    def dodaj_krawedz(self, u, v):
        if 0 <= u < self.A and 0 <= v < self.A:
            self.macierz[u][v] = 1
            self.macierz[v][u] = 1

    def wyswietl(self):
        for wiersz in self.macierz:
            print(wiersz)

class GrafListaSasiadow:
    def __init__(self, skierowany=False):
        self.skierowany = skierowany
        self.adj_list = {}
    def dodaj_wierzcholek(self, v):
        if v not in self.adj_list:
            self.adj_list[v] = []

    def dodaj_krawedz(self, u, v, waga):
        self.dodaj_wierzcholek(u)
        self.dodaj_wierzcholek(v)

        self.adj_list[u].append((v, waga))

        if not self.skierowany:
            self.adj_list[v].append((u, waga))

    def wyswietl(self):
        for wiersz in self.adj_list:
            print(f"{wiersz} -> {self.adj_list[wiersz]}")

class GrafDwochTablic:
    def __init__(self):
        self.wierzcholki = []
        self.sasiedzi = []

    def dodaj_wierzcholek(self, v):
        if v not in self.wierzcholki:
            self.wierzcholki.append(v)
            self.sasiedzi.append([])

    def pobierz_indeks_wierzcholka(self, v):
        if v in self.wierzcholki:
            return self.wierzcholki.index(v)
        return -1

    def dodaj_krawedz(self, v1, v2, skierowany=False):
        idx1 = self.pobierz_indeks_wierzcholka(v1)
        idx2 = self.pobierz_indeks_wierzcholka(v2)

        if idx1 != -1 and idx2 != -1:
            self.sasiedzi[idx1].append(v2)
            if not skierowany:
                self.sasiedzi[idx2].append(v1)
        else:
            print("Jeden lub oba wierzchołki nie istnieją.")

    def wyswietl(self):
        for i in range(len(self.wierzcholki)):
            print(f"{self.wierzcholki[i]} -> {self.sasiedzi[i]}")

print("Graf z wykorzystaniem macierzy sasiadow")
g1 = GrafMacierzSasiedztwa(4)
g1.dodaj_krawedz(0, 1)
g1.dodaj_krawedz(0, 2)
g1.dodaj_krawedz(1, 2)
g1.dodaj_krawedz(2, 3)

g1.wyswietl()

print()
print("================")
print()

print("Graf z wykorzystaniem listy sąsiadów")
g2 = GrafListaSasiadow(skierowany=False)
g2.dodaj_krawedz(1, 2, 4)
g2.dodaj_krawedz(1, 3, 2)
g2.dodaj_krawedz(2, 3, 5)
g2.dodaj_krawedz(3, 4, 1)

g2.wyswietl()

print()
print("================")
print()

print("Graf z wykorzystaniem dwóch tablic")
g3 = GrafDwochTablic()
g3.dodaj_wierzcholek("A")
g3.dodaj_wierzcholek("B")
g3.dodaj_wierzcholek("C")
g3.dodaj_wierzcholek("D")

g3.dodaj_krawedz("A", "B")
g3.dodaj_krawedz("A", "C")
g3.dodaj_krawedz("B", "D")
g3.dodaj_krawedz("C", "D")

g3.wyswietl()