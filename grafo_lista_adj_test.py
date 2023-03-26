import unittest
from meu_grafo_lista_adj import *
from bibgrafo.grafo_errors import *
from bibgrafo.aresta import Aresta


class TestGrafo(unittest.TestCase):

    def setUp(self):
        # Grafo da Paraíba
        self.g_p = MeuGrafo()
        self.g_p.adiciona_vertice("J")
        self.g_p.adiciona_vertice("C")
        self.g_p.adiciona_vertice("E")
        self.g_p.adiciona_vertice("P")
        self.g_p.adiciona_vertice("M")
        self.g_p.adiciona_vertice("T")
        self.g_p.adiciona_vertice("Z")
        self.g_p.adiciona_aresta('a1', 'J', 'C')
        self.g_p.adiciona_aresta('a2', 'C', 'E')
        self.g_p.adiciona_aresta('a3', 'C', 'E')
        self.g_p.adiciona_aresta('a4', 'P', 'C')
        self.g_p.adiciona_aresta('a5', 'P', 'C')
        self.g_p.adiciona_aresta('a6', 'T', 'C')
        self.g_p.adiciona_aresta('a7', 'M', 'C')
        self.g_p.adiciona_aresta('a8', 'M', 'T')
        self.g_p.adiciona_aresta('a9', 'T', 'Z')

        # Clone do Grafo da Paraíba para ver se o método equals está funcionando
        self.g_p2 = MeuGrafo()
        self.g_p2.adiciona_vertice("J")
        self.g_p2.adiciona_vertice("C")
        self.g_p2.adiciona_vertice("E")
        self.g_p2.adiciona_vertice("P")
        self.g_p2.adiciona_vertice("M")
        self.g_p2.adiciona_vertice("T")
        self.g_p2.adiciona_vertice("Z")
        self.g_p2.adiciona_aresta('a1', 'J', 'C')
        self.g_p2.adiciona_aresta('a2', 'C', 'E')
        self.g_p2.adiciona_aresta('a3', 'C', 'E')
        self.g_p2.adiciona_aresta('a4', 'P', 'C')
        self.g_p2.adiciona_aresta('a5', 'P', 'C')
        self.g_p2.adiciona_aresta('a6', 'T', 'C')
        self.g_p2.adiciona_aresta('a7', 'M', 'C')
        self.g_p2.adiciona_aresta('a8', 'M', 'T')
        self.g_p2.adiciona_aresta('a9', 'T', 'Z')

        # Outro clone do Grafo da Paraíba para ver se o método equals está funcionando
        # Esse tem um pequena diferença na primeira aresta
        self.g_p3 = MeuGrafo()
        self.g_p3.adiciona_vertice("J")
        self.g_p3.adiciona_vertice("C")
        self.g_p3.adiciona_vertice("E")
        self.g_p3.adiciona_vertice("P")
        self.g_p3.adiciona_vertice("M")
        self.g_p3.adiciona_vertice("T")
        self.g_p3.adiciona_vertice("Z")
        self.g_p3.adiciona_aresta('a', 'J', 'C')
        self.g_p3.adiciona_aresta('a2', 'C', 'E')
        self.g_p3.adiciona_aresta('a3', 'C', 'E')
        self.g_p3.adiciona_aresta('a4', 'P', 'C')
        self.g_p3.adiciona_aresta('a5', 'P', 'C')
        self.g_p3.adiciona_aresta('a6', 'T', 'C')
        self.g_p3.adiciona_aresta('a7', 'M', 'C')
        self.g_p3.adiciona_aresta('a8', 'M', 'T')
        self.g_p3.adiciona_aresta('a9', 'T', 'Z')

        # Outro clone do Grafo da Paraíba para ver se o método equals está funcionando
        # Esse tem um pequena diferença na segunda aresta
        self.g_p4 = MeuGrafo()
        self.g_p4.adiciona_vertice("J")
        self.g_p4.adiciona_vertice("C")
        self.g_p4.adiciona_vertice("E")
        self.g_p4.adiciona_vertice("P")
        self.g_p4.adiciona_vertice("M")
        self.g_p4.adiciona_vertice("T")
        self.g_p4.adiciona_vertice("Z")
        self.g_p4.adiciona_aresta('a1', 'J', 'C')
        self.g_p4.adiciona_aresta('a2', 'J', 'E')
        self.g_p4.adiciona_aresta('a3', 'C', 'E')
        self.g_p4.adiciona_aresta('a4', 'P', 'C')
        self.g_p4.adiciona_aresta('a5', 'P', 'C')
        self.g_p4.adiciona_aresta('a6', 'T', 'C')
        self.g_p4.adiciona_aresta('a7', 'M', 'C')
        self.g_p4.adiciona_aresta('a8', 'M', 'T')
        self.g_p4.adiciona_aresta('a9', 'T', 'Z')

        # Grafo da Paraíba sem arestas paralelas
        self.g_p_sem_paralelas = MeuGrafo()
        self.g_p_sem_paralelas.adiciona_vertice("J")
        self.g_p_sem_paralelas.adiciona_vertice("C")
        self.g_p_sem_paralelas.adiciona_vertice("E")
        self.g_p_sem_paralelas.adiciona_vertice("P")
        self.g_p_sem_paralelas.adiciona_vertice("M")
        self.g_p_sem_paralelas.adiciona_vertice("T")
        self.g_p_sem_paralelas.adiciona_vertice("Z")
        self.g_p_sem_paralelas.adiciona_aresta('a1', 'J', 'C')
        self.g_p_sem_paralelas.adiciona_aresta('a2', 'C', 'E')
        self.g_p_sem_paralelas.adiciona_aresta('a3', 'P', 'C')
        self.g_p_sem_paralelas.adiciona_aresta('a4', 'T', 'C')
        self.g_p_sem_paralelas.adiciona_aresta('a5', 'M', 'C')
        self.g_p_sem_paralelas.adiciona_aresta('a6', 'M', 'T')
        self.g_p_sem_paralelas.adiciona_aresta('a7', 'T', 'Z')

        # Grafos completos
        self.g_c = MeuGrafo()
        self.g_c.adiciona_vertice("J")
        self.g_c.adiciona_vertice("C")
        self.g_c.adiciona_vertice("E")
        self.g_c.adiciona_vertice("P")
        self.g_c.adiciona_aresta('a1', 'J', 'C')
        self.g_c.adiciona_aresta('a2', 'J', 'E')
        self.g_c.adiciona_aresta('a3', 'J', 'P')
        self.g_c.adiciona_aresta('a4', 'E', 'C')
        self.g_c.adiciona_aresta('a5', 'P', 'C')
        self.g_c.adiciona_aresta('a6', 'P', 'E')

        self.g_c2 = MeuGrafo()
        self.g_c2.adiciona_vertice("Nina")
        self.g_c2.adiciona_vertice("Maria")
        self.g_c2.adiciona_aresta('amiga', 'Nina', 'Maria')

        self.g_c3 = MeuGrafo()
        self.g_c3.adiciona_vertice("Único")

        # Grafos com laco
        self.g_l1 = MeuGrafo()
        self.g_l1.adiciona_vertice("A")
        self.g_l1.adiciona_vertice("B")
        self.g_l1.adiciona_vertice("C")
        self.g_l1.adiciona_vertice("D")
        self.g_l1.adiciona_aresta('a1', 'A', 'A')
        self.g_l1.adiciona_aresta('a2', 'A', 'B')
        self.g_l1.adiciona_aresta('a3', 'A', 'A')

        self.g_l2 = MeuGrafo()
        self.g_l2.adiciona_vertice("A")
        self.g_l2.adiciona_vertice("B")
        self.g_l2.adiciona_vertice("C")
        self.g_l2.adiciona_vertice("D")
        self.g_l2.adiciona_aresta('a1', 'A', 'B')
        self.g_l2.adiciona_aresta('a2', 'B', 'B')
        self.g_l2.adiciona_aresta('a3', 'B', 'A')

        self.g_l3 = MeuGrafo()
        self.g_l3.adiciona_vertice("A")
        self.g_l3.adiciona_vertice("B")
        self.g_l3.adiciona_vertice("C")
        self.g_l3.adiciona_vertice("D")
        self.g_l3.adiciona_aresta('a1', 'C', 'A')
        self.g_l3.adiciona_aresta('a2', 'C', 'C')
        self.g_l3.adiciona_aresta('a3', 'D', 'D')
        self.g_l3.adiciona_aresta('a4', 'D', 'D')

        self.g_l4 = MeuGrafo()
        self.g_l4.adiciona_vertice("D")
        self.g_l4.adiciona_aresta('a1', 'D', 'D')

        self.g_l5 = MeuGrafo()
        self.g_l5.adiciona_vertice("C")
        self.g_l5.adiciona_vertice("D")
        self.g_l5.adiciona_aresta('a1', 'D', 'C')
        self.g_l5.adiciona_aresta('a2', 'C', 'C')

        # Grafos desconexos
        self.g_d = MeuGrafo()
        self.g_d.adiciona_vertice("A")
        self.g_d.adiciona_vertice("B")
        self.g_d.adiciona_vertice("C")
        self.g_d.adiciona_vertice("D")
        self.g_d.adiciona_aresta('asd', 'A', 'B')

        self.g_d2 = MeuGrafo()
        self.g_d2.adiciona_vertice("A")
        self.g_d2.adiciona_vertice("B")
        self.g_d2.adiciona_vertice("C")
        self.g_d2.adiciona_vertice("D")

        # Grafos Dfs
        self.g_dfsSala = MeuGrafo()
        self.g_dfsSala.adiciona_vertice("K")
        self.g_dfsSala.adiciona_vertice("L")
        self.g_dfsSala.adiciona_vertice("M")
        self.g_dfsSala.adiciona_vertice("N")
        self.g_dfsSala.adiciona_vertice("COISA")
        self.g_dfsSala.adiciona_aresta("KCOISA", "K", "COISA")
        self.g_dfsSala.adiciona_aresta("KL", "K", "L")
        self.g_dfsSala.adiciona_aresta("lm", "L", "M")
        self.g_dfsSala.adiciona_aresta("a1", "K", "COISA")
        self.g_dfsSala.adiciona_aresta("a2", "N", "L")

        self.g_dfsSalaResolvido = MeuGrafo()
        self.g_dfsSalaResolvido.adiciona_vertice("K")
        self.g_dfsSalaResolvido.adiciona_vertice("L")
        self.g_dfsSalaResolvido.adiciona_vertice("M")
        self.g_dfsSalaResolvido.adiciona_vertice("N")
        self.g_dfsSalaResolvido.adiciona_vertice("COISA")
        self.g_dfsSalaResolvido.adiciona_aresta("KCOISA", "K", "COISA")
        self.g_dfsSalaResolvido.adiciona_aresta("KL", "K", "L")
        self.g_dfsSalaResolvido.adiciona_aresta("lm", "L", "M")
        self.g_dfsSalaResolvido.adiciona_aresta("a2", "N", "L")

        # esse grafo eu tirei do docs do roteiro dois que o professor passou
        self.g_grafoExemplo = MeuGrafo()
        self.g_grafoExemplo.adiciona_vertice("A")
        self.g_grafoExemplo.adiciona_vertice("B")
        self.g_grafoExemplo.adiciona_vertice("C")
        self.g_grafoExemplo.adiciona_vertice("D")
        self.g_grafoExemplo.adiciona_vertice("E")
        self.g_grafoExemplo.adiciona_vertice("F")
        self.g_grafoExemplo.adiciona_vertice("G")
        self.g_grafoExemplo.adiciona_vertice("H")
        self.g_grafoExemplo.adiciona_vertice("I")
        self.g_grafoExemplo.adiciona_vertice("J")
        self.g_grafoExemplo.adiciona_vertice("K")
        self.g_grafoExemplo.adiciona_aresta('1', 'A', 'B')
        self.g_grafoExemplo.adiciona_aresta('2', 'A', 'G')
        self.g_grafoExemplo.adiciona_aresta('3', 'A', 'J')
        self.g_grafoExemplo.adiciona_aresta('4', 'K', 'G')
        self.g_grafoExemplo.adiciona_aresta('5', 'K', 'J')
        self.g_grafoExemplo.adiciona_aresta('6', 'J', 'G')
        self.g_grafoExemplo.adiciona_aresta('7', 'J', 'I')
        self.g_grafoExemplo.adiciona_aresta('8', 'I', 'G')
        self.g_grafoExemplo.adiciona_aresta('9', 'G', 'H')
        self.g_grafoExemplo.adiciona_aresta('10', 'H', 'F')
        self.g_grafoExemplo.adiciona_aresta('11', 'F', 'B')
        self.g_grafoExemplo.adiciona_aresta('12', 'B', 'G')
        self.g_grafoExemplo.adiciona_aresta('13', 'B', 'C')
        self.g_grafoExemplo.adiciona_aresta('14', 'C', 'D')
        self.g_grafoExemplo.adiciona_aresta('15', 'D', 'E')
        self.g_grafoExemplo.adiciona_aresta('16', 'D', 'B')
        self.g_grafoExemplo.adiciona_aresta('17', 'E', 'B')

        self.g_grafoExemploResolvido = MeuGrafo()
        self.g_grafoExemploResolvido.adiciona_vertice("A")
        self.g_grafoExemploResolvido.adiciona_vertice("B")
        self.g_grafoExemploResolvido.adiciona_vertice("F")
        self.g_grafoExemploResolvido.adiciona_vertice("H")
        self.g_grafoExemploResolvido.adiciona_vertice("G")
        self.g_grafoExemploResolvido.adiciona_vertice("K")
        self.g_grafoExemploResolvido.adiciona_vertice("J")
        self.g_grafoExemploResolvido.adiciona_vertice("I")
        self.g_grafoExemploResolvido.adiciona_vertice("C")
        self.g_grafoExemploResolvido.adiciona_vertice("D")
        self.g_grafoExemploResolvido.adiciona_vertice("E")
        self.g_grafoExemploResolvido.adiciona_aresta("1", "A", "B")
        self.g_grafoExemploResolvido.adiciona_aresta("11", "F", "B")
        self.g_grafoExemploResolvido.adiciona_aresta("10", "H", "F")
        self.g_grafoExemploResolvido.adiciona_aresta("9", "G", "H")
        self.g_grafoExemploResolvido.adiciona_aresta("4", "K", "G")
        self.g_grafoExemploResolvido.adiciona_aresta("5", "K", "J")
        self.g_grafoExemploResolvido.adiciona_aresta("7", "J", "I")
        self.g_grafoExemploResolvido.adiciona_aresta("13", "B", "C")
        self.g_grafoExemploResolvido.adiciona_aresta("14", "C", "D")
        self.g_grafoExemploResolvido.adiciona_aresta("15", "D", "E")

        # grafo da paraiba já implementado só que dfs
        self.g_pDfs = MeuGrafo()
        self.g_pDfs.adiciona_vertice("J")
        self.g_pDfs.adiciona_vertice("C")
        self.g_pDfs.adiciona_vertice("E")
        self.g_pDfs.adiciona_vertice("P")
        self.g_pDfs.adiciona_vertice("M")
        self.g_pDfs.adiciona_vertice("T")
        self.g_pDfs.adiciona_vertice("Z")
        self.g_pDfs.adiciona_aresta("a1", "J", "C")
        self.g_pDfs.adiciona_aresta("a2", "C", "E")
        self.g_pDfs.adiciona_aresta("a4", "P", "C")
        self.g_pDfs.adiciona_aresta("a6", "T", "C")
        self.g_pDfs.adiciona_aresta("a8", "M", "T")
        self.g_pDfs.adiciona_aresta("a9", "T", "Z")

        # grafo paraiba4 já implementado só que dfs
        self.g_p4Dfs = MeuGrafo()
        self.g_p4Dfs.adiciona_vertice("J")
        self.g_p4Dfs.adiciona_vertice("C")
        self.g_p4Dfs.adiciona_vertice("E")
        self.g_p4Dfs.adiciona_vertice("P")
        self.g_p4Dfs.adiciona_vertice("M")
        self.g_p4Dfs.adiciona_vertice("T")
        self.g_p4Dfs.adiciona_vertice("Z")
        self.g_p4Dfs.adiciona_aresta('a1', 'J', 'C')
        self.g_p4Dfs.adiciona_aresta('a3', 'C', 'E')
        self.g_p4Dfs.adiciona_aresta('a4', 'P', 'C')
        self.g_p4Dfs.adiciona_aresta('a6', 'T', 'C')
        self.g_p4Dfs.adiciona_aresta('a8', 'M', 'T')
        self.g_p4Dfs.adiciona_aresta('a9', 'T', 'Z')

        # grafo completo já implementado só que dfs
        self.g_cDfs = MeuGrafo()
        self.g_cDfs.adiciona_vertice("J")
        self.g_cDfs.adiciona_vertice("C")
        self.g_cDfs.adiciona_vertice("E")
        self.g_cDfs.adiciona_vertice("P")
        self.g_cDfs.adiciona_aresta('a1', 'J', 'C')
        self.g_cDfs.adiciona_aresta('a4', 'E', 'C')
        self.g_cDfs.adiciona_aresta('a6', 'P', 'E')

        self.g_c2Dfs = MeuGrafo()
        self.g_c2Dfs.adiciona_vertice("Nina")
        self.g_c2Dfs.adiciona_vertice("Maria")
        self.g_c2Dfs.adiciona_aresta('amiga', 'Nina', 'Maria')

        # grafo com laços já implementados só que dfs
        self.g_l3Dfs = MeuGrafo()
        self.g_l3Dfs.adiciona_vertice("A")
        self.g_l3Dfs.adiciona_vertice("C")
        self.g_l3Dfs.adiciona_aresta('a1', 'C', 'A')

        self.g_l2Dfs = MeuGrafo()
        self.g_l2Dfs.adiciona_vertice("A")
        self.g_l2Dfs.adiciona_vertice("B")
        self.g_l2Dfs.adiciona_aresta('a1', 'A', 'B')

        # Grafo Bfs
        self.g_pBfs = MeuGrafo()
        self.g_pBfs.adiciona_vertice("J")
        self.g_pBfs.adiciona_vertice("C")
        self.g_pBfs.adiciona_vertice("E")
        self.g_pBfs.adiciona_vertice("P")
        self.g_pBfs.adiciona_vertice("M")
        self.g_pBfs.adiciona_vertice("T")
        self.g_pBfs.adiciona_vertice("Z")
        self.g_pBfs.adiciona_aresta('a1', 'J', 'C')
        self.g_pBfs.adiciona_aresta('a2', 'C', 'E')
        self.g_pBfs.adiciona_aresta('a4', 'P', 'C')
        self.g_pBfs.adiciona_aresta('a6', 'T', 'C')
        self.g_pBfs.adiciona_aresta('a7', 'M', 'C')
        self.g_pBfs.adiciona_aresta('a9', 'T', 'Z')

        self.g_p4Bfs = MeuGrafo()
        self.g_p4Bfs.adiciona_vertice("J")
        self.g_p4Bfs.adiciona_vertice("C")
        self.g_p4Bfs.adiciona_vertice("E")
        self.g_p4Bfs.adiciona_vertice("P")
        self.g_p4Bfs.adiciona_vertice("M")
        self.g_p4Bfs.adiciona_vertice("T")
        self.g_p4Bfs.adiciona_vertice("Z")
        self.g_p4Bfs.adiciona_aresta('a1', 'J', 'C')
        self.g_p4Bfs.adiciona_aresta('a2', 'J', 'E')
        self.g_p4Bfs.adiciona_aresta('a4', 'P', 'C')
        self.g_p4Bfs.adiciona_aresta('a6', 'T', 'C')
        self.g_p4Bfs.adiciona_aresta('a7', 'M', 'C')
        self.g_p4Bfs.adiciona_aresta('a9', 'T', 'Z')

        self.g_SalaResolvidoBfs = MeuGrafo()
        self.g_SalaResolvidoBfs.adiciona_vertice("K")
        self.g_SalaResolvidoBfs.adiciona_vertice("L")
        self.g_SalaResolvidoBfs.adiciona_vertice("M")
        self.g_SalaResolvidoBfs.adiciona_vertice("N")
        self.g_SalaResolvidoBfs.adiciona_vertice("COISA")
        self.g_SalaResolvidoBfs.adiciona_aresta("KCOISA", "K", "COISA")
        self.g_SalaResolvidoBfs.adiciona_aresta("KL", "K", "L")
        self.g_SalaResolvidoBfs.adiciona_aresta("lm", "L", "M")
        self.g_SalaResolvidoBfs.adiciona_aresta("a2", "N", "L")

        self.g_BfsSala = MeuGrafo()
        self.g_BfsSala.adiciona_vertice("K")
        self.g_BfsSala.adiciona_vertice("L")
        self.g_BfsSala.adiciona_vertice("M")
        self.g_BfsSala.adiciona_vertice("N")
        self.g_BfsSala.adiciona_vertice("COISA")
        self.g_BfsSala.adiciona_aresta("KCOISA", "K", "COISA")
        self.g_BfsSala.adiciona_aresta("KL", "K", "L")
        self.g_BfsSala.adiciona_aresta("lm", "L", "M")
        self.g_BfsSala.adiciona_aresta("a1", "K", "COISA")
        self.g_BfsSala.adiciona_aresta("a2", "N", "L")

        self.g_grafoExemploResolvidoBfs = MeuGrafo()
        self.g_grafoExemploResolvidoBfs.adiciona_vertice("A")
        self.g_grafoExemploResolvidoBfs.adiciona_vertice("B")
        self.g_grafoExemploResolvidoBfs.adiciona_vertice("F")
        self.g_grafoExemploResolvidoBfs.adiciona_vertice("H")
        self.g_grafoExemploResolvidoBfs.adiciona_vertice("G")
        self.g_grafoExemploResolvidoBfs.adiciona_vertice("K")
        self.g_grafoExemploResolvidoBfs.adiciona_vertice("J")
        self.g_grafoExemploResolvidoBfs.adiciona_vertice("I")
        self.g_grafoExemploResolvidoBfs.adiciona_vertice("C")
        self.g_grafoExemploResolvidoBfs.adiciona_vertice("D")
        self.g_grafoExemploResolvidoBfs.adiciona_vertice("E")
        self.g_grafoExemploResolvidoBfs.adiciona_aresta('1', 'A', 'B')
        self.g_grafoExemploResolvidoBfs.adiciona_aresta('2', 'A', 'G')
        self.g_grafoExemploResolvidoBfs.adiciona_aresta('3', 'A', 'J')
        self.g_grafoExemploResolvidoBfs.adiciona_aresta('11', 'F', 'B')
        self.g_grafoExemploResolvidoBfs.adiciona_aresta('13', 'B', 'C')
        self.g_grafoExemploResolvidoBfs.adiciona_aresta('16', 'D', 'B')
        self.g_grafoExemploResolvidoBfs.adiciona_aresta('17', 'E', 'B')
        self.g_grafoExemploResolvidoBfs.adiciona_aresta('4', 'K', 'G')
        self.g_grafoExemploResolvidoBfs.adiciona_aresta('8', 'I', 'G')
        self.g_grafoExemploResolvidoBfs.adiciona_aresta('9', 'G', 'H')

        self.g_cBfs = MeuGrafo()
        self.g_cBfs.adiciona_vertice("J")
        self.g_cBfs.adiciona_vertice("C")
        self.g_cBfs.adiciona_vertice("E")
        self.g_cBfs.adiciona_vertice("P")
        self.g_cBfs.adiciona_aresta('a1', 'J', 'C')
        self.g_cBfs.adiciona_aresta('a2', 'J', 'E')
        self.g_cBfs.adiciona_aresta('a3', 'J', 'P')

        self.g_c2Bfs = MeuGrafo()
        self.g_c2Bfs.adiciona_vertice("Nina")
        self.g_c2Bfs.adiciona_vertice("Maria")
        self.g_c2Bfs.adiciona_aresta('amiga', 'Nina', 'Maria')

        self.g_l3Bfs = MeuGrafo()
        self.g_l3Bfs.adiciona_vertice("A")
        self.g_l3Bfs.adiciona_vertice("C")
        self.g_l3Bfs.adiciona_aresta('a1', 'C', 'A')

        self.g_l2Bfs = MeuGrafo()
        self.g_l2Bfs.adiciona_vertice("A")
        self.g_l2Bfs.adiciona_vertice("B")
        self.g_l2Bfs.adiciona_aresta('a1', 'A', 'B')

    def test_adiciona_aresta(self):
        self.assertTrue(self.g_p.adiciona_aresta('a10', 'J', 'C'))
        a = Aresta("zxc", self.g_p.get_vertice("C"), self.g_p.get_vertice("Z"))
        self.assertTrue(self.g_p.adiciona_aresta(a))
        with self.assertRaises(ArestaInvalidaError):
            self.assertTrue(self.g_p.adiciona_aresta(a))
        with self.assertRaises(VerticeInvalidoError):
            self.assertTrue(self.g_p.adiciona_aresta('b1', '', 'C'))
        with self.assertRaises(VerticeInvalidoError):
            self.assertTrue(self.g_p.adiciona_aresta('b1', 'A', 'C'))
        with self.assertRaises(NotImplementedError):
            self.g_p.adiciona_aresta('')
        with self.assertRaises(NotImplementedError):
            self.g_p.adiciona_aresta('aa-bb')
        with self.assertRaises(VerticeInvalidoError):
            self.g_p.adiciona_aresta('x', 'J', 'V')
        with self.assertRaises(ArestaInvalidaError):
            self.g_p.adiciona_aresta('a1', 'J', 'C')

    def test_eq(self):
        self.assertEqual(self.g_p, self.g_p2)
        self.assertNotEqual(self.g_p, self.g_p3)
        self.assertNotEqual(self.g_p, self.g_p_sem_paralelas)
        self.assertNotEqual(self.g_p, self.g_p4)

    def test_vertices_nao_adjacentes(self):
        self.assertEqual(self.g_p.vertices_nao_adjacentes(),
                         {'J-E', 'J-P', 'J-M', 'J-T', 'J-Z', 'C-Z', 'E-P', 'E-M', 'E-T', 'E-Z', 'P-M', 'P-T', 'P-Z',
                          'M-Z'})
        self.assertEqual(self.g_d.vertices_nao_adjacentes(), {'A-C', 'A-D', 'B-C', 'B-D', 'C-D'})
        self.assertEqual(self.g_d2.vertices_nao_adjacentes(), {'A-B', 'A-C', 'A-D', 'B-C', 'B-D', 'C-D'})
        self.assertEqual(self.g_c.vertices_nao_adjacentes(), set())
        self.assertEqual(self.g_c3.vertices_nao_adjacentes(), set())

    def test_ha_laco(self):
        self.assertFalse(self.g_p.ha_laco())
        self.assertFalse(self.g_p2.ha_laco())
        self.assertFalse(self.g_p3.ha_laco())
        self.assertFalse(self.g_p4.ha_laco())
        self.assertFalse(self.g_p_sem_paralelas.ha_laco())
        self.assertFalse(self.g_d.ha_laco())
        self.assertFalse(self.g_c.ha_laco())
        self.assertFalse(self.g_c2.ha_laco())
        self.assertFalse(self.g_c3.ha_laco())
        self.assertTrue(self.g_l1.ha_laco())
        self.assertTrue(self.g_l2.ha_laco())
        self.assertTrue(self.g_l3.ha_laco())
        self.assertTrue(self.g_l4.ha_laco())
        self.assertTrue(self.g_l5.ha_laco())

    def test_grau(self):
        # Paraíba
        self.assertEqual(self.g_p.grau('J'), 1)
        self.assertEqual(self.g_p.grau('C'), 7)
        self.assertEqual(self.g_p.grau('E'), 2)
        self.assertEqual(self.g_p.grau('P'), 2)
        self.assertEqual(self.g_p.grau('M'), 2)
        self.assertEqual(self.g_p.grau('T'), 3)
        self.assertEqual(self.g_p.grau('Z'), 1)
        with self.assertRaises(VerticeInvalidoError):
            self.assertEqual(self.g_p.grau('G'), 5)

        self.assertEqual(self.g_d.grau('A'), 1)
        self.assertEqual(self.g_d.grau('C'), 0)
        self.assertNotEqual(self.g_d.grau('D'), 2)
        self.assertEqual(self.g_d2.grau('A'), 0)

        # Completos
        self.assertEqual(self.g_c.grau('J'), 3)
        self.assertEqual(self.g_c.grau('C'), 3)
        self.assertEqual(self.g_c.grau('E'), 3)
        self.assertEqual(self.g_c.grau('P'), 3)

        # Com laço. Lembrando que cada laço conta 2 vezes por vértice para cálculo do grau
        self.assertEqual(self.g_l1.grau('A'), 5)
        self.assertEqual(self.g_l2.grau('B'), 4)
        self.assertEqual(self.g_l4.grau('D'), 2)

    def test_ha_paralelas(self):
        self.assertTrue(self.g_p.ha_paralelas())
        self.assertFalse(self.g_p_sem_paralelas.ha_paralelas())
        self.assertFalse(self.g_c.ha_paralelas())
        self.assertFalse(self.g_c2.ha_paralelas())
        self.assertFalse(self.g_c3.ha_paralelas())
        self.assertTrue(self.g_l1.ha_paralelas())

    def test_arestas_sobre_vertice(self):
        self.assertEqual(self.g_p.arestas_sobre_vertice('J'), {'a1'})
        self.assertEqual(self.g_p.arestas_sobre_vertice('C'), {'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7'})
        self.assertEqual(self.g_p.arestas_sobre_vertice('M'), {'a7', 'a8'})
        self.assertEqual(self.g_l2.arestas_sobre_vertice('B'), {'a1', 'a2', 'a3'})
        self.assertEqual(self.g_d.arestas_sobre_vertice('C'), set())
        self.assertEqual(self.g_d.arestas_sobre_vertice('A'), {'asd'})
        with self.assertRaises(VerticeInvalidoError):
            self.g_p.arestas_sobre_vertice('A')

    def test_eh_completo(self):
        self.assertFalse(self.g_p.eh_completo())
        self.assertFalse((self.g_p_sem_paralelas.eh_completo()))
        self.assertTrue((self.g_c.eh_completo()))
        self.assertTrue((self.g_c2.eh_completo()))
        self.assertTrue((self.g_c3.eh_completo()))
        self.assertFalse((self.g_l1.eh_completo()))
        self.assertFalse((self.g_l2.eh_completo()))
        self.assertFalse((self.g_l3.eh_completo()))
        self.assertFalse((self.g_l4.eh_completo()))
        self.assertFalse((self.g_l5.eh_completo()))
        self.assertFalse((self.g_d.eh_completo()))
        self.assertFalse((self.g_d2.eh_completo()))

    def test_dfs(self):
        # grafo passado no quadro da sala
        self.assertEqual(self.g_dfsSala.dfs(), self.g_dfsSalaResolvido)

        # grafo passado no docs do roteiro como exemplo
        self.assertEqual(self.g_grafoExemplo.dfs(), self.g_grafoExemploResolvido)

        # grafo da paraiba já implementado
        self.assertEqual(self.g_p.dfs(), self.g_pDfs)
        self.assertEqual(self.g_p4.dfs(), self.g_p4Dfs)

        # grafo completo já implementado
        self.assertEqual(self.g_c.dfs(), self.g_cDfs)
        self.assertEqual(self.g_c2.dfs(), self.g_c2Dfs)

        # grafo com laço já implementado
        self.assertEqual(self.g_l3.dfs(), self.g_l3Dfs)
        self.assertEqual(self.g_l2.dfs(), self.g_l2Dfs)

    def test_bfs(self):
        # grafo passado no quadro da sala
        self.assertEqual(self.g_BfsSala.dfs(), self.g_SalaResolvidoBfs)

        # grafo passado no docs do roteiro como exemplo
        self.assertEqual(self.g_grafoExemplo.bfs(), self.g_grafoExemploResolvidoBfs)

        # grafo da paraiba já implementado
        self.assertEqual(self.g_p.bfs(), self.g_pBfs)
        self.assertEqual(self.g_p4.bfs(), self.g_p4Bfs)

        # grafo completo já implementado
        self.assertEqual(self.g_c.bfs(), self.g_cBfs)
        self.assertEqual(self.g_c2.dfs(), self.g_c2Bfs)

        # grafo com laço já implementado
        self.assertEqual(self.g_l3.bfs(), self.g_l3Bfs)
        self.assertEqual(self.g_l2.bfs(), self.g_l2Bfs)


