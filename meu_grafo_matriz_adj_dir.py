from bibgrafo.grafo_matriz_adj_dir import *
from bibgrafo.grafo_errors import *


class MeuGrafo(GrafoMatrizAdjacenciaDirecionado):

    def vertices_nao_adjacentes(self):
        '''
        Provê uma lista de vértices não adjacentes no grafo. A lista terá o seguinte formato: [X-Z, X-W, ...]
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Uma lista com os pares de vértices não adjacentes
        '''
        pass

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
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
        pass

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        pass

    def arestas_sobre_vertice(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: O vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        pass

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        pass

    def warshall(self):
        # Criação da matriz E
        E = []

        # Verifica se existe uma aresta entre os vértices i e j na matriz
        # Se existir, atribui o valor 1, caso contrário, atribui o valor 0
        E = [[1 if len(self.matriz[i][j]) >= 1 else 0 for j in range(len(self.vertices))] for i in
             range(len(self.vertices))]

        # Algoritmo de Warshall
        # Percorre a matriz E para atualizar os caminhos mínimos entre os vértices
        for i in range(len(self.vertices)):
            for j in range(len(self.vertices)):
                if E[j][i] == 1:
                    # Compara os valores de E[j][k] e E[i][k] para cada k
                    # Atualiza E[j][k] com o maior valor entre os dois
                    for k in range(len(self.vertices)):
                        E[j][k] = max(E[j][k], E[i][k])

        # Retorna a matriz E resultante após a aplicação do algoritmo de Warshall
        return E

    def verticeInverso(self, aresta, V=''):
        # Retorne o rótulo do vértice oposto ao dado vértice na dada aresta

        if aresta.v1.rotulo == V:  # se o vértice V for igual ao rótulo do vértice v1 da aresta
            return aresta.v2.rotulo  # retorna o rótulo do vértice v2 da aresta
        elif aresta.v2.rotulo == V:  # se o vértice V for igual ao rótulo do vértice v2 da aresta
            return aresta.v1.rotulo  # se V não for igual a nenhum dos vértices da aresta
        else:  # da erro
            raise VerticeInvalidoError

    def arestasConectadas(self, v):
        # Encontra o índice do vértice com rótulo v
        i = self.indice_do_vertice(Vertice(v))

        # Cria um dicionário para armazenar as arestas incidentes no vértice de rótulo v
        arestasIncidentes = {}

        # Passa por todos os vértices e verifica se a aresta na posição (i,j) da matriz de adj é não vazia
        for j in range(len(self.vertices)):
            if len(self.matriz[i][j]) != 0:
                # Se for não vazia, passa sobre as arestas e guarda elas no dicionário de arestas que estão conectadas
                for rot_aresta in self.matriz[i][j]:
                    arestasIncidentes[rot_aresta] = self.matriz[i][j][rot_aresta]

        # Retorna o dicionário com as arestas conectas no vértice passado
        return arestasIncidentes

    def dijkstra(self, vi, vf):
        # Inicializa os dicionários de controle para cada vértice do grafo
        verticesVisitados = {}
        pesoMinimo = {}
        verticeAnterior = {}

        infinito = float('inf')

        for v in self.vertices:
            verticesVisitados[v.rotulo] = False
            pesoMinimo[v.rotulo] = infinito  # Define o peso inicial para cada vértice como infinito
            verticeAnterior[v.rotulo] = None
        pesoMinimo[vi] = 0  # Define o peso do vértice inicial como 0
        verticesVisitados[vi] = True
        verciteAtual = vi

        # Executa o algoritmo de Dijkstra até chegar no vértice final
        while verciteAtual != vf:
            arestasSaida = self.arestasConectadas(verciteAtual)
            for rot_aresta in arestasSaida:
                aresta = arestasSaida[rot_aresta]
                oposto = self.verticeInverso(aresta, verciteAtual)
                if verticesVisitados[oposto]:
                    continue
                if pesoMinimo[oposto] > pesoMinimo[verciteAtual] + aresta.peso:
                    pesoMinimo[oposto] = pesoMinimo[verciteAtual] + aresta.peso
                    verticeAnterior[oposto] = [verciteAtual, rot_aresta]

            # Encontra o vértice com o menor peso e ainda não visitado
            proximo, menorPeso = None, infinito
            for v in self.vertices:
                if verticesVisitados[v.rotulo] or pesoMinimo[v.rotulo] == infinito:
                    continue
                if pesoMinimo[v.rotulo] < menorPeso:
                    menorPeso = pesoMinimo[v.rotulo]
                    proximo = v.rotulo
            if not proximo:
                return None

            # Atualiza o vértice atual e marca como visitado
            verticesVisitados[proximo] = True
            verciteAtual = proximo

        # Reconstrói o caminho mais curto a partir do vértice final
        caminho = [verciteAtual]
        while verciteAtual != vi:
            caminho = verticeAnterior[verciteAtual] + caminho
            verciteAtual = verticeAnterior[verciteAtual][0]
        return caminho

    def khan(self):
        grafo = deepcopy(self)
        lista_top = []
        fontes = [vertice.rotulo for vertice in grafo.vertices if grafo.ehFonte(vertice)]

        while fontes:
            vertice_fonte = fontes.pop(0)
            lista_top.append(vertice_fonte)

            indice_vertice_fonte = grafo.vertices.index(grafo.get_vertice(vertice_fonte))

            for j in range(len(grafo.vertices)):
                matriz_vertice = grafo.matriz[indice_vertice_fonte][j]
                if matriz_vertice:
                    matriz_vertice.clear()
                    grafo.matriz[j][indice_vertice_fonte].clear()

            for i, vertice in enumerate(grafo.vertices):
                if grafo.ehFonte(vertice) and vertice.rotulo not in lista_top and vertice.rotulo not in fontes:
                    fontes.append(vertice.rotulo)

        print(lista_top)
        return lista_top

    def ehFonte(self, v=""):
        index = self.vertices.index(v)
        for i in range(len(self.vertices)):
            if any(self.matriz[i][index]):
                return False
        return True
