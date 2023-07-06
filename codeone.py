import datetime

class Diretorio:
    def __init__(self, nome="", tipo="Diretorio"):
        self.nome = nome
        self.tipo = tipo
        self.subdiretorios = []
        self.arquivos = []

    def adicionar_subdiretorio(self, subdiretorio):
        self.subdiretorios.append(subdiretorio)

    def adicionar_arquivo(self, arquivo):
        self.arquivos.append(arquivo)

    def listar_subdiretorios(self):
        for subdiretorio in self.subdiretorios:
            print(subdiretorio)

    def listar_arquivos(self):
        for arquivo in self.arquivos:
            print(arquivo)

    def __str__(self):
        return f"Nome: {self.nome}\nTipo: {self.tipo}"

class Arquivo:
    def __init__(self, nome="", tipo="", tamanho=0, conteudo="", diretorio=None):
        self.nome = nome
        self.tipo = tipo
        self.tamanho = tamanho
        self.conteudo = conteudo
        self.data = datetime.datetime.now()
        self.diretorio = diretorio

    def __str__(self):
        return f"Nome: {self.nome}\nTipo: {self.tipo}\nTamanho: {self.tamanho} bytes\nData de Criação: {self.data}\nDiretório: {self.diretorio}"

class Interface:
    def __init__(self, user, password):
        self.user = user
        self.password = password
        self.diretorio_padrao = Diretorio("Diretório Padrão", "Diretório")

    def login(self):
        if self.user != 'ifpb':
            return 'Erro! Usuário inválido'
        elif self.password != 'ifpb':
            return 'Erro! Senha inválida'
        else:
            return 'Login bem-sucedido'

    def explorador(self):
        while True:
            print("1. Adicionar arquivo")
            print("2. Remover arquivo")
            print("3. Buscar arquivo")
            print("4. Listar arquivos do diretório")
            print("5. Criar diretório")
            print("6. Listar subdiretórios")
            print("7. Listar arquivos de um diretório")
            print("8. Sair")
            opcao = int(input("Escolha uma opção: "))

            if opcao == 1:
                nome = input("Digite o nome do arquivo: ")
                tipo = input("Digite o tipo do arquivo: ")
                tamanho = int(input("Digite o tamanho do arquivo em bytes: "))
                conteudo = input("Digite o conteúdo do arquivo: ")

                diretorio = input("Digite o nome do diretório para adicionar o arquivo (ou deixe em branco para o diretório padrão): ")
                if diretorio:
                    arquivo = Arquivo(nome, tipo, tamanho, conteudo, diretorio)
                    self.adicionar_arquivo_em_diretorio(arquivo, diretorio)
                else:
                    arquivo = Arquivo(nome, tipo, tamanho, conteudo, self.diretorio_padrao)
                    self.diretorio_padrao.adicionar_arquivo(arquivo)
                
                print("Arquivo adicionado com sucesso!")

            elif opcao == 2:
                nome = input("Digite o nome do arquivo a ser removido: ")
                arquivo = self.buscar_arquivo(nome)
                if arquivo:
                    self.remover_arquivo(arquivo)
                    print("Arquivo removido com sucesso!")
                else:
                    print("Arquivo não encontrado.")

            elif opcao == 3:
                nome = input("Digite o nome do arquivo a ser buscado: ")
                arquivo = self.buscar_arquivo(nome)
                if arquivo:
                    print(arquivo)
                else:
                    print("Arquivo não encontrado.")

            elif opcao == 4:
                self.diretorio_padrao.listar_arquivos()

            elif opcao == 5:
                nome = input("Digite o nome do diretório: ")
                diretorio = Diretorio(nome, "Diretório")
                self.diretorio_padrao.adicionar_subdiretorio(diretorio)
                print("Diretório criado com sucesso!")

            elif opcao == 6:
                self.diretorio_padrao.listar_subdiretorios()

            elif opcao == 7:
                nome_diretorio = input("Digite o nome do diretório para listar os arquivos: ")
                diretorio = self.buscar_diretorio(nome_diretorio)
                if diretorio:
                    diretorio.listar_arquivos()
                else:
                    print("Diretório não encontrado.")

            elif opcao == 8:
                break

            else:
                print("Opção inválida. Tente novamente.")

if __name__ == '__main__':
    user = input("Digite o nome de usuário: ")
    password = input("Digite a senha: ")

    interface = Interface(user, password)
    resultado = interface.login()
    print(resultado)

    if resultado == 'Login bem-sucedido':
        interface.explorador()
