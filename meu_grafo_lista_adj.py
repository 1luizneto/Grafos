from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from bibgrafo.grafo_errors import *


class MeuGrafo(GrafoListaAdjacencia):

    def vertices_nao_adjacentes(self):
        """
        Provê um conjunto de vértices não adjacentes no grafo.
        O conjunto terá o seguinte formato: {X-Z, X-W, ...}
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Um objeto do tipo set que contém os pares de vértices não adjacentes
        """

        verticesNaoAdjacentes = set()
        vertices = self.vertices
        arestas = self.arestas

        '''
        1° Verfifica se pra todo Vertice1 existe adjacencia em todos os vertices
        Logo em seguida, tem um for que verifica se para cada aresta ele conecta no vertice
        '''
        for vertice1 in vertices:
            for vertice2 in vertices:
                adjacente = False
                for arestaAtual in arestas:
                    if arestas[arestaAtual].eh_ponta(vertice1) and arestas[arestaAtual].eh_ponta(
                            vertice2): adjacente = True

                vertices1 = f"{vertice1}-{vertice2}"  # Adiciona sempre os vertices atuais pra comprarar e evitar erros
                verticesInvertido = f"{vertice2}-{vertice1}"

                if vertice1 != vertice2:  # O vertice 1 não pode ser igual ao vertice 2, ex: J,J
                    if not adjacente:  # O vertice não pode ser adjacente
                        if vertices1 not in verticesNaoAdjacentes:  # O vertice não já pode ter sido adcionada uma vez
                            if verticesInvertido not in verticesNaoAdjacentes: verticesNaoAdjacentes.add(
                                vertices1)  # Nem na forma "inversa"

        return verticesNaoAdjacentes

    def ha_laco(self):
        """
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        """

        arestas = self.arestas

        '''
        O programa identifica somente se na aresta[a] os vertices que elas conectam são iguais
        '''
        for a in arestas:
            if arestas[a].v1 == arestas[a].v2:
                return True
        return False

    def grau(self, V=''):
        """
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoError se o vértice não existe no grafo
        """

        if self.existe_rotulo_vertice(V):  # Primeiro verifica se o vértice pertence ao grafo
            grau = 0
            for a in self.arestas:  # For responsável por passar por todas as listas de arestas
                if self.arestas[a].v1.rotulo == V:  # Aresta["a1"].vJ.rotulo
                    grau += 1
                if self.arestas[a].v2.rotulo == V:  # Aresta["a1"].vC (esse v1, v2 é o vertice 1 e o 2 da aresta, já que uma aresta não pode existir sem dois vértices)
                    grau += 1
        else:
            raise VerticeInvalidoError  # Se o vértice não pertencer ao grafo, retorne o erro

        return grau

    def ha_paralelas(self):
        """
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        """

        count = 0
        for a in self.arestas:
            '''
            # Várievel criada pra pegar os vertices
            # V1 e V2 para ser feito as comparações
            '''
            vertice1 = self.arestas[a].v1.rotulo, self.arestas[a].v2.rotulo

            for b in self.arestas:
                '''
                Esse segundo for é responsável por verificar se de fato há pararelas, 
                porque ele compara o vertice 1, com todos os vertices do grafo até achar um igual 
                se retornar count == 2 é porque tem paralela
                Tem que retornar 2 porque sempre a primeira comparação é verdadeira 
                '''
                vertice2 = self.arestas[b].v1.rotulo, self.arestas[b].v2.rotulo
                if vertice1 == vertice2:
                    count += 1

            if count == 2:
                return True
            else:
                count = 0

        return False

    def arestas_sobre_vertice(self, V):
        """
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: Um string com o rótulo do vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        """

        listaA = set()

        if self.existe_rotulo_vertice(V):
            for v1 in self.vertices:
                for a in self.arestas:  # Verifica a partir de um vertice V, quais arestas incidem sobre o vértice
                    if self.arestas[a].v1.rotulo == V or self.arestas[a].v2.rotulo == V:
                        listaA.add(f"{a}")
                return listaA
        else:
            raise VerticeInvalidoError

    def eh_completo(self):
        """
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        """

        qV = self.vertices
        qV = len(qV)
        qA = self.arestas
        qA = len(qA)
        '''
        Várieveis criadas para saber a quantidade de vertices de arestas
        If quantidade de Arestas for igual a n*(n-1)/2, onde n é o número de vertices no grafo
        Se o número total de arestas for igual a *(n-1)/2, o grafo é completo
        '''
        if qA == (qV * (qV - 1) / 2):
            return True

        return False

    def dfs(self):
        # Cria um novo grafo para guardar a árvore DFS e pega a raiz como o primeiro vértice do grafo escolhido
        arvoreDFS = MeuGrafo()
        raiz = self.vertices[0].rotulo
        arvoreDFS.adiciona_vertice(raiz)

        # Inicializa um conjunto de vértices visitados
        visitados = set()

        # Chama o método de busca pra preencher a árvore DFS
        self.dfsBusca(raiz, arvoreDFS, visitados)

        # Retorna a árvore DFS "final"
        return arvoreDFS

    # Método de busca recursivo
    def dfsBusca(self, Pai, arvoreDFS, visitados):
        # Adiciona o vértice pai ao conjunto de vértices visitados
        visitados.add(Pai)

        # Obtém todas as arestas que saem do vértice pai e guarda numa variavel
        arestasdoPai = self.arestas_sobre_vertice(Pai)
        rotulosPai = list(arestasdoPai)
        rotulosPai.sort()

        # Iteração sobre todas as arestas
        for aresta in rotulosPai:
            # Verifica se o vértice ligado à aresta ainda não foi visitado e se ainda não foi adicionado à árvore DFS
            if not arvoreDFS.existe_rotulo_vertice(aresta):

                # Descobre qual vértice é o filho do vértice pai
                if Pai == self.arestas[aresta].v1.rotulo:
                    Filho = self.arestas[aresta].v2.rotulo
                else:
                    Filho = self.arestas[aresta].v1.rotulo
                    
                # Verifica se o filho ainda não foi visitado
                if Filho not in visitados:
                    # Adiciona o filho à árvore DFS e cria uma nova aresta
                    arvoreDFS.adiciona_vertice(Filho)
                    arvoreDFS.adiciona_aresta(self.arestas[aresta])
                    
                    # Chama a função dnv para preencher o subgrafo DFS do filho
                    self.dfsBusca(Filho, arvoreDFS, visitados)

        # Retorna a árvore DFS
        return arvoreDFS
