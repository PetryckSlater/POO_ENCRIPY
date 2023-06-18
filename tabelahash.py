import datetime

class Diretorio:
    def __init__(self, nome="", tipo="Diretorio"):
        self.nome = nome
        self.tipo = tipo
    
    def __str__(self):
        return f"Nome: {self.nome}\nTipo: {self.tipo}"

class Arquivo:
    def __init__(self, nome="", tipo="", tamanho=0, conteudo=""):
        self.nome = nome
        self.tipo = tipo
        self.tamanho = tamanho
        self.conteudo = conteudo
        self.data = datetime.datetime.now()

    def __str__(self):
        return f"Nome: {self.nome}\nTipo: {self.tipo}\nTamanho: {self.tamanho} bytes\nData de Criação: {self.data}\n"


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash_function(self, key):
        return hash(key) % self.size

    def adicionar_arquivo(self, arquivo):
        index = self._hash_function(arquivo.nome)
        self.table[index].append(arquivo)

    def remover_arquivo(self, arquivo):
        index = self._hash_function(arquivo.nome)
        for i, file in enumerate(self.table[index]):
            if file.nome == arquivo.nome:
                self.table[index].pop(i)
                break

    def buscar(self, nome):
        index = self._hash_function(nome)
        for arquivo in self.table[index]:
            if arquivo.nome == nome:
                return arquivo
        return None

    def listar_arquivos(self):
        for slot in self.table:
            for arquivo in slot:
                print(arquivo)


root = Diretorio("~")
arquivo1 = Arquivo("Arquivo1.txt", "txt", 100, "Conteúdo do arquivo 1")
arquivo2 = Arquivo("Arquivo2.jpg", "jpg", 200, "Conteúdo do arquivo 2")
arquivo3 = Arquivo("Arquivo3.docx", "docx", 150, "Conteúdo do arquivo 3")
tabela_hash = HashTable(10)

# tabela_hash.adicionar_arquivo(root)
# tabela_hash.adicionar_arquivo(arquivo1)
# tabela_hash.adicionar_arquivo(arquivo2)
# tabela_hash.adicionar_arquivo(arquivo3)

tabela_hash.listar_arquivos()
