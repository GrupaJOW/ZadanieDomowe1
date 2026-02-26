class GrafMacierzSasiedztwa:
    def __init__(self, n):
        self.macierz = [[0] * n for _ in range(n)]

    def dodaj_krawedz(self, u, v, waga):
        self.macierz[u][v] = waga
        self.macierz[v][u] = waga

    def wyswietl(self):
        for wiersz in self.macierz:
            print(wiersz)


class GrafListaSasiadow:
    def __init__(self):
        self.adj_list = {}

    def dodaj_krawedz(self, u, v, waga):
        self.adj_list.setdefault(u, []).append((v, waga))
        self.adj_list.setdefault(v, []).append((u, waga))

    def wyswietl(self):
        for wiersz in self.adj_list:
            print(f"{wiersz} -> {self.adj_list[wiersz]}")


class GrafDwochTablic:
    def __init__(self):
        self.wierzcholki = []
        self.sasiedzi = []

    def dodaj_krawedz(self, u, v, waga):
        if u not in self.wierzcholki:
            self.wierzcholki.append(u)
            self.sasiedzi.append([])
        if v not in self.wierzcholki:
            self.wierzcholki.append(v)
            self.sasiedzi.append([])

        self.sasiedzi[self.wierzcholki.index(u)].append((v, waga))
        self.sasiedzi[self.wierzcholki.index(v)].append((u, waga))

    def wyswietl(self):
        for i in range(len(self.wierzcholki)):
            print(f"{self.wierzcholki[i]} -> {self.sasiedzi[i]}")


n, m = map(int, input().split())

g1 = GrafMacierzSasiedztwa(n)
g2 = GrafListaSasiadow()
g3 = GrafDwochTablic()

for _ in range(m):
    u, v, waga = map(int, input().split())
    g1.dodaj_krawedz(u, v, waga)
    g2.dodaj_krawedz(u, v, waga)
    g3.dodaj_krawedz(u, v, waga)

print("Graf z wykorzystaniem macierzy sasiadow")
g1.wyswietl()
print("\n---------------\n")
print("Graf z wykorzystaniem listy sasiadow")
g2.wyswietl()
print("\n---------------\n")
print("Graf z wykorzystaniem dwoch tablic")
g3.wyswietl()