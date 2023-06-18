import datetime

class Arquivo:
    def __init__(self, nome, tipo, descricao, tamanho, conteudo, data):
        self.nome = nome
        self.tipo = tipo
        self.descricao = descricao
        self.tamanho = tamanho
        self.conteudo = conteudo
        self.data = data
        self.esquerda = None
        self.direita = None
        self.altura = 1

    def __str__(self):
        return f'''
Nome: {self.nome}
Descrição: {self.descricao}
Tamanho: {self.tamanho}
Conteúdo: {self.conteudo}
Data de criação: {self.data}'''


class Diretorio:
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo
        self.raiz = None

    def adicionar_arquivo(self, arquivo):
        self.raiz = self._inserir(self.raiz, arquivo)

    def remover_arquivo(self, arquivo):
        self.raiz = self._remover(self.raiz, arquivo)

    def buscar(self, elemento):
        return self._buscar(self.raiz, elemento)

    def listar_arquivos(self):
        self._listar_in_order(self.raiz)

    def _obter_altura(self, nodo):
        if nodo is None:
            return 0
        return nodo.altura

    def _obter_fator_balanceamento(self, nodo):
        if nodo is None:
            return 0
        return self._obter_altura(nodo.esquerda) - self._obter_altura(nodo.direita)

    def _atualizar_altura(self, nodo):
        if nodo is None:
            return
        nodo.altura = 1 + max(self._obter_altura(nodo.esquerda), self._obter_altura(nodo.direita))

    def _rotacao_esquerda(self, nodo_desbalanceado):
        nodo_direita = nodo_desbalanceado.direita
        nodo_direita_esquerda = nodo_direita.esquerda

        nodo_direita.esquerda = nodo_desbalanceado
        nodo_desbalanceado.direita = nodo_direita_esquerda

        self._atualizar_altura(nodo_desbalanceado)
        self._atualizar_altura(nodo_direita)

        return nodo_direita

    def _rotacao_direita(self, nodo_desbalanceado):
        nodo_esquerda = nodo_desbalanceado.esquerda
        nodo_esquerda_direita = nodo_esquerda.direita

        nodo_esquerda.direita = nodo_desbalanceado
        nodo_desbalanceado.esquerda = nodo_esquerda_direita

        self._atualizar_altura(nodo_desbalanceado)
        self._atualizar_altura(nodo_esquerda)

        return nodo_esquerda

    def _balancear_nodo(self, nodo):
        if nodo is None:
            return nodo

        self._atualizar_altura(nodo)

        fator_balanceamento = self._obter_fator_balanceamento(nodo)

        if fator_balanceamento > 1:  # Rotação à direita
            if self._obter_fator_balanceamento(nodo.esquerda) < 0:
                nodo.esquerda = self._rotacao_esquerda(nodo.esquerda)
            return self._rotacao_direita(nodo)

        if fator_balanceamento < -1:  # Rotação à esquerda
            if self._obter_fator_balanceamento(nodo.direita) > 0:
                nodo.direita = self._rotacao_direita(nodo.direita)
            return self._rotacao_esquerda(nodo)

        return nodo

    def _inserir(self, nodo, arquivo):
        if nodo is None:
            return Arquivo(arquivo.nome, arquivo.tipo, arquivo.descricao, arquivo.tamanho, arquivo.conteudo, arquivo.data)

        if arquivo.nome < nodo.nome:
            nodo.esquerda = self._inserir(nodo.esquerda, arquivo)
        else:
            nodo.direita = self._inserir(nodo.direita, arquivo)

        return self._balancear_nodo(nodo)

    def _encontrar_nodo_minimo(self, nodo):
        atual = nodo
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual

    def _remover(self, raiz, arquivo):
        if raiz is None:
            return raiz

        if arquivo.nome < raiz.nome:
            raiz.esquerda = self._remover(raiz.esquerda, arquivo)
        elif arquivo.nome > raiz.nome:
            raiz.direita = self._remover(raiz.direita, arquivo)
        else:
            if raiz.esquerda is None:
                temp = raiz.direita
                raiz = None
                return temp
            elif raiz.direita is None:
                temp = raiz.esquerda
                raiz = None
                return temp
            temp = self._encontrar_nodo_minimo(raiz.direita)
            raiz.nome = temp.nome
            raiz.tipo = temp.tipo
            raiz.descricao = temp.descricao
            raiz.tamanho = temp.tamanho
            raiz.conteudo = temp.conteudo
            raiz.data = temp.data
            raiz.direita = self._remover(raiz.direita, temp)

        return self._balancear_nodo(raiz)

    def _buscar(self, nodo, elemento):
        if nodo is None or nodo.nome == elemento:
            return nodo

        if elemento < nodo.nome:
            return self._buscar(nodo.esquerda, elemento)
        else:
            return self._buscar(nodo.direita, elemento)

    def _listar_in_order(self, nodo):
        if nodo is not None:
            self._listar_in_order(nodo.esquerda)
            if nodo.tipo == 'arquivo':
                print(nodo.nome)
            self._listar_in_order(nodo.direita)


foto1 = Arquivo('Zeus', 'arquivo', 'Deus da mitologia', 32, 'imagem', datetime.datetime.now())
foto2 = Arquivo('Paisagem', 'arquivo', 'Vales verdejantes', 133, 'imagem', datetime.datetime.now())

raiz = Diretorio('Raíz', 'diretorio')
imagens = Diretorio('Imagens', 'diretorio')
downloads = Diretorio('Downloads', 'diretorio')
documentos = Diretorio('Documentos', 'diretorio')
screenshots = Diretorio('Screenshots', 'diretorio')
salvas = Diretorio('Imagens Salvas', 'diretorio')

raiz.adicionar_arquivo(imagens)
raiz.adicionar_arquivo(downloads)
raiz.adicionar_arquivo(documentos)

imagens.adicionar_arquivo(foto1)
imagens.adicionar_arquivo(screenshots)
imagens.adicionar_arquivo(salvas)
imagens.adicionar_arquivo(foto2)

imagens.listar_arquivos()
