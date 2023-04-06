from bibgrafo.grafo_matriz_adj_nao_dir import GrafoMatrizAdjacenciaNaoDirecionado
from bibgrafo.grafo_errors import *


class MeuGrafo(GrafoMatrizAdjacenciaNaoDirecionado):

    def vertices_nao_adjacentes(self):
        '''
        Provê uma lista de vértices não adjacentes no grafo. A lista terá o seguinte formato: [X-Z, X-W, ...]
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Uma lista com os pares de vértices não adjacentes
        '''

        verticesNaoAdjacentes = set()
        # Se é completo não tem vertices não adjacentes
        if self.eh_completo():
            return verticesNaoAdjacentes
        else:
            # Percorre todas as linhas da matriz
            for i in range(len(self.vertices)):
                # Percorre todas as colunas da matriz + 1, que é para verificar só a metade da matriz
                # Facilitando meu trabalho de programar mais ifs, e de trabalho pra máquina :D
                for j in range(i+1, len(self.vertices)):
                    # Se o dicionário for vazio, não tem arestas nele ou seja = vertices não adjacentes
                    if len(self.matriz[i][j]) == 0:
                        verticesNaoAdjacentes.add(f"{self.vertices[i].rotulo}-{self.vertices[j].rotulo}")
        return verticesNaoAdjacentes

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''

        # Passa por todas as linhas da matriz
        for i in range(len(self.vertices)):
            # Passa pela diagonal da matriz para descobrir se tem laço
            if len(self.matriz[i][i]) > 0:
                return True
        return False

    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        # Verifica se o vertice passado Existe
        if self.existe_rotulo_vertice(V):
            grau = 0
            # Passa pelas linhas da matriz
            for i in range(len(self.vertices)):
                # Verifica se tem laço na matriz
                if self.matriz[i][i] != 0 and self.vertices[i].rotulo == V:
                    grau += 2 * len(self.matriz[i][i])
                # Conta tbm todos as arestas conectadas nos vertices, para calcular o grau
                elif len(self.matriz[i][self.vertices.index(self.get_vertice(V))]) != 0:
                    grau += len(self.matriz[i][self.vertices.index(self.get_vertice(V))])
            return grau
        else:
            raise VerticeInvalidoError(f"Vértice {V} não existe no grafo.")
    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        # Passa pelas linahs da matriz
        for i in range(len(self.vertices)):
            # Passa pelas colunas da matriz
            for j in range(len(self.vertices)):
                # Se o dicionario da celula da matriz for maior que um, é porque tem paralelas
                if len(self.matriz[i][j]) > 1:
                    return True
        return False

    def arestas_sobre_vertice(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: O vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError("Vértice {} não existe no grafo".format(V))

        v_obj = self.get_vertice(V)
        i_v = self.indice_do_vertice(v_obj)
        arestas = set()
        for j in range(len(self.vertices)):
            for a in self.matriz[i_v][j]:
                arestas.add(a)
        return arestas

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        # Se tem laço já não é completo
        if self.ha_laco():
            return False
        else:
            totalVertices = len(self.vertices)
            verdade = 0
            # Passa por todas as linhas da matriz
            for i in range(len(self.vertices)):
                # Se o grau do vertice for igual ao N° de vertices totais - 1, então adciona uma condição verdadeira
                if self.grau(self.vertices[i].rotulo) == (totalVertices-1):
                    verdade += 1
                else:
                    return False
            # Se a condição verdade for igual ao total de vertices, é porque o grau é completo
            if verdade == totalVertices:
                return True