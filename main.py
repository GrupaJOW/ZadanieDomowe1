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
        for wierzcholek in self.adj_list:
            print(f"{wierzcholek} -> {self.adj_list[wierzcholek]}")


class GrafDwochTablic:
    def __init__(self, n):
        self.wierzcholki = list(range(n))
        self.sasiedzi = [[] for _ in range(n)]

    def dodaj_krawedz(self, u, v, waga=1):
        self.sasiedzi[u].append((v, waga))

    def wyswietl(self):
        for i in range(len(self.wierzcholki)):
            print(f"{self.wierzcholki[i]} -> {self.sasiedzi[i]}")

    def sasiedzi_wierzcholka(self, v):
        if 0 <= v < len(self.sasiedzi):
            return self.sasiedzi[v]
        return []


n, m = map(int, input().split())

g1 = GrafMacierzSasiedztwa(n)
g2 = GrafListaSasiadow()
g3 = GrafDwochTablic(n)  # <- zmiana: podajemy n

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