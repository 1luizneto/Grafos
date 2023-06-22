import unittest
from meu_grafo_matriz_adj_dir import *
from bibgrafo.grafo_errors import *


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
        self.g_p2 = MeuGrafo([Vertice('J'),
                              Vertice('C'),
                              Vertice('E'),
                              Vertice('P'),
                              Vertice('M'),
                              Vertice('T'),
                              Vertice('Z')])
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

        # Grafo com ciclos e laços
        self.g_e = MeuGrafo()
        self.g_e.adiciona_vertice("A")
        self.g_e.adiciona_vertice("B")
        self.g_e.adiciona_vertice("C")
        self.g_e.adiciona_vertice("D")
        self.g_e.adiciona_vertice("E")
        self.g_e.adiciona_aresta('1', 'A', 'B')
        self.g_e.adiciona_aresta('2', 'A', 'C')
        self.g_e.adiciona_aresta('3', 'C', 'A')
        self.g_e.adiciona_aresta('4', 'C', 'B')
        self.g_e.adiciona_aresta('10', 'C', 'B')
        self.g_e.adiciona_aresta('5', 'C', 'D')
        self.g_e.adiciona_aresta('6', 'D', 'D')
        self.g_e.adiciona_aresta('7', 'D', 'B')
        self.g_e.adiciona_aresta('8', 'D', 'E')
        self.g_e.adiciona_aresta('9', 'E', 'A')
        self.g_e.adiciona_aresta('11', 'E', 'B')

        # Matrizes para teste do algoritmo de Warshall

        self.g_p_m = self.constroi_matriz(self.g_p)
        self.g_p_m[0][1] = 1
        self.g_p_m[0][2] = 1
        self.g_p_m[1][2] = 1
        self.g_p_m[3][1] = 1
        self.g_p_m[3][2] = 1
        self.g_p_m[4][1] = 1
        self.g_p_m[4][2] = 1
        self.g_p_m[4][5] = 1
        self.g_p_m[4][6] = 1
        self.g_p_m[5][1] = 1
        self.g_p_m[5][2] = 1
        self.g_p_m[5][6] = 1

        self.g_e_m = self.constroi_matriz(self.g_e)
        for i in range(0, len(self.g_e_m)):
            self.g_e_m[0][i] = 1
            self.g_e_m[2][i] = 1
            self.g_e_m[3][i] = 1
            self.g_e_m[4][i] = 1

            # grafos warshall
            self.g_w1 = MeuGrafo()
            self.g_w1.adiciona_vertice("A")
            self.g_w1.adiciona_vertice("B")
            self.g_w1.adiciona_vertice("C")
            self.g_w1.adiciona_vertice("D")
            self.g_w1.adiciona_aresta('a1', 'A', 'B')
            self.g_w1.adiciona_aresta('a2', 'A', 'C')
            self.g_w1.adiciona_aresta('a3', 'B', 'D')
            self.g_w1.adiciona_aresta('a2', 'C', 'D')

            self.g_w2 = MeuGrafo()
            self.g_w2.adiciona_vertice('A')
            self.g_w2.adiciona_vertice('B')
            self.g_w2.adiciona_vertice('C')
            self.g_w2.adiciona_vertice('D')
            self.g_w2.adiciona_aresta('a1', 'A', 'B')
            self.g_w2.adiciona_aresta('a2', 'A', 'C')
            self.g_w2.adiciona_aresta('a3', 'B', 'D')
            self.g_w2.adiciona_aresta('a4', 'C', 'D')
            self.g_w2.adiciona_aresta('a5', 'A', 'D')
            self.g_w2.adiciona_aresta('a6', 'C', 'B')

            self.g_w3 = MeuGrafo()
            self.g_w3.adiciona_vertice('A')
            self.g_w3.adiciona_vertice('B')
            self.g_w3.adiciona_vertice('C')
            self.g_w3.adiciona_vertice('D')
            self.g_w3.adiciona_vertice('E')
            self.g_w3.adiciona_vertice('F')
            self.g_w3.adiciona_aresta('a1', 'A', 'B')
            self.g_w3.adiciona_aresta('a2', 'A', 'C')
            self.g_w3.adiciona_aresta('a3', 'C', 'D')
            self.g_w3.adiciona_aresta('a4', 'B', 'D')
            self.g_w3.adiciona_aresta('a5', 'C', 'F')
            self.g_w3.adiciona_aresta('a6', 'D', 'E')
            self.g_w3.adiciona_aresta('a7', 'E', 'F')

            self.g_w4 = MeuGrafo()
            self.g_w4.adiciona_vertice("A")
            self.g_w4.adiciona_vertice("B")
            self.g_w4.adiciona_vertice("C")
            self.g_w4.adiciona_vertice("D")
            self.g_w4.adiciona_vertice("E")
            self.g_w4.adiciona_vertice("F")
            self.g_w4.adiciona_aresta('a1', 'A', 'B')
            self.g_w4.adiciona_aresta('a2', 'B', 'C')
            self.g_w4.adiciona_aresta('a3', 'C', 'B')
            self.g_w4.adiciona_aresta('a4', 'B', 'D')
            self.g_w4.adiciona_aresta('a5', 'D', 'C')
            self.g_w4.adiciona_aresta('a6', 'B', 'F')
            self.g_w4.adiciona_aresta('a7', 'B', 'E')
            self.g_w4.adiciona_aresta('a8', 'E', 'F')

            # Matrizes para teste do algoritmo de Warshall

            self.g_w1_m = self.constroi_matriz(self.g_w1)
            self.g_w1_m[0][0] = 0
            self.g_w1_m[0][1] = 1
            self.g_w1_m[0][2] = 1
            self.g_w1_m[0][3] = 1

            self.g_w1_m[1][0] = 0
            self.g_w1_m[1][1] = 0
            self.g_w1_m[1][2] = 0
            self.g_w1_m[1][3] = 1

            self.g_w1_m[2][0] = 0
            self.g_w1_m[2][1] = 0
            self.g_w1_m[2][2] = 0
            self.g_w1_m[2][3] = 1

            self.g_w1_m[3][0] = 0
            self.g_w1_m[3][1] = 0
            self.g_w1_m[3][2] = 0
            self.g_w1_m[3][3] = 0

            self.g_w2_m = self.constroi_matriz(self.g_w2)
            self.g_w2_m[0][0] = 0
            self.g_w2_m[0][1] = 1
            self.g_w2_m[0][2] = 1
            self.g_w2_m[0][3] = 1

            self.g_w2_m[1][0] = 0
            self.g_w2_m[1][1] = 0
            self.g_w2_m[1][2] = 0
            self.g_w2_m[1][3] = 1

            self.g_w2_m[2][0] = 0
            self.g_w2_m[2][1] = 1
            self.g_w2_m[2][2] = 0
            self.g_w2_m[2][3] = 1

            self.g_w2_m[3][0] = 0
            self.g_w2_m[3][1] = 0
            self.g_w2_m[3][2] = 0
            self.g_w2_m[3][3] = 0

            self.g_w3_m = self.constroi_matriz(self.g_w3)
            self.g_w3_m[0][0] = 0
            self.g_w3_m[0][1] = 1
            self.g_w3_m[0][2] = 1
            self.g_w3_m[0][3] = 1
            self.g_w3_m[0][4] = 1
            self.g_w3_m[0][5] = 1

            self.g_w3_m[1][0] = 0
            self.g_w3_m[1][1] = 0
            self.g_w3_m[1][2] = 0
            self.g_w3_m[1][3] = 1
            self.g_w3_m[1][4] = 1
            self.g_w3_m[1][5] = 1

            self.g_w3_m[2][0] = 0
            self.g_w3_m[2][1] = 0
            self.g_w3_m[2][2] = 0
            self.g_w3_m[2][3] = 1
            self.g_w3_m[2][4] = 1
            self.g_w3_m[2][5] = 1

            self.g_w3_m[3][0] = 0
            self.g_w3_m[3][1] = 0
            self.g_w3_m[3][2] = 0
            self.g_w3_m[3][3] = 0
            self.g_w3_m[3][4] = 1
            self.g_w3_m[3][5] = 1

            self.g_w3_m[4][0] = 0
            self.g_w3_m[4][1] = 0
            self.g_w3_m[4][2] = 0
            self.g_w3_m[4][3] = 0
            self.g_w3_m[4][4] = 0
            self.g_w3_m[4][5] = 1

            self.g_w3_m[5][0] = 0
            self.g_w3_m[5][1] = 0
            self.g_w3_m[5][2] = 0
            self.g_w3_m[5][3] = 0
            self.g_w3_m[5][4] = 0
            self.g_w3_m[5][5] = 0

            self.g_w4_m = self.constroi_matriz(self.g_w4)
            self.g_w4_m[0][0] = 0
            self.g_w4_m[0][1] = 1
            self.g_w4_m[0][2] = 1
            self.g_w4_m[0][3] = 1
            self.g_w4_m[0][4] = 1
            self.g_w4_m[0][5] = 1

            self.g_w4_m[1][0] = 0
            self.g_w4_m[1][1] = 1
            self.g_w4_m[1][2] = 1
            self.g_w4_m[1][3] = 1
            self.g_w4_m[1][4] = 1
            self.g_w4_m[1][5] = 1

            self.g_w4_m[2][0] = 0
            self.g_w4_m[2][1] = 1
            self.g_w4_m[2][2] = 1
            self.g_w4_m[2][3] = 1
            self.g_w4_m[2][4] = 1
            self.g_w4_m[2][5] = 1

            self.g_w4_m[3][0] = 0
            self.g_w4_m[3][1] = 1
            self.g_w4_m[3][2] = 1
            self.g_w4_m[3][3] = 1
            self.g_w4_m[3][4] = 1
            self.g_w4_m[3][5] = 1

            self.g_w4_m[4][0] = 0
            self.g_w4_m[4][1] = 0
            self.g_w4_m[4][2] = 0
            self.g_w4_m[4][3] = 0
            self.g_w4_m[4][4] = 0
            self.g_w4_m[4][5] = 1

            self.g_w4_m[5][0] = 0
            self.g_w4_m[5][1] = 0
            self.g_w4_m[5][2] = 0
            self.g_w4_m[5][3] = 0
            self.g_w4_m[5][4] = 0
            self.g_w4_m[5][5] = 0

        # Grafos desconexos
        self.g_dijkstra = MeuGrafo()
        self.g_dijkstra.adiciona_vertice("A")
        self.g_dijkstra.adiciona_vertice("B")
        self.g_dijkstra.adiciona_vertice("C")
        self.g_dijkstra.adiciona_vertice("D")
        self.g_dijkstra.adiciona_aresta('l1', 'A', 'B', 1)
        self.g_dijkstra.adiciona_aresta('l2', 'A', 'C', 1)
        self.g_dijkstra.adiciona_aresta('l3', 'B', 'D', 1)
        self.g_dijkstra.adiciona_aresta('l4', 'C', 'D', 2)
        # caminho mais leve tem mais arestas
        self.g_dijkstra2 = MeuGrafo()
        self.g_dijkstra2.adiciona_vertice('A')
        self.g_dijkstra2.adiciona_vertice('B')
        self.g_dijkstra2.adiciona_vertice('C')
        self.g_dijkstra2.adiciona_vertice('D')
        self.g_dijkstra2.adiciona_vertice('E')
        self.g_dijkstra2.adiciona_vertice('F')
        self.g_dijkstra2.adiciona_vertice('G')
        self.g_dijkstra2.adiciona_aresta('l1', 'A', 'B', 2)
        self.g_dijkstra2.adiciona_aresta('l2', 'B', 'C', 3)
        self.g_dijkstra2.adiciona_aresta('l3', 'A', 'D', 1)
        self.g_dijkstra2.adiciona_aresta('l4', 'D', 'C', 2)
        self.g_dijkstra2.adiciona_aresta('l9', 'A', 'C', 7)
        self.g_dijkstra2.adiciona_aresta('l5', 'C', 'E', 1)
        self.g_dijkstra2.adiciona_aresta('l6', 'E', 'G', 2)
        self.g_dijkstra2.adiciona_aresta('l7', 'G', 'F', 3)
        self.g_dijkstra2.adiciona_aresta('l8', 'C', 'F', 8)

        # Grafos para o Algoritmo de Khan
        self.eng_comp = MeuGrafo()
        self.eng_comp.adiciona_vertice('Pré-Cálculo')
        self.eng_comp.adiciona_vertice('Inglês Instrumental')
        self.eng_comp.adiciona_vertice('Introdução à Engenharia de Computação')
        self.eng_comp.adiciona_vertice('Algoritmos e Programação')
        self.eng_comp.adiciona_vertice('Lab. de Algoritmos e Programação')
        self.eng_comp.adiciona_vertice('Sistemas Digitais I')
        self.eng_comp.adiciona_vertice('Medição Eletro-eletrônica')
        self.eng_comp.adiciona_vertice('Cálculo I')
        self.eng_comp.adiciona_vertice('Estatística Aplicada à Computação')
        self.eng_comp.adiciona_vertice('Leitura e Produção de Textos')
        self.eng_comp.adiciona_vertice('Estruturas de Dados e Algoritmos')
        self.eng_comp.adiciona_vertice('Laboratório de Estruturas de Dados e Algoritmos')
        self.eng_comp.adiciona_vertice('Sistemas Digitais II')
        self.eng_comp.adiciona_vertice('Educação Ambiental e Sustentabilidade')
        self.eng_comp.adiciona_vertice('Cálculo II')
        self.eng_comp.adiciona_vertice('Relações Humanas no Trabalho')
        self.eng_comp.adiciona_vertice('Teoria dos Grafos')
        self.eng_comp.adiciona_vertice('Programação Orientada a Objetos')
        self.eng_comp.adiciona_vertice('Laboratório de Programação Orientada a Objetos')
        self.eng_comp.adiciona_vertice('Organização e Arquitetura de Computadores')
        self.eng_comp.adiciona_vertice('Física Clássica')
        self.eng_comp.adiciona_vertice('Metodologia da Pesquisa Científica')
        self.eng_comp.adiciona_vertice('Teoria da Computação')
        self.eng_comp.adiciona_vertice('Sistemas Operacionais')
        self.eng_comp.adiciona_vertice('Microprocessadores e Microcontroladores')
        self.eng_comp.adiciona_vertice('Álgebra Linear Aplicada à Computação')
        self.eng_comp.adiciona_vertice('Eletricidade e Eletromagnetismo')
        self.eng_comp.adiciona_vertice('Redes de Computadore')
        self.eng_comp.adiciona_vertice('Bancos de Dados')
        self.eng_comp.adiciona_vertice('Projeto de Sistemas Digitais')
        self.eng_comp.adiciona_vertice('Métodos Numéricos')
        self.eng_comp.adiciona_vertice('Inteligência Artificial')
        self.eng_comp.adiciona_vertice('Padrões de Projetos')
        self.eng_comp.adiciona_vertice('Sinais e Sistemas')
        self.eng_comp.adiciona_vertice('Verificação Funcional de Sistemas Digitais')
        self.eng_comp.adiciona_vertice('Libras')
        self.eng_comp.adiciona_vertice('Análise e Técnicas de Algoritmos')
        self.eng_comp.adiciona_vertice('Análise e Projeto de Sistemas')
        self.eng_comp.adiciona_vertice('Desenho Assistido por Computador')
        self.eng_comp.adiciona_vertice('Circuitos Eletro-Eletrônicos')
        self.eng_comp.adiciona_vertice('Teste de Software')
        self.eng_comp.adiciona_vertice('Gerência de Projetos')
        self.eng_comp.adiciona_vertice('Técnicas de Prototipagem')
        self.eng_comp.adiciona_vertice('Processamento Digital de Sinais')
        self.eng_comp.adiciona_vertice('Sensores e Atuadores')
        self.eng_comp.adiciona_vertice('Empreendedorismo de Base Tecnológica')
        self.eng_comp.adiciona_vertice('Projeto em Engenharia de Computação I')
        self.eng_comp.adiciona_vertice('Sistemas Embarcados')
        self.eng_comp.adiciona_vertice('Controle e Automação I')
        self.eng_comp.adiciona_vertice('Educação em Direitos Humanos')
        self.eng_comp.adiciona_vertice('Educação em Diversidade')
        self.eng_comp.adiciona_vertice('Projeto em Engenharia de Computação II')

        self.eng_comp.adiciona_aresta("a1", "Pré-Cálculo", "Cálculo I")
        self.eng_comp.adiciona_aresta("a2", "Algoritmos e Programação", "Estruturas de Dados e Algoritmos")
        self.eng_comp.adiciona_aresta("a3", "Lab. de Algoritmos e Programação", "Estruturas de Dados e Algoritmos")
        self.eng_comp.adiciona_aresta("a4", "Algoritmos e Programação",
                                      "Laboratório de Estruturas de Dados e Algoritmos")
        self.eng_comp.adiciona_aresta("a5", "Lab. de Algoritmos e Programação",
                                      "Laboratório de Estruturas de Dados e Algoritmos")
        self.eng_comp.adiciona_aresta("a6", "Sistemas Digitais I", "Sistemas Digitais II")
        self.eng_comp.adiciona_aresta("a7", "Cálculo I", "Cálculo II")
        self.eng_comp.adiciona_aresta("a8", "Estruturas de Dados e Algoritmos", "Teoria dos Grafos")
        self.eng_comp.adiciona_aresta("a9", "Algoritmos e Programação", "Programação Orientada a Objetos")
        self.eng_comp.adiciona_aresta("a10", "Lab. de Algoritmos e Programação", "Programação Orientada a Objetos")
        self.eng_comp.adiciona_aresta("a11", "Algoritmos e Programação",
                                      "Laboratório de Programação Orientada a Objetos")
        self.eng_comp.adiciona_aresta("a12", "Lab. de Algoritmos e Programação",
                                      "Laboratório de Programação Orientada a Objetos")
        self.eng_comp.adiciona_aresta("a13", "Sistemas Digitais II", "Organização e Arquitetura de Computadores")
        self.eng_comp.adiciona_aresta("a14", "Cálculo I", "Física Clássica")
        self.eng_comp.adiciona_aresta("a15", "Estruturas de Dados e Algoritmos", "Teoria da Computação")
        self.eng_comp.adiciona_aresta("a16", "Estruturas de Dados e Algoritmos", "Sistemas Operacionais")
        self.eng_comp.adiciona_aresta("a17", "Organização e Arquitetura de Computadores", "Sistemas Operacionais")
        self.eng_comp.adiciona_aresta("a18", "Organização e Arquitetura de Computadores",
                                      "Microprocessadores e Microcontroladores")
        self.eng_comp.adiciona_aresta("a19", "Cálculo II", "Álgebra Linear Aplicada à Computação")
        self.eng_comp.adiciona_aresta("a20", "Cálculo II", "Eletricidade e Eletromagnetismo")
        self.eng_comp.adiciona_aresta("a21", "Estruturas de Dados e Algoritmos", "Redes de Computadore")
        self.eng_comp.adiciona_aresta("a22", "Estruturas de Dados e Algoritmos", "Bancos de Dados")
        self.eng_comp.adiciona_aresta("a23", "Organização e Arquitetura de Computadores",
                                      "Projeto de Sistemas Digitais")
        self.eng_comp.adiciona_aresta("a24", "Sistemas Operacionais", "Projeto de Sistemas Digitais")
        self.eng_comp.adiciona_aresta("a25", "Álgebra Linear Aplicada à Computação", "Métodos Numéricos")
        self.eng_comp.adiciona_aresta("a26", "Teoria da Computação", "Inteligência Artificial")
        self.eng_comp.adiciona_aresta("a27", "Programação Orientada a Objetos", "Padrões de Projetos")
        self.eng_comp.adiciona_aresta("a28", "Laboratório de Programação Orientada a Objetos", "Padrões de Projetos")
        self.eng_comp.adiciona_aresta("a29", "Cálculo II", "Sinais e Sistemas")
        self.eng_comp.adiciona_aresta("a30", "Projeto de Sistemas Digitais",
                                      "Verificação Funcional de Sistemas Digitais")
        self.eng_comp.adiciona_aresta("a31", "Estruturas de Dados e Algoritmos", "Análise e Técnicas de Algoritmos")
        self.eng_comp.adiciona_aresta("a32", "Padrões de Projetos", "Análise e Projeto de Sistemas")
        self.eng_comp.adiciona_aresta("a33", "Eletricidade e Eletromagnetismo", "Circuitos Eletro-Eletrônicos")
        self.eng_comp.adiciona_aresta("a34", "Sinais e Sistemas", "Circuitos Eletro-Eletrônicos")
        self.eng_comp.adiciona_aresta("a35", "Programação Orientada a Objetos", "Teste de Software")
        self.eng_comp.adiciona_aresta("a36", "Laboratório de Programação Orientada a Objetos", "Teste de Software")
        self.eng_comp.adiciona_aresta("a37", "Bancos de Dados", "Teste de Software")
        self.eng_comp.adiciona_aresta("a38", "Análise e Projeto de Sistemas", "Gerência de Projetos")
        self.eng_comp.adiciona_aresta("a39", "Desenho Assistido por Computador", "Técnicas de Prototipagem")
        self.eng_comp.adiciona_aresta("a40", "Métodos Numéricos", "Processamento Digital de Sinais")
        self.eng_comp.adiciona_aresta("a41", "Sinais e Sistemas", "Processamento Digital de Sinais")
        self.eng_comp.adiciona_aresta("a42", "Circuitos Eletro-Eletrônicos", "Sensores e Atuadores")
        self.eng_comp.adiciona_aresta("a43", "Técnicas de Prototipagem", "Projeto em Engenharia de Computação I")
        self.eng_comp.adiciona_aresta("a44", "Sistemas Operacionais", "Sistemas Embarcados")
        self.eng_comp.adiciona_aresta("a45", "Microprocessadores e Microcontroladores", "Sistemas Embarcados")
        self.eng_comp.adiciona_aresta("a46", "Métodos Numéricos", "Controle e Automação I")
        self.eng_comp.adiciona_aresta("a47", "Circuitos Eletro-Eletrônicos", "Controle e Automação I")
        self.eng_comp.adiciona_aresta("a48", "Projeto em Engenharia de Computação I",
                                      "Projeto em Engenharia de Computação II")

        self.const_edificios = MeuGrafo()
        self.const_edificios.adiciona_vertice('Informática Básica')
        self.const_edificios.adiciona_vertice('Inglês Instrumental')
        self.const_edificios.adiciona_vertice('Português Instrumental')
        self.const_edificios.adiciona_vertice('Química Aplicada')
        self.const_edificios.adiciona_vertice('Cálculo Diferencial e Integral I')
        self.const_edificios.adiciona_vertice('Álgebra Vetorial e Geometria Analítica')
        self.const_edificios.adiciona_vertice('Desenho Técnico')
        self.const_edificios.adiciona_vertice('Introdução a Construção Edifícios')
        self.const_edificios.adiciona_vertice('Física I')
        self.const_edificios.adiciona_vertice('Metodologia da Pesquisa Científica')
        self.const_edificios.adiciona_vertice('Materiais de Construção I')
        self.const_edificios.adiciona_vertice('Des. Assist. por Computador I')
        self.const_edificios.adiciona_vertice('Cálculo Diferencial e Integral II')
        self.const_edificios.adiciona_vertice('Topografia I')
        self.const_edificios.adiciona_vertice('Desenho e Projeto Arquitetônico')
        self.const_edificios.adiciona_vertice('Matemática Financeira Aplicada')
        self.const_edificios.adiciona_vertice('Resistência dos Materiais')
        self.const_edificios.adiciona_vertice('Física II')
        self.const_edificios.adiciona_vertice('Estatística Aplicada')
        self.const_edificios.adiciona_vertice('Técnicas Construtivas I')
        self.const_edificios.adiciona_vertice('Topografia II')
        self.const_edificios.adiciona_vertice('Materiais de Construção II')
        self.const_edificios.adiciona_vertice('Des. Assist. por Computador II')
        self.const_edificios.adiciona_vertice('Instalações Hidrossanitárias')
        self.const_edificios.adiciona_vertice('Instalações Elétricas Pred.')
        self.const_edificios.adiciona_vertice('Especificações e Orcamentos I')
        self.const_edificios.adiciona_vertice('Segurança do Trabalho')
        self.const_edificios.adiciona_vertice('Técnicas Construtivas II')
        self.const_edificios.adiciona_vertice('Estruturas de Concreto I')
        self.const_edificios.adiciona_vertice('Mecânica dos Solos')
        self.const_edificios.adiciona_vertice('Patologia das Construções')
        self.const_edificios.adiciona_vertice('Manutenção Predial')
        self.const_edificios.adiciona_vertice('Estruturas Metálicas')
        self.const_edificios.adiciona_vertice('Fundações e Sistemas de Contenção')
        self.const_edificios.adiciona_vertice('Estruturas de Madeira')
        self.const_edificios.adiciona_vertice('Estruturas de Concreto II')
        self.const_edificios.adiciona_vertice('Especificações e Orcamentos II')
        self.const_edificios.adiciona_vertice('Instalações Especiais')
        self.const_edificios.adiciona_vertice('Formação do Empreendedor')
        self.const_edificios.adiciona_vertice('Planej. Gestão e Controle de Obra')
        self.const_edificios.adiciona_vertice('Legislação Aplicada')
        self.const_edificios.adiciona_vertice('Avaliação Pós-ocupação')
        self.const_edificios.adiciona_vertice('Gestão da Qualidade e Produtividade')
        self.const_edificios.adiciona_vertice('Gestão Ambiental')
        self.const_edificios.adiciona_vertice('Administração de Custos')
        self.const_edificios.adiciona_vertice('Relações Humanas no Trabalho')
        self.const_edificios.adiciona_vertice('Trabalho de Conclusão de Curso')
        self.const_edificios.adiciona_vertice('Estágio Supervisionado')
        self.const_edificios.adiciona_vertice('Libras (optativa)')

        self.const_edificios.adiciona_aresta("a1", "Cálculo Diferencial e Integral I", "Física I")
        self.const_edificios.adiciona_aresta("a2", "Química Aplicada", "Materiais de Construção I")
        self.const_edificios.adiciona_aresta("a3", "Informática Básica", "Des. Assist. por Computador I")
        self.const_edificios.adiciona_aresta("a4", "Desenho Técnico", "Des. Assist. por Computador I")
        self.const_edificios.adiciona_aresta("a5", "Cálculo Diferencial e Integral I",
                                             "Cálculo Diferencial e Integral II")
        self.const_edificios.adiciona_aresta("a6", "Desenho Técnico", "Topografia I")
        self.const_edificios.adiciona_aresta("a7", "Desenho Técnico", "Desenho e Projeto Arquitetônico")
        self.const_edificios.adiciona_aresta("a8", "Cálculo Diferencial e Integral I", "Resistência dos Materiais")
        self.const_edificios.adiciona_aresta("a9", "Física I", "Resistência dos Materiais")
        self.const_edificios.adiciona_aresta("a10", "Física I", "Física II")
        self.const_edificios.adiciona_aresta("a11", "Cálculo Diferencial e Integral II", "Física II")
        self.const_edificios.adiciona_aresta("a12", "Cálculo Diferencial e Integral I", "Estatística Aplicada")
        self.const_edificios.adiciona_aresta("a13", "Informática Básica", "Técnicas Construtivas I")
        self.const_edificios.adiciona_aresta("a14", "Desenho e Projeto Arquitetônico", "Técnicas Construtivas I")
        self.const_edificios.adiciona_aresta("a15", "Topografia I", "Topografia II")
        self.const_edificios.adiciona_aresta("a16", "Materiais de Construção I", "Materiais de Construção II")
        self.const_edificios.adiciona_aresta("a17", "Des. Assist. por Computador I", "Des. Assist. por Computador II")
        self.const_edificios.adiciona_aresta("a18", "Desenho Técnico", "Instalações Hidrossanitárias")
        self.const_edificios.adiciona_aresta("a19", "Física I", "Instalações Hidrossanitárias")
        self.const_edificios.adiciona_aresta("a20", "Desenho Técnico", "Instalações Elétricas Pred.")
        self.const_edificios.adiciona_aresta("a21", "Física I", "Instalações Elétricas Pred.")
        self.const_edificios.adiciona_aresta("a22", "Materiais de Construção I", "Especificações e Orcamentos I")
        self.const_edificios.adiciona_aresta("a23", "Des. Assist. por Computador I", "Segurança do Trabalho")
        self.const_edificios.adiciona_aresta("a23", "Topografia II", "Técnicas Construtivas II")
        self.const_edificios.adiciona_aresta("a24", "Materiais de Construção II", "Técnicas Construtivas II")
        self.const_edificios.adiciona_aresta("a25", "Desenho Técnico", "Estruturas de Concreto I")
        self.const_edificios.adiciona_aresta("a26", "Resistência dos Materiais", "Estruturas de Concreto I")
        self.const_edificios.adiciona_aresta("a27", "Informática Básica", "Mecânica dos Solos")
        self.const_edificios.adiciona_aresta("a28", "Materiais de Construção II", "Mecânica dos Solos")
        self.const_edificios.adiciona_aresta("a29", "Materiais de Construção II", "Patologia das Construções")
        self.const_edificios.adiciona_aresta("a30", "Especificações e Orcamentos I", "Patologia das Construções")
        self.const_edificios.adiciona_aresta("a31", "Técnicas Construtivas II", "Patologia das Construções")
        self.const_edificios.adiciona_aresta("a32", "Estruturas de Concreto I", "Patologia das Construções")
        self.const_edificios.adiciona_aresta("a33", "Instalações Hidrossanitárias", "Manutenção Predial")
        self.const_edificios.adiciona_aresta("a34", "Instalações Elétricas Pred.", "Manutenção Predial")
        self.const_edificios.adiciona_aresta("a35", "Técnicas Construtivas II", "Manutenção Predial")
        self.const_edificios.adiciona_aresta("a36", "Estruturas de Concreto I", "Manutenção Predial")
        self.const_edificios.adiciona_aresta("a37", "Desenho Técnico", "Estruturas Metálicas")
        self.const_edificios.adiciona_aresta("a38", "Resistência dos Materiais", "Estruturas Metálicas")
        self.const_edificios.adiciona_aresta("a39", "Mecânica dos Solos", "Fundações e Sistemas de Contenção")
        self.const_edificios.adiciona_aresta("a40", "Desenho Técnico", "Estruturas de Madeira")
        self.const_edificios.adiciona_aresta("a41", "Resistência dos Materiais", "Estruturas de Madeira")
        self.const_edificios.adiciona_aresta("a42", "Estruturas de Concreto I", "Estruturas de Concreto II")
        self.const_edificios.adiciona_aresta("a43", "Especificações e Orcamentos I", "Especificações e Orcamentos II")
        self.const_edificios.adiciona_aresta("a44", "Matemática Financeira Aplicada",
                                             "Planej. Gestão e Controle de Obra")
        self.const_edificios.adiciona_aresta("a45", "Segurança do Trabalho", "Planej. Gestão e Controle de Obra")
        self.const_edificios.adiciona_aresta("a46", "Metodologia da Pesquisa Científica", "Avaliação Pós-ocupação")
        self.const_edificios.adiciona_aresta("a47", "Desenho e Projeto Arquitetônico", "Avaliação Pós-ocupação")
        self.const_edificios.adiciona_aresta("a48", "Física II", "Avaliação Pós-ocupação")
        self.const_edificios.adiciona_aresta("a49", "Topografia II", "Avaliação Pós-ocupação")
        self.const_edificios.adiciona_aresta("a50", "Mecânica dos Solos", "Gestão da Qualidade e Produtividade")
        self.const_edificios.adiciona_aresta("a51", "Metodologia da Pesquisa Científica", "Gestão Ambiental")
        self.const_edificios.adiciona_aresta("a52", "Matemática Financeira Aplicada", "Administração de Custos")

        self.fisica = MeuGrafo()
        self.fisica.adiciona_vertice('Introdução à Física')
        self.fisica.adiciona_vertice('Pré-Cálculo')
        self.fisica.adiciona_vertice('Psicologia da Aprendizagem')
        self.fisica.adiciona_vertice('Álgebra Vetorial e Geometria Analítica')
        self.fisica.adiciona_vertice('Língua Portuguesa I')
        self.fisica.adiciona_vertice('Metodologia do Trabalho Científico')
        self.fisica.adiciona_vertice('História da Educação')
        self.fisica.adiciona_vertice('Física Básica I')
        self.fisica.adiciona_vertice('Física Experimental I')
        self.fisica.adiciona_vertice('Cálculo Diferencial e Integral I')
        self.fisica.adiciona_vertice('Álgebra Linear')
        self.fisica.adiciona_vertice('Língua Portuguesa II')
        self.fisica.adiciona_vertice('Inglês Instrumental')
        self.fisica.adiciona_vertice('Filosofia da Educação')
        self.fisica.adiciona_vertice('Física Básica II')
        self.fisica.adiciona_vertice('Física Experimental II')
        self.fisica.adiciona_vertice('Cálculo Diferencial e Integral II')
        self.fisica.adiciona_vertice('Química Geral')
        self.fisica.adiciona_vertice('Sociologia da Educação')
        self.fisica.adiciona_vertice('Educação em Direitos Humanos')
        self.fisica.adiciona_vertice('Educação Ambiental e Sustentabilidade')
        self.fisica.adiciona_vertice('Física Básica III')
        self.fisica.adiciona_vertice('Física Experimental III')
        self.fisica.adiciona_vertice('Didática Geral')
        self.fisica.adiciona_vertice('Políticas e Gestão Educacional')
        self.fisica.adiciona_vertice('Cálculo Diferencial e Integral III')
        self.fisica.adiciona_vertice('Computação Aplicada à Física')
        self.fisica.adiciona_vertice('Física Básica IV')
        self.fisica.adiciona_vertice('Física Experimental IV')
        self.fisica.adiciona_vertice('Física Matemática I')
        self.fisica.adiciona_vertice('Termodinâmica')
        self.fisica.adiciona_vertice('Didática Aplicada ao Ensino de Física')
        self.fisica.adiciona_vertice('Prática de Ensino I')
        self.fisica.adiciona_vertice('Estágio Supervisionado I')
        self.fisica.adiciona_vertice('Física Moderna')
        self.fisica.adiciona_vertice('Física Moderna Experimental')
        self.fisica.adiciona_vertice('Mecânica Analítica')
        self.fisica.adiciona_vertice('Evolução do Pensamento Científico')
        self.fisica.adiciona_vertice('Educação em Diversidade')
        self.fisica.adiciona_vertice('Prática de Ensino II')
        self.fisica.adiciona_vertice('Estágio Supervisionado II')
        self.fisica.adiciona_vertice('Mecânica Quântica')
        self.fisica.adiciona_vertice('Eletromagnetismo')
        self.fisica.adiciona_vertice('Prática de Ensino III')
        self.fisica.adiciona_vertice('Prática de Lab. e Inst. para o Ens. de Fís. I')
        self.fisica.adiciona_vertice('Optativa I')
        self.fisica.adiciona_vertice('Estágio Supervisionado III')
        self.fisica.adiciona_vertice('Libras')
        self.fisica.adiciona_vertice('Prática de Lab. e Inst. para o Ens. de Fís. II')
        self.fisica.adiciona_vertice('Prática de Ensino IV')
        self.fisica.adiciona_vertice('Mecânica Estatística')
        self.fisica.adiciona_vertice('TCC')
        self.fisica.adiciona_vertice('Optativa II')
        self.fisica.adiciona_vertice('Estágio Supervisionado IV')

        self.fisica.adiciona_aresta("a1", "Introdução à Física", "Física Básica I")
        self.fisica.adiciona_aresta("a2", "Pré-Cálculo", "Física Básica I")
        self.fisica.adiciona_aresta("a3", "Introdução à Física", "Física Experimental I")
        self.fisica.adiciona_aresta("a4", "Pré-Cálculo", "Física Experimental I")
        self.fisica.adiciona_aresta("a5", "Pré-Cálculo", "Cálculo Diferencial e Integral I")
        self.fisica.adiciona_aresta("a6", "Pré-Cálculo", "Álgebra Linear")
        self.fisica.adiciona_aresta("a7", "Álgebra Vetorial e Geometria Analítica", "Álgebra Linear")
        self.fisica.adiciona_aresta("a8", "Língua Portuguesa I", "Língua Portuguesa II")
        self.fisica.adiciona_aresta("a9", "Física Básica I", "Física Básica II")
        self.fisica.adiciona_aresta("a10", "Cálculo Diferencial e Integral I", "Física Básica II")
        self.fisica.adiciona_aresta("a11", "Física Básica I", "Física Experimental II")
        self.fisica.adiciona_aresta("a12", "Física Experimental I", "Física Experimental II")
        self.fisica.adiciona_aresta("a13", "Cálculo Diferencial e Integral I", "Cálculo Diferencial e Integral II")
        self.fisica.adiciona_aresta("a14", "Física Básica II", "Física Básica III")
        self.fisica.adiciona_aresta("a15", "Física Básica II", "Física Experimental III")
        self.fisica.adiciona_aresta("a16", "Física Experimental II", "Física Experimental III")
        self.fisica.adiciona_aresta("a17", "Cálculo Diferencial e Integral I", "Cálculo Diferencial e Integral III")
        self.fisica.adiciona_aresta("a18", "Física Básica II", "Computação Aplicada à Física")
        self.fisica.adiciona_aresta("a19", "Física Básica III", "Física Básica IV")
        self.fisica.adiciona_aresta("a20", "Cálculo Diferencial e Integral III", "Física Básica IV")
        self.fisica.adiciona_aresta("a21", "Física Básica III", "Física Experimental IV")
        self.fisica.adiciona_aresta("a22", "Física Experimental III", "Física Experimental IV")
        self.fisica.adiciona_aresta("a23", "Cálculo Diferencial e Integral III", "Física Matemática I")
        self.fisica.adiciona_aresta("a24", "Física Básica II", "Termodinâmica")
        self.fisica.adiciona_aresta("a25", "Didática Geral", "Didática Aplicada ao Ensino de Física")
        self.fisica.adiciona_aresta("a26", "Física Básica I", "Estágio Supervisionado I")
        self.fisica.adiciona_aresta("a27", "Didática Geral", "Estágio Supervisionado I")
        self.fisica.adiciona_aresta("a28", "Física Básica IV", "Física Moderna Experimental")
        self.fisica.adiciona_aresta("a29", "Física Experimental IV", "Física Moderna Experimental")
        self.fisica.adiciona_aresta("a30", "Física Básica I", "Mecânica Analítica")
        self.fisica.adiciona_aresta("a31", "Física Matemática I", "Mecânica Analítica")
        self.fisica.adiciona_aresta("a32", "Física Básica IV", "Evolução do Pensamento Científico")
        self.fisica.adiciona_aresta("a33", "Prática de Ensino I", "Prática de Ensino II")
        self.fisica.adiciona_aresta("a34", "Física Básica II", "Estágio Supervisionado II")
        self.fisica.adiciona_aresta("a35", "Estágio Supervisionado I", "Estágio Supervisionado II")
        self.fisica.adiciona_aresta("a36", "Física Moderna", "Mecânica Quântica")
        self.fisica.adiciona_aresta("a37", "Física Básica III", "Eletromagnetismo")
        self.fisica.adiciona_aresta("a38", "Cálculo Diferencial e Integral III", "Eletromagnetismo")
        self.fisica.adiciona_aresta("a39", "Prática de Ensino II", "Prática de Ensino III")
        self.fisica.adiciona_aresta("a40", "Física Básica II", "Prática de Lab. e Inst. para o Ens. de Fís. I")
        self.fisica.adiciona_aresta("a41", "Didática Geral", "Prática de Lab. e Inst. para o Ens. de Fís. I")
        self.fisica.adiciona_aresta("a42", "Física Básica III", "Estágio Supervisionado III")
        self.fisica.adiciona_aresta("a43", "Estágio Supervisionado II", "Estágio Supervisionado III")
        self.fisica.adiciona_aresta("a44", "Educação em Diversidade", "Libras")
        self.fisica.adiciona_aresta("a45", "Prática de Lab. e Inst. para o Ens. de Fís. I",
                                    "Prática de Lab. e Inst. para o Ens. de Fís. II")
        self.fisica.adiciona_aresta("a46", "Prática de Ensino III", "Prática de Ensino IV")
        self.fisica.adiciona_aresta("a47", "Termodinâmica", "Mecânica Estatística")
        self.fisica.adiciona_aresta("a48", "Mecânica Quântica", "Mecânica Estatística")
        self.fisica.adiciona_aresta("a49", "Metodologia do Trabalho Científico", "TCC")
        self.fisica.adiciona_aresta("a50", "Língua Portuguesa II", "TCC")
        self.fisica.adiciona_aresta("a51", "Física Básica IV", "Estágio Supervisionado IV")
        self.fisica.adiciona_aresta("a52", "Estágio Supervisionado III", "Estágio Supervisionado IV")

        self.matematica = MeuGrafo()
        self.matematica.adiciona_vertice('Matemática para o Ensino Médio 1')
        self.matematica.adiciona_vertice('Matemática para o Ensino Fundamental')
        self.matematica.adiciona_vertice('Trigonometria')
        self.matematica.adiciona_vertice('História da Educação')
        self.matematica.adiciona_vertice('Psicologia da Aprendizagem')
        self.matematica.adiciona_vertice('Língua Portuguesa 1')
        self.matematica.adiciona_vertice('Inglês Instrumental')
        self.matematica.adiciona_vertice('Matemática para o Ensino Médio 2')
        self.matematica.adiciona_vertice('Cálculo 1')
        self.matematica.adiciona_vertice('Álgebra Vetorial e Geometria Analítica')
        self.matematica.adiciona_vertice('Epistemologia da Matemática')
        self.matematica.adiciona_vertice('Filosofia da Educação')
        self.matematica.adiciona_vertice('Língua Portuguesa 2')
        self.matematica.adiciona_vertice('Educação em Diversidade')
        self.matematica.adiciona_vertice('Matemática para o Ensino Médio 3')
        self.matematica.adiciona_vertice('Cálculo 2')
        self.matematica.adiciona_vertice('Argumentação Matemática')
        self.matematica.adiciona_vertice('Prática de Laboratório de Ensino de Matemática 1')
        self.matematica.adiciona_vertice('Sociologia da Educação')
        self.matematica.adiciona_vertice('Didática Geral')
        self.matematica.adiciona_vertice('Álgebra Linear 1')
        self.matematica.adiciona_vertice('Cálculo 3')
        self.matematica.adiciona_vertice('Didática da Matemática')
        self.matematica.adiciona_vertice('Prática de Laboratório de Ensino de Matemática 2')
        self.matematica.adiciona_vertice('Libras 1')
        self.matematica.adiciona_vertice('Metodologia do Trabalho Científico')
        self.matematica.adiciona_vertice('Introdução a Teoria dos Números')
        self.matematica.adiciona_vertice('Desenho Geométrico')
        self.matematica.adiciona_vertice('Física Básica 1')
        self.matematica.adiciona_vertice('Prática de Ensino de Matemática 1')
        self.matematica.adiciona_vertice('Introdução à Programação')
        self.matematica.adiciona_vertice('Gestão Educacional e Planejamento')
        self.matematica.adiciona_vertice('Estágio Supervisionado 1')
        self.matematica.adiciona_vertice('Estruturas Algébricas 1')
        self.matematica.adiciona_vertice('Geometria Euclidiana Plana')
        self.matematica.adiciona_vertice('Estatística e Probabilidade')
        self.matematica.adiciona_vertice('Prática de Ensino de Matemática 2')
        self.matematica.adiciona_vertice('Pesquisa Aplicada em Matemática 1')
        self.matematica.adiciona_vertice('Educação em Direitos Humanos')
        self.matematica.adiciona_vertice('Estágio Supervisionado 2')
        self.matematica.adiciona_vertice('Análise Real 1')
        self.matematica.adiciona_vertice('Matemática Financeira 1')
        self.matematica.adiciona_vertice('Equações Diferenciais Ordinárias')
        self.matematica.adiciona_vertice('Prática de Ensino de Matemática 3')
        self.matematica.adiciona_vertice('Pesquisa Aplicada em Matemática 2')
        self.matematica.adiciona_vertice('Optativa 1')
        self.matematica.adiciona_vertice('Estágio Supervisionado 3')
        self.matematica.adiciona_vertice('Geometria Euclidiana Espacial')
        self.matematica.adiciona_vertice('TCC')
        self.matematica.adiciona_vertice('História da Matemática')
        self.matematica.adiciona_vertice('Prática de Ensino de Matemática 4')
        self.matematica.adiciona_vertice('Educação Ambiental e Sustentabilidade')
        self.matematica.adiciona_vertice('Optativa 2')
        self.matematica.adiciona_vertice('Estágio Supervisionado 4')

        self.matematica.adiciona_aresta("a1", "Matemática para o Ensino Médio 1", "Matemática para o Ensino Médio 2")
        self.matematica.adiciona_aresta("a2", "Matemática para o Ensino Médio 1", "Cálculo 1")
        self.matematica.adiciona_aresta("a3", "Trigonometria", "Cálculo 1")
        self.matematica.adiciona_aresta("a4", "Língua Portuguesa 1", "Língua Portuguesa 2")
        self.matematica.adiciona_aresta("a5", "Matemática para o Ensino Médio 2", "Matemática para o Ensino Médio 3")
        self.matematica.adiciona_aresta("a6", "Cálculo 1", "Cálculo 2")
        self.matematica.adiciona_aresta("a7", "Matemática para o Ensino Fundamental", "Argumentação Matemática")
        self.matematica.adiciona_aresta("a8", "Matemática para o Ensino Fundamental",
                                        "Prática de Laboratório de Ensino de Matemática 1")
        self.matematica.adiciona_aresta("a9", "Matemática para o Ensino Médio 2", "Álgebra Linear 1")
        self.matematica.adiciona_aresta("a10", "Álgebra Vetorial e Geometria Analítica", "Álgebra Linear 1")
        self.matematica.adiciona_aresta("a11", "Álgebra Vetorial e Geometria Analítica", "Cálculo 3")
        self.matematica.adiciona_aresta("a12", "Cálculo 2", "Cálculo 3")
        self.matematica.adiciona_aresta("a13", "Didática Geral", "Didática da Matemática")
        self.matematica.adiciona_aresta("a14", "Prática de Laboratório de Ensino de Matemática 1",
                                        "Prática de Laboratório de Ensino de Matemática 2")
        self.matematica.adiciona_aresta("a15", "Educação em Diversidade", "Libras 1")
        self.matematica.adiciona_aresta("a16", "Argumentação Matemática", "Introdução a Teoria dos Números")
        self.matematica.adiciona_aresta("a17", "Matemática para o Ensino Fundamental", "Desenho Geométrico")
        self.matematica.adiciona_aresta("a18", "Cálculo 2", "Física Básica 1")
        self.matematica.adiciona_aresta("a19", "Prática de Laboratório de Ensino de Matemática 2",
                                        "Prática de Ensino de Matemática 1")
        self.matematica.adiciona_aresta("a20", "Prática de Laboratório de Ensino de Matemática 2",
                                        "Introdução à Programação")
        self.matematica.adiciona_aresta("a21", "Prática de Laboratório de Ensino de Matemática 2",
                                        "Estágio Supervisionado 1")
        self.matematica.adiciona_aresta("a22", "Introdução a Teoria dos Números", "Estruturas Algébricas 1")
        self.matematica.adiciona_aresta("a23", "Desenho Geométrico", "Geometria Euclidiana Plana")
        self.matematica.adiciona_aresta("a24", "Cálculo 2", "Estatística e Probabilidade")
        self.matematica.adiciona_aresta("a25", "Prática de Ensino de Matemática 1", "Prática de Ensino de Matemática 2")
        self.matematica.adiciona_aresta("a26", "Metodologia do Trabalho Científico",
                                        "Pesquisa Aplicada em Matemática 1")
        self.matematica.adiciona_aresta("a27", "Estágio Supervisionado 1", "Estágio Supervisionado 2")
        self.matematica.adiciona_aresta("a28", "Cálculo 3", "Análise Real 1")
        self.matematica.adiciona_aresta("a29", "Cálculo 1", "Matemática Financeira 1")
        self.matematica.adiciona_aresta("a30", "Álgebra Linear 1", "Equações Diferenciais Ordinárias")
        self.matematica.adiciona_aresta("a31", "Cálculo 3", "Equações Diferenciais Ordinárias")
        self.matematica.adiciona_aresta("a32", "Prática de Ensino de Matemática 2", "Prática de Ensino de Matemática 3")
        self.matematica.adiciona_aresta("a33", "Pesquisa Aplicada em Matemática 1", "Pesquisa Aplicada em Matemática 2")
        self.matematica.adiciona_aresta("a34", "Estágio Supervisionado 2", "Estágio Supervisionado 3")
        self.matematica.adiciona_aresta("a35", "Geometria Euclidiana Plana", "Geometria Euclidiana Espacial")
        self.matematica.adiciona_aresta("a36", "Pesquisa Aplicada em Matemática 2", "TCC")
        self.matematica.adiciona_aresta("a37", "Cálculo 2", "História da Matemática")
        self.matematica.adiciona_aresta("a38", "Prática de Ensino de Matemática 3", "Prática de Ensino de Matemática 4")
        self.matematica.adiciona_aresta("a39", "Estágio Supervisionado 3", "Estágio Supervisionado 4")

        self.letras = MeuGrafo()
        self.letras.adiciona_vertice('Introdução aos Estudos Literários')
        self.letras.adiciona_vertice('Introdução à Linguistica')
        self.letras.adiciona_vertice('Leitura e Produção de Texto I')
        self.letras.adiciona_vertice('Informática Básica')
        self.letras.adiciona_vertice('Fundamentos da Educação a Distância')
        self.letras.adiciona_vertice('Inglês Instrumental')
        self.letras.adiciona_vertice('História da Educação Brasileira')
        self.letras.adiciona_vertice('Teoria Literária I')
        self.letras.adiciona_vertice('Literatura e Ensino')
        self.letras.adiciona_vertice('Morfologia da Língua Portuguesa')
        self.letras.adiciona_vertice('Fundamentos da Linguística Românica')
        self.letras.adiciona_vertice('Linguística I')
        self.letras.adiciona_vertice('Filosofia da Educação')
        self.letras.adiciona_vertice('Metodologia da Pesquisa Científica')
        self.letras.adiciona_vertice('Teoria Literária II')
        self.letras.adiciona_vertice('Literatura Brasileira I')
        self.letras.adiciona_vertice('Literatura Portuguesa I')
        self.letras.adiciona_vertice('História da Língua Portuguesa')
        self.letras.adiciona_vertice('Linguística II')
        self.letras.adiciona_vertice('Psicologia da Aprendizagem')
        self.letras.adiciona_vertice('Seminário de Pesquisa Interdisciplinar I')
        self.letras.adiciona_vertice('Literatura Brasileira II')
        self.letras.adiciona_vertice('Literatura Portuguesa II')
        self.letras.adiciona_vertice('Fonética e Fonologia da Língua Portuguesa')
        self.letras.adiciona_vertice('Aquisição da Linguagem')
        self.letras.adiciona_vertice('Didática')
        self.letras.adiciona_vertice('Morfossintaxe')
        self.letras.adiciona_vertice('Seminário de Pesquisa Interdisciplinar II')
        self.letras.adiciona_vertice('Literatura Brasileira III')
        self.letras.adiciona_vertice('Semântica da Lingua Portuguesa')
        self.letras.adiciona_vertice('Leitura e Produção de Texto II')
        self.letras.adiciona_vertice('Orientação de Estágio Supervisionado I')
        self.letras.adiciona_vertice('Metodologia do Ensino de Língua Portuguesa')
        self.letras.adiciona_vertice('Metodologia do Ensino de Literatura')
        self.letras.adiciona_vertice('Seminário de Pesquisa Interdisciplinar III')
        self.letras.adiciona_vertice('Literatura Brasileira IV')
        self.letras.adiciona_vertice('Literaturas Africanas de Língua Portuguesa')
        self.letras.adiciona_vertice('Sociolinguística')
        self.letras.adiciona_vertice('Orientação de Estágio Supervisionado II')
        self.letras.adiciona_vertice('Língua Brasileira de Sinais (LIBRAS)')
        self.letras.adiciona_vertice('Educação Inclusiva')
        self.letras.adiciona_vertice('Seminário de Pesquisa Interdisciplinar IV')
        self.letras.adiciona_vertice('Estágio Supervisionado I')
        self.letras.adiciona_vertice('Literatura Brasileira V')
        self.letras.adiciona_vertice('Literatura Infantil e juvenil')
        self.letras.adiciona_vertice('Literatura e Cultura Popular')
        self.letras.adiciona_vertice('Orientação de Estágio Supervisionado III')
        self.letras.adiciona_vertice('Pragmática')
        self.letras.adiciona_vertice('Estrutura e Funcionamento da Educ. Básica')
        self.letras.adiciona_vertice('Orientação de TCC I')
        self.letras.adiciona_vertice('Estágio Supervisionado II')
        self.letras.adiciona_vertice('Língua Portuguesa como segunda língua para surdos (Optativa)')
        self.letras.adiciona_vertice('Gestão Educacional')
        self.letras.adiciona_vertice('Tópicos em Projetos Especiais')
        self.letras.adiciona_vertice('Sociologia da Educação')
        self.letras.adiciona_vertice('Orientação de Estágio Supervisionado IV')
        self.letras.adiciona_vertice('Educação e Direitos Humanos')
        self.letras.adiciona_vertice('Educação Ambiental e Interdisciplinaridade')
        self.letras.adiciona_vertice('Orientação de TCC II')
        self.letras.adiciona_vertice('Estágio Supervisionado III')

        self.letras.adiciona_aresta("a1", "Introdução aos Estudos Literários", "Teoria Literária I")
        self.letras.adiciona_aresta("a2", "Introdução aos Estudos Literários", "Literatura e Ensino")
        self.letras.adiciona_aresta("a3", "Introdução à Linguistica", "Morfologia da Língua Portuguesa")
        self.letras.adiciona_aresta("a4", "Introdução à Linguistica", "Linguística I")
        self.letras.adiciona_aresta("a5", "História da Educação Brasileira", "Filosofia da Educação")
        self.letras.adiciona_aresta("a6", "Teoria Literária I", "Teoria Literária II")
        self.letras.adiciona_aresta("a7", "Teoria Literária I", "Literatura Brasileira I")
        self.letras.adiciona_aresta("a8", "Teoria Literária I", "Literatura Portuguesa I")
        self.letras.adiciona_aresta("a9", "Fundamentos da Linguística Românica", "História da Língua Portuguesa")
        self.letras.adiciona_aresta("a10", "Linguística I", "Linguística II")
        self.letras.adiciona_aresta("a11", "Teoria Literária II", "Literatura Brasileira II")
        self.letras.adiciona_aresta("a12", "Literatura Portuguesa I", "Literatura Portuguesa II")
        self.letras.adiciona_aresta("a13", "Linguística I", "Fonética e Fonologia da Língua Portuguesa")
        self.letras.adiciona_aresta("a14", "Linguística I", "Aquisição da Linguagem")
        self.letras.adiciona_aresta("a15", "Psicologia da Aprendizagem", "Aquisição da Linguagem")
        self.letras.adiciona_aresta("a16", "Morfologia da Língua Portuguesa", "Morfossintaxe")
        self.letras.adiciona_aresta("a17", "Linguística II", "Morfossintaxe")
        self.letras.adiciona_aresta("a18", "Seminário de Pesquisa Interdisciplinar I",
                                    "Seminário de Pesquisa Interdisciplinar II")
        self.letras.adiciona_aresta("a19", "Teoria Literária II", "Literatura Brasileira III")
        self.letras.adiciona_aresta("a20", "Linguística II", "Semântica da Lingua Portuguesa")
        self.letras.adiciona_aresta("a21", "Leitura e Produção de Texto I", "Leitura e Produção de Texto II")
        self.letras.adiciona_aresta("a22", "Didática", "Orientação de Estágio Supervisionado I")
        self.letras.adiciona_aresta("a23", "Linguística II", "Metodologia do Ensino de Língua Portuguesa")
        self.letras.adiciona_aresta("a24", "Literatura e Ensino", "Metodologia do Ensino de Literatura")
        self.letras.adiciona_aresta("a25", "Seminário de Pesquisa Interdisciplinar I",
                                    "Seminário de Pesquisa Interdisciplinar III")
        self.letras.adiciona_aresta("a26", "Teoria Literária II", "Literatura Brasileira IV")
        self.letras.adiciona_aresta("a27", "Teoria Literária II", "Literaturas Africanas de Língua Portuguesa")
        self.letras.adiciona_aresta("a28", "Linguística II", "Sociolinguística")
        self.letras.adiciona_aresta("a29", "Orientação de Estágio Supervisionado I",
                                    "Orientação de Estágio Supervisionado II")
        self.letras.adiciona_aresta("a30", "Seminário de Pesquisa Interdisciplinar I",
                                    "Seminário de Pesquisa Interdisciplinar IV")
        self.letras.adiciona_aresta("a31", "Orientação de Estágio Supervisionado I", "Estágio Supervisionado I")
        self.letras.adiciona_aresta("a32", "Teoria Literária II", "Literatura Brasileira V")
        self.letras.adiciona_aresta("a33", "Teoria Literária II", "Literatura Infantil e juvenil")
        self.letras.adiciona_aresta("a34", "Teoria Literária II", "Literatura e Cultura Popular")
        self.letras.adiciona_aresta("a35", "Orientação de Estágio Supervisionado II",
                                    "Orientação de Estágio Supervisionado III")
        self.letras.adiciona_aresta("a36", "Linguística II", "Pragmática")
        self.letras.adiciona_aresta("a37", "Didática", "Estrutura e Funcionamento da Educ. Básica")
        self.letras.adiciona_aresta("a38", "Metodologia da Pesquisa Científica", "Orientação de TCC I")
        self.letras.adiciona_aresta("a39", "Leitura e Produção de Texto II", "Orientação de TCC I")
        self.letras.adiciona_aresta("a40", "Orientação de Estágio Supervisionado II", "Estágio Supervisionado II")
        self.letras.adiciona_aresta("a41", "Estágio Supervisionado I", "Estágio Supervisionado II")
        self.letras.adiciona_aresta("a42", "Língua Brasileira de Sinais (LIBRAS)",
                                    "Língua Portuguesa como segunda língua para surdos (Optativa)")
        self.letras.adiciona_aresta("a43", "História da Educação Brasileira", "Sociologia da Educação")
        self.letras.adiciona_aresta("a44", "Orientação de Estágio Supervisionado III",
                                    "Orientação de Estágio Supervisionado IV")
        self.letras.adiciona_aresta("a45", "Orientação de TCC I", "Orientação de TCC II")
        self.letras.adiciona_aresta("a46", "Orientação de Estágio Supervisionado III", "Estágio Supervisionado III")
        self.letras.adiciona_aresta("a47", "Estágio Supervisionado II", "Estágio Supervisionado III")

        self.telematica = MeuGrafo()
        self.telematica.adiciona_vertice('Introdução à Telemática')
        self.telematica.adiciona_vertice('Fundamentos de Eletricidade')
        self.telematica.adiciona_vertice('Programação I')
        self.telematica.adiciona_vertice('Lab. de Sist. Abertos')
        self.telematica.adiciona_vertice('Inglês Instrumental')
        self.telematica.adiciona_vertice('Pré-cálculo')
        self.telematica.adiciona_vertice('Língua Portuguesa')
        self.telematica.adiciona_vertice('Redes de Computadores')
        self.telematica.adiciona_vertice('Eletrônica para Telecomunicações')
        self.telematica.adiciona_vertice('Medição Eletroeletrônica')
        self.telematica.adiciona_vertice('Programação II')
        self.telematica.adiciona_vertice('Arquitetura de Computadores')
        self.telematica.adiciona_vertice('Cálculo Diferencial e Integral')
        self.telematica.adiciona_vertice('Educação em Diversidade')
        self.telematica.adiciona_vertice('Tecnologias de Redes Locais')
        self.telematica.adiciona_vertice('Estatística Aplicada à Telemática')
        self.telematica.adiciona_vertice('Sinais e Sistemas')
        self.telematica.adiciona_vertice('Administração de Sistemas')
        self.telematica.adiciona_vertice('Sistemas Operacionais')
        self.telematica.adiciona_vertice('Programação III')
        self.telematica.adiciona_vertice('Metodologia da Pesquisa Científica')
        self.telematica.adiciona_vertice('Interconexão de Redes')
        self.telematica.adiciona_vertice('Cabeamento Estruturado')
        self.telematica.adiciona_vertice('Teoria da Informação e Codificação')
        self.telematica.adiciona_vertice('Sistemas de Comunicações')
        self.telematica.adiciona_vertice('Processamento Digital de Sinais')
        self.telematica.adiciona_vertice('Administração de Serviços')
        self.telematica.adiciona_vertice('Educação Ambiental e Sustentabilidade')
        self.telematica.adiciona_vertice('Redes de Longa Distância')
        self.telematica.adiciona_vertice('Segurança de Redes de Computadores')
        self.telematica.adiciona_vertice('Comunicações Sem Fio')
        self.telematica.adiciona_vertice('Comunicações Ópticas')
        self.telematica.adiciona_vertice('Projeto em Telemática')
        self.telematica.adiciona_vertice('Formação do Empreendedor')
        self.telematica.adiciona_vertice('Optativa I')
        self.telematica.adiciona_vertice('Projeto de Redes de Computadores')
        self.telematica.adiciona_vertice('Sistemas Telefônicos')
        self.telematica.adiciona_vertice('Educação em Direitos Humanos')
        self.telematica.adiciona_vertice('Relações Humanas no Trabalho')
        self.telematica.adiciona_vertice('Ética')
        self.telematica.adiciona_vertice('Optativa II')
        self.telematica.adiciona_vertice('Trabalho de Conclusão de Curso (Obrigatória)')
        self.telematica.adiciona_vertice('Estágio Supervisionado (Optativa)')

        self.telematica.adiciona_aresta("a1", "Introdução à Telemática", "Redes de Computadores")
        self.telematica.adiciona_aresta("a2", "Fundamentos de Eletricidade", "Eletrônica para Telecomunicações")
        self.telematica.adiciona_aresta("a3", "Pré-cálculo", "Eletrônica para Telecomunicações")
        self.telematica.adiciona_aresta("a4", "Fundamentos de Eletricidade", "Medição Eletroeletrônica")
        self.telematica.adiciona_aresta("a5", "Pré-cálculo", "Medição Eletroeletrônica")
        self.telematica.adiciona_aresta("a6", "Programação I", "Programação II")
        self.telematica.adiciona_aresta("a7", "Pré-cálculo", "Cálculo Diferencial e Integral")
        self.telematica.adiciona_aresta("a8", "Redes de Computadores", "Tecnologias de Redes Locais")
        self.telematica.adiciona_aresta("a9", "Cálculo Diferencial e Integral", "Estatística Aplicada à Telemática")
        self.telematica.adiciona_aresta("a10", "Eletrônica para Telecomunicações", "Sinais e Sistemas")
        self.telematica.adiciona_aresta("a11", "Medição Eletroeletrônica", "Sinais e Sistemas")
        self.telematica.adiciona_aresta("a12", "Cálculo Diferencial e Integral", "Sinais e Sistemas")
        self.telematica.adiciona_aresta("a13", "Lab. de Sist. Abertos", "Administração de Sistemas")
        self.telematica.adiciona_aresta("a14", "Arquitetura de Computadores", "Sistemas Operacionais")
        self.telematica.adiciona_aresta("a15", "Redes de Computadores", "Programação III")
        self.telematica.adiciona_aresta("a16", "Programação II", "Programação III")
        self.telematica.adiciona_aresta("a17", "Tecnologias de Redes Locais", "Interconexão de Redes")
        self.telematica.adiciona_aresta("a18", "Tecnologias de Redes Locais", "Cabeamento Estruturado")
        self.telematica.adiciona_aresta("a19", "Estatística Aplicada à Telemática",
                                        "Teoria da Informação e Codificação")
        self.telematica.adiciona_aresta("a20", "Estatística Aplicada à Telemática", "Sistemas de Comunicações")
        self.telematica.adiciona_aresta("a21", "Sinais e Sistemas", "Sistemas de Comunicações")
        self.telematica.adiciona_aresta("a22", "Sinais e Sistemas", "Processamento Digital de Sinais")
        self.telematica.adiciona_aresta("a23", "Redes de Computadores", "Administração de Serviços")
        self.telematica.adiciona_aresta("a24", "Administração de Sistemas", "Administração de Serviços")
        self.telematica.adiciona_aresta("a25", "Interconexão de Redes", "Redes de Longa Distância")
        self.telematica.adiciona_aresta("a26", "Interconexão de Redes", "Segurança de Redes de Computadores")
        self.telematica.adiciona_aresta("a27", "Sistemas de Comunicações", "Comunicações Sem Fio")
        self.telematica.adiciona_aresta("a28", "Sistemas de Comunicações", "Comunicações Ópticas")
        self.telematica.adiciona_aresta("a29", "Metodologia da Pesquisa Científica", "Projeto em Telemática")
        self.telematica.adiciona_aresta("a30", "Interconexão de Redes", "Projeto em Telemática")
        self.telematica.adiciona_aresta("a31", "Sistemas de Comunicações", "Projeto em Telemática")
        self.telematica.adiciona_aresta("a32", "Cabeamento Estruturado", "Projeto de Redes de Computadores")
        self.telematica.adiciona_aresta("a33", "Redes de Longa Distância", "Projeto de Redes de Computadores")
        self.telematica.adiciona_aresta("a34", "Comunicações Sem Fio", "Sistemas Telefônicos")
        self.telematica.adiciona_aresta("a35", "Projeto em Telemática", "Trabalho de Conclusão de Curso (Obrigatória)")
        self.telematica.adiciona_aresta("a36", "Metodologia da Pesquisa Científica",
                                        "Estágio Supervisionado (Optativa)")
        self.telematica.adiciona_aresta("a37", "Interconexão de Redes", "Estágio Supervisionado (Optativa)")
        self.telematica.adiciona_aresta("a38", "Sistemas de Comunicações", "Estágio Supervisionado (Optativa)")

        self.listaEng = ["Pré-Cálculo", "Inglês Instrumental", "Introdução à Engenharia de Computação",
                         "Algoritmos e Programação", "Lab. de Algoritmos e Programação", "Sistemas Digitais I",
                         "Medição Eletro-eletrônica", "Estatística Aplicada à Computação",
                         "Leitura e Produção de Textos", "Educação Ambiental e Sustentabilidade",
                         "Relações Humanas no Trabalho", "Metodologia da Pesquisa Científica", "Libras",
                         "Desenho Assistido por Computador", "Empreendedorismo de Base Tecnológica",
                         "Educação em Direitos Humanos", "Educação em Diversidade", "Cálculo I",
                         "Estruturas de Dados e Algoritmos", "Laboratório de Estruturas de Dados e Algoritmos",
                         "Programação Orientada a Objetos", "Laboratório de Programação Orientada a Objetos",
                         "Sistemas Digitais II", "Técnicas de Prototipagem", "Cálculo II", "Física Clássica",
                         "Teoria dos Grafos", "Teoria da Computação", "Redes de Computadore", "Bancos de Dados",
                         "Análise e Técnicas de Algoritmos", "Padrões de Projetos",
                         "Organização e Arquitetura de Computadores", "Projeto em Engenharia de Computação I",
                         "Álgebra Linear Aplicada à Computação", "Eletricidade e Eletromagnetismo", "Sinais e Sistemas",
                         "Inteligência Artificial", "Teste de Software", "Análise e Projeto de Sistemas",
                         "Sistemas Operacionais", "Microprocessadores e Microcontroladores",
                         "Projeto em Engenharia de Computação II", "Métodos Numéricos", "Circuitos Eletro-Eletrônicos",
                         "Gerência de Projetos", "Projeto de Sistemas Digitais", "Sistemas Embarcados",
                         "Processamento Digital de Sinais", "Sensores e Atuadores", "Controle e Automação I",
                         "Verificação Funcional de Sistemas Digitais", ]
        self.listaTel = ["Introdução à Telemática", "Fundamentos de Eletricidade", "Programação I",
                         "Lab. de Sist. Abertos", "Inglês Instrumental", "Pré-cálculo", "Língua Portuguesa",
                         "Arquitetura de Computadores", "Educação em Diversidade", "Metodologia da Pesquisa Científica",
                         "Educação Ambiental e Sustentabilidade", "Formação do Empreendedor", "Optativa I",
                         "Educação em Direitos Humanos", "Relações Humanas no Trabalho", "Ética", "Optativa II",
                         "Redes de Computadores", "Programação II", "Administração de Sistemas",
                         "Eletrônica para Telecomunicações", "Medição Eletroeletrônica",
                         "Cálculo Diferencial e Integral", "Sistemas Operacionais", "Tecnologias de Redes Locais",
                         "Programação III", "Administração de Serviços", "Estatística Aplicada à Telemática",
                         "Sinais e Sistemas", "Interconexão de Redes", "Cabeamento Estruturado",
                         "Teoria da Informação e Codificação", "Sistemas de Comunicações",
                         "Processamento Digital de Sinais", "Redes de Longa Distância",
                         "Segurança de Redes de Computadores", "Comunicações Sem Fio", "Comunicações Ópticas",
                         "Projeto em Telemática", "Estágio Supervisionado (Optativa)",
                         "Projeto de Redes de Computadores", "Sistemas Telefônicos",
                         "Trabalho de Conclusão de Curso (Obrigatória)"]
        self.listaMat = ["Matemática para o Ensino Médio 1", "Matemática para o Ensino Fundamental", "Trigonometria",
                         "História da Educação", "Psicologia da Aprendizagem", "Língua Portuguesa 1",
                         "Inglês Instrumental", "Álgebra Vetorial e Geometria Analítica", "Epistemologia da Matemática",
                         "Filosofia da Educação", "Educação em Diversidade", "Sociologia da Educação", "Didática Geral",
                         "Metodologia do Trabalho Científico", "Gestão Educacional e Planejamento",
                         "Educação em Direitos Humanos", "Optativa 1", "Educação Ambiental e Sustentabilidade",
                         "Optativa 2", "Matemática para o Ensino Médio 2", "Argumentação Matemática",
                         "Prática de Laboratório de Ensino de Matemática 1", "Desenho Geométrico", "Cálculo 1",
                         "Língua Portuguesa 2", "Libras 1", "Didática da Matemática",
                         "Pesquisa Aplicada em Matemática 1", "Matemática para o Ensino Médio 3", "Álgebra Linear 1",
                         "Introdução a Teoria dos Números", "Prática de Laboratório de Ensino de Matemática 2",
                         "Geometria Euclidiana Plana", "Cálculo 2", "Matemática Financeira 1",
                         "Pesquisa Aplicada em Matemática 2", "Estruturas Algébricas 1",
                         "Prática de Ensino de Matemática 1", "Introdução à Programação", "Estágio Supervisionado 1",
                         "Geometria Euclidiana Espacial", "Cálculo 3", "Física Básica 1", "Estatística e Probabilidade",
                         "História da Matemática", "TCC", "Prática de Ensino de Matemática 2",
                         "Estágio Supervisionado 2", "Análise Real 1", "Equações Diferenciais Ordinárias",
                         "Prática de Ensino de Matemática 3", "Estágio Supervisionado 3",
                         "Prática de Ensino de Matemática 4", "Estágio Supervisionado 4"]
        self.listaFis = ["Introdução à Física", "Pré-Cálculo", "Psicologia da Aprendizagem",
                         "Álgebra Vetorial e Geometria Analítica", "Língua Portuguesa I",
                         "Metodologia do Trabalho Científico", "História da Educação", "Inglês Instrumental",
                         "Filosofia da Educação", "Química Geral", "Sociologia da Educação",
                         "Educação em Direitos Humanos", "Educação Ambiental e Sustentabilidade", "Didática Geral",
                         "Políticas e Gestão Educacional", "Prática de Ensino I", "Física Moderna",
                         "Educação em Diversidade", "Optativa I", "Optativa II", "Física Básica I",
                         "Física Experimental I", "Cálculo Diferencial e Integral I", "Álgebra Linear",
                         "Língua Portuguesa II", "Didática Aplicada ao Ensino de Física", "Prática de Ensino II",
                         "Mecânica Quântica", "Libras", "Estágio Supervisionado I", "Física Experimental II",
                         "Física Básica II", "Cálculo Diferencial e Integral II", "Cálculo Diferencial e Integral III",
                         "TCC", "Prática de Ensino III", "Física Básica III", "Física Experimental III",
                         "Computação Aplicada à Física", "Termodinâmica", "Estágio Supervisionado II",
                         "Prática de Lab. e Inst. para o Ens. de Fís. I", "Física Matemática I", "Prática de Ensino IV",
                         "Física Básica IV", "Eletromagnetismo", "Física Experimental IV", "Mecânica Estatística",
                         "Estágio Supervisionado III", "Prática de Lab. e Inst. para o Ens. de Fís. II",
                         "Mecânica Analítica", "Evolução do Pensamento Científico", "Física Moderna Experimental",
                         "Estágio Supervisionado IV"]
        self.listaEdi = ["Informática Básica", "Inglês Instrumental", "Português Instrumental", "Química Aplicada",
                         "Cálculo Diferencial e Integral I", "Álgebra Vetorial e Geometria Analítica",
                         "Desenho Técnico", "Introdução a Construção Edifícios", "Metodologia da Pesquisa Científica",
                         "Matemática Financeira Aplicada", "Instalações Especiais", "Formação do Empreendedor",
                         "Legislação Aplicada", "Relações Humanas no Trabalho", "Trabalho de Conclusão de Curso",
                         "Estágio Supervisionado", "Libras (optativa)", "Materiais de Construção I", "Física I",
                         "Cálculo Diferencial e Integral II", "Estatística Aplicada", "Des. Assist. por Computador I",
                         "Topografia I", "Desenho e Projeto Arquitetônico", "Gestão Ambiental",
                         "Administração de Custos", "Materiais de Construção II", "Especificações e Orcamentos I",
                         "Resistência dos Materiais", "Instalações Hidrossanitárias", "Instalações Elétricas Pred.",
                         "Física II", "Des. Assist. por Computador II", "Segurança do Trabalho", "Topografia II",
                         "Técnicas Construtivas I", "Mecânica dos Solos", "Especificações e Orcamentos II",
                         "Estruturas de Concreto I", "Estruturas Metálicas", "Estruturas de Madeira",
                         "Planej. Gestão e Controle de Obra", "Técnicas Construtivas II", "Avaliação Pós-ocupação",
                         "Fundações e Sistemas de Contenção", "Gestão da Qualidade e Produtividade",
                         "Estruturas de Concreto II", "Patologia das Construções", "Manutenção Predial"]
        self.listaLet = ["Introdução aos Estudos Literários", "Introdução à Linguistica",
                         "Leitura e Produção de Texto I", "Informática Básica", "Fundamentos da Educação a Distância",
                         "Inglês Instrumental", "História da Educação Brasileira",
                         "Fundamentos da Linguística Românica", "Metodologia da Pesquisa Científica",
                         "Psicologia da Aprendizagem", "Seminário de Pesquisa Interdisciplinar I", "Didática",
                         "Língua Brasileira de Sinais (LIBRAS)", "Educação Inclusiva", "Gestão Educacional",
                         "Tópicos em Projetos Especiais", "Educação e Direitos Humanos",
                         "Educação Ambiental e Interdisciplinaridade", "Teoria Literária I", "Literatura e Ensino",
                         "Morfologia da Língua Portuguesa", "Linguística I", "Leitura e Produção de Texto II",
                         "Filosofia da Educação", "Sociologia da Educação", "História da Língua Portuguesa",
                         "Seminário de Pesquisa Interdisciplinar II", "Seminário de Pesquisa Interdisciplinar III",
                         "Seminário de Pesquisa Interdisciplinar IV", "Orientação de Estágio Supervisionado I",
                         "Estrutura e Funcionamento da Educ. Básica",
                         "Língua Portuguesa como segunda língua para surdos (Optativa)", "Teoria Literária II",
                         "Literatura Brasileira I", "Literatura Portuguesa I", "Metodologia do Ensino de Literatura",
                         "Linguística II", "Fonética e Fonologia da Língua Portuguesa", "Aquisição da Linguagem",
                         "Orientação de TCC I", "Orientação de Estágio Supervisionado II", "Estágio Supervisionado I",
                         "Literatura Brasileira II", "Literatura Brasileira III", "Literatura Brasileira IV",
                         "Literaturas Africanas de Língua Portuguesa", "Literatura Brasileira V",
                         "Literatura Infantil e juvenil", "Literatura e Cultura Popular", "Literatura Portuguesa II",
                         "Morfossintaxe", "Semântica da Lingua Portuguesa",
                         "Metodologia do Ensino de Língua Portuguesa", "Sociolinguística", "Pragmática",
                         "Orientação de TCC II", "Orientação de Estágio Supervisionado III",
                         "Estágio Supervisionado II", "Orientação de Estágio Supervisionado IV",
                         "Estágio Supervisionado III"]

    def constroi_matriz(self, g: MeuGrafo):
        ordem = len(g._vertices)
        m = list()
        for i in range(ordem):
            m.append(list())
            for j in range(ordem):
                m[i].append(0)
        return m

    def test_adiciona_aresta(self):
        self.assertTrue(self.g_p.adiciona_aresta('a10', 'J', 'C'))
        a = ArestaDirecionada("zxc", self.g_p.get_vertice("C"), self.g_p.get_vertice("Z"))
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

    def test_remove_vertice(self):
        self.assertTrue(self.g_p.remove_vertice("J"))
        with self.assertRaises(VerticeInvalidoError):
            self.g_p.remove_vertice("J")
        with self.assertRaises(VerticeInvalidoError):
            self.g_p.remove_vertice("K")
        self.assertTrue(self.g_p.remove_vertice("C"))
        self.assertTrue(self.g_p.remove_vertice("Z"))

    def test_remove_aresta(self):
        self.assertTrue(self.g_p.remove_aresta("a1"))
        self.assertFalse(self.g_p.remove_aresta("a1"))
        self.assertTrue(self.g_p.remove_aresta("a7"))
        self.assertFalse(self.g_c.remove_aresta("a"))
        self.assertTrue(self.g_c.remove_aresta("a6"))
        self.assertTrue(self.g_c.remove_aresta("a1", "J"))
        self.assertTrue(self.g_c.remove_aresta("a5", "C"))
        with self.assertRaises(VerticeInvalidoError):
            self.g_p.remove_aresta("a2", "X", "C")
        with self.assertRaises(VerticeInvalidoError):
            self.g_p.remove_aresta("a3", "X")
        with self.assertRaises(VerticeInvalidoError):
            self.g_p.remove_aresta("a3", v2="X")

    def test_eq(self):
        self.assertEqual(self.g_p, self.g_p2)
        self.assertNotEqual(self.g_p, self.g_p3)
        self.assertNotEqual(self.g_p, self.g_p_sem_paralelas)
        self.assertNotEqual(self.g_p, self.g_p4)

    def test_vertices_nao_adjacentes(self):
        self.assertEqual(set(self.g_p.vertices_nao_adjacentes()),
                         {'J-E', 'J-P', 'J-M', 'J-T', 'J-Z', 'C-J', 'C-T', 'C-Z', 'C-M', 'C-P', 'E-C', 'E-J', 'E-P',
                          'E-M', 'E-T', 'E-Z', 'P-J', 'P-E', 'P-M', 'P-T', 'P-Z', 'M-J', 'M-E', 'M-P', 'M-Z', 'T-J',
                          'T-M', 'T-E', 'T-P', 'Z-J', 'Z-C', 'Z-E', 'Z-P', 'Z-M', 'Z-T'})

        self.assertEqual(set(self.g_c.vertices_nao_adjacentes()), {'C-J', 'C-E', 'C-P', 'E-J', 'E-P', 'P-J'})
        self.assertEqual(self.g_c3.vertices_nao_adjacentes(), [])
        self.assertEqual(set(self.g_e.vertices_nao_adjacentes()),
                         {'A-D', 'A-E', 'B-A', 'B-C', 'B-D', 'B-E', 'C-E', 'D-C', 'D-A', 'E-D', 'E-C'})

    def test_ha_laco(self):
        self.assertFalse(self.g_p.ha_laco())
        self.assertFalse(self.g_p_sem_paralelas.ha_laco())
        self.assertFalse(self.g_c2.ha_laco())
        self.assertTrue(self.g_l1.ha_laco())
        self.assertTrue(self.g_l2.ha_laco())
        self.assertTrue(self.g_l3.ha_laco())
        self.assertTrue(self.g_l4.ha_laco())
        self.assertTrue(self.g_l5.ha_laco())
        self.assertTrue(self.g_e.ha_laco())

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
        self.assertEqual(self.g_e.grau('C'), 5)
        self.assertEqual(self.g_e.grau('D'), 5)

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
        self.assertTrue(self.g_e.ha_paralelas())

    def test_arestas_sobre_vertice(self):
        self.assertEqual(set(self.g_p.arestas_sobre_vertice('J')), {'a1'})
        self.assertEqual(set(self.g_p.arestas_sobre_vertice('C')), {'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7'})
        self.assertEqual(set(self.g_p.arestas_sobre_vertice('M')), {'a7', 'a8'})
        self.assertEqual(set(self.g_l2.arestas_sobre_vertice('B')), {'a1', 'a2', 'a3'})
        self.assertEqual(set(self.g_d.arestas_sobre_vertice('C')), set())
        self.assertEqual(set(self.g_d.arestas_sobre_vertice('A')), {'asd'})
        with self.assertRaises(VerticeInvalidoError):
            self.g_p.arestas_sobre_vertice('A')
        self.assertEqual(set(self.g_e.arestas_sobre_vertice('D')), {'5', '6', '7', '8'})

    def test_warshall(self):
        self.assertEqual(self.g_p.warshall(), self.g_p_m)
        self.assertEqual(self.g_e.warshall(), self.g_e_m)
        self.assertEqual(self.g_w1.warshall(), self.g_w1_m)
        self.assertEqual(self.g_w2.warshall(), self.g_w2_m)
        self.assertEqual(self.g_w3.warshall(), self.g_w3_m)
        self.assertEqual(self.g_w4.warshall(), self.g_w4_m)

    def test_dijkstra(self):
        self.assertEqual(['J', 'a1', 'C'], self.g_p.dijkstra('J', 'C'))
        self.assertEqual(None, self.g_p.dijkstra('C', 'J'))
        self.assertTrue(self.g_p.dijkstra('J', 'E') in
                        [['J', 'a1', 'C', 'a2', 'E'],
                         ['J', 'a1', 'C', 'a3', 'E']])
        self.assertEqual(None, self.g_p.dijkstra('E', 'C'))
        # existem dois caminhos possíveis entre M e C
        self.assertEqual(['M', 'a7', 'C'], self.g_p.dijkstra('M', 'C'))

        # dois caminhos possíveis, mesmo comprimento, pesos diferentes
        self.assertEqual(['A', 'l1', 'B', 'l3', 'D'],
                         self.g_dijkstra.dijkstra('A', 'D'))
        # três caminhos possíveis, os de menor peso têm mais arestas
        self.assertEqual(['A', 'l3', 'D', 'l4', 'C'],
                         self.g_dijkstra2.dijkstra('A', 'C'))
        # dois caminhos possíveis, o de menor peso tem mais arestas
        self.assertEqual(['C', 'l5', 'E', 'l6', 'G', 'l7', 'F'],
                         self.g_dijkstra2.dijkstra('C', 'F'))
        self.assertEqual(None, self.g_dijkstra2.dijkstra('C', 'A'))
        self.assertEqual(None, self.g_dijkstra2.dijkstra('F', 'C'))

    def test_khan(self):
        self.assertEqual(self.eng_comp.khan(), self.listaEng)
        self.assertEqual(self.telematica.khan(), self.listaTel)
        self.assertEqual(self.matematica.khan(), self.listaMat)
        self.assertEqual(self.fisica.khan(), self.listaFis)
        self.assertEqual(self.const_edificios.khan(), self.listaEdi)
        self.assertEqual(self.letras.khan(), self.listaLet)
