import datetime


class Arquivo:
    def __init__(self, nome="", tipo="", tamanho=0, conteudo=""):
        self.nome = nome
        self.tipo = tipo
        self.tamanho = tamanho
        self.conteudo = conteudo
        self.data = datetime.datetime.now()

    def __str__(self):
        return f"Nome: {self.nome}\nTipo: {self.tipo}\nTamanho: {self.tamanho} bytes\nData de Criação: {self.data}\n"


class Diretorio:
    def __init__(self, nome="", tipo=""):
        self.nome = nome
        self.tipo = tipo
        self.descricao = ""
        self.arquivos = []

    def adicionar_arquivo(self, arquivo):
        self.arquivos.append(arquivo)

    def remover_arquivo(self, arquivo):
        if arquivo in self.arquivos:
            self.arquivos.remove(arquivo)

    def buscar(self, nome):
        for arquivo in self.arquivos:
            if arquivo.nome == nome:
                return arquivo
        return None

    def listar_arquivos(self):
        for arquivo in self.arquivos:
            print(arquivo)

# Exemplo de uso
# foto1 = Arquivo("Zeus", "imagem", 32, "conteúdo da imagem")
# foto2 = Arquivo("Paisagem", "imagem", 133, "conteúdo da paisagem")

# imagens = Diretorio("Imagens", "diretorio")
# imagens.adicionar_arquivo(foto1)
# imagens.adicionar_arquivo(foto2)

# imagens.listar_arquivos()
