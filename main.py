import numpy as np
orase = np.array(
    ["Satu Mare", "Oradea", "Arad", "Timisoara", "Craiova", "Baia Mare", "Cluj Napoca", "Alba Iulia", "Bistrita", "Targu Mures",
     "Sibiu", "Brasov", "Pitesti", "Suceava", "Iasi", "Piatra Neamt", "Bucuresti", "Braila", "Tulcea", "Constanta"])

# Cautarea Bidirectionala
class BidirectionalSearch:
    def __init__(self, noduri):
        # se initializeaza graful cu numarul de noduri pe care acesta il contine
        self.node = noduri
        self.graph = [None] * self.node
        # creem listele pentru cautarea inainte si inapoi
        self.startPoint_queue = list()
        self.stopPoint_queue = list()
        #INITIALIZEZ SURSA SI DESTINATIA CA FALSE
        self.startPoint_Visited = [False] * self.node
        self.stopPoint_visited = [False] * self.node
        # se initializeaza cele doua liste pentru cautarea inainte si inapoi
        self.startPoint_Parinte = [None] * self.node
        self.stopPoint_parent = [None] * self.node

    def nod_intersectie(self, startPoint, stopPoint):
        node = AdjacentNode(stopPoint)
        node.next = self.graph[startPoint]
        self.graph[startPoint] = node

        node = AdjacentNode(startPoint)
        node.next = self.graph[stopPoint]
        self.graph[stopPoint] = node

    # functie cautare
    def cautare(self, direction='forward'):
        if direction == 'forward':
            # cautare inainte
            current = self.startPoint_queue.pop(0)
            connected_node = self.graph[current]
            while connected_node:
                peak = connected_node.vertex
                if not self.startPoint_Visited[peak]:
                    self.startPoint_queue.append(peak)
                    self.startPoint_Visited[peak] = True
                    self.startPoint_Parinte[peak] = current
                connected_node = connected_node.next
        else:
            # cautare inapoi
            current = self.stopPoint_queue.pop(0)
            connected_node = self.graph[current]
            while connected_node:
                peak = connected_node.vertex
                if not self.stopPoint_visited[peak]:
                    self.stopPoint_queue.append(peak)
                    self.stopPoint_visited[peak] = True
                    self.stopPoint_parent[peak] = current
                connected_node = connected_node.next
    # punct intersectie
    def is_intersecting(self):
        # returnam nodul intersectiei
        # daca exista, daca nu returnam -1
        for i in range(self.node):
            if (self.startPoint_Visited[i] and
                    self.stopPoint_visited[i]):
                return i
        return -1

    # printam nod uriile parcurse de la startpoint la stoppoint
    def print_path(self, intersecting_node,
                   startPoint, stopPoint):

        # printam calea finala
        path = list()
        path.append(intersecting_node)
        i = intersecting_node

        while i != startPoint:
            path.append(self.startPoint_Parinte[i])
            i = self.startPoint_Parinte[i]

        path = path[::-1]
        i = intersecting_node

        while i != stopPoint:
            path.append(self.stopPoint_parent[i])
            i = self.stopPoint_parent[i]

        print("--> Drumul este:")
        path = list(map(str, path))

        for i in range(len(path)):
            print(orase[int(path[i])])
        print(f"Numarul de orase parcurse este: {len(path)}")

    # functie cautare bidimensionala
    def bidirectional_search(self, startPoint, stopPoint):
    # se adauga nodul de start in lista, se trece ca vizitat
        self.startPoint_queue.append(startPoint)
        self.startPoint_Visited[startPoint] = True
        self.startPoint_Parinte[startPoint] = -1
    # inapoi
        self.stopPoint_queue.append(stopPoint)
        self.stopPoint_visited[stopPoint] = True
        self.stopPoint_parent[stopPoint] = -1
        while self.startPoint_queue and self.stopPoint_queue:
            self.cautare(direction='forward')
            self.cautare(direction='backward')

            # nodul de intersectie
            intersecting_node = self.is_intersecting()

            # daca exista nod de intersectie se returneaza calea
            if intersecting_node != -1:
                print(f"Sa gasit o ruta intr-e {orase[startPoint]} si {orase[stopPoint]}! :D")
                print(f"Intersectia rutelor reprezinta orasul : {orase[intersecting_node]}")
                self.print_path(intersecting_node,
                                startPoint, stopPoint)
                exit(0)
        return -1
class AdjacentNode:
    def __init__(self, vertex):
        self.vertex = vertex
        self.next = None

if __name__ == '__main__':
    n = 20 # numarul de orase
    startPoint = 0  # Orasul de start
    stopPoint = 19 # Orasul destinatie

   # 0Satu Mare   1Oradea   2Arad  3Timisoara  4Craiova  5Baia Mare  6Cluj Napoca  7Alba Iulia  8Bistrita  9Targu Mures
   # 10Sibiu  11Brasov  12Pitesti  13Suceava  14Iasi  15Piatra Neamt  16Bucuresti  17Braila  18Tulcea  19Constanta

    # lista noduri
    graph = BidirectionalSearch(n)
    graph.nod_intersectie(0, 1)
    graph.nod_intersectie(0, 5)
    graph.nod_intersectie(1, 2)
    graph.nod_intersectie(1, 6)
    graph.nod_intersectie(2, 6)
    graph.nod_intersectie(2, 3)
    graph.nod_intersectie(3, 4)
    graph.nod_intersectie(3, 7)
    graph.nod_intersectie(4, 12)
    graph.nod_intersectie(4, 7)
    graph.nod_intersectie(5, 6)
    graph.nod_intersectie(6, 8)
    graph.nod_intersectie(6, 9)
    graph.nod_intersectie(6, 7)
    graph.nod_intersectie(7, 10)
    graph.nod_intersectie(8, 9)
    graph.nod_intersectie(8, 13)
    graph.nod_intersectie(9, 10)
    graph.nod_intersectie(9, 11)
    graph.nod_intersectie(10, 11)
    graph.nod_intersectie(11, 12)
    graph.nod_intersectie(11, 16)
    graph.nod_intersectie(11, 15)
    graph.nod_intersectie(12, 16)
    graph.nod_intersectie(13, 14)
    graph.nod_intersectie(14, 15)
    graph.nod_intersectie(15, 17)
    graph.nod_intersectie(15, 16)
    graph.nod_intersectie(16, 17)
    graph.nod_intersectie(16, 19)
    graph.nod_intersectie(17, 18)
    graph.nod_intersectie(18, 19)

    solution = graph.bidirectional_search(startPoint, stopPoint)
    if solution == -1:
        print(f"Nu exista legatura intr-e {startPoint} si {stopPoint}")