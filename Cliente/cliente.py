import socket

class Cliente:
    def __init__(self, ip_servidor, porta) -> None:
        self._ip_servidor = ip_servidor
        self._porta = porta
        self._tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        '''
        Inicializa a execução do cliente
        '''
        cliente = (self._ip_servidor, self._porta)
        try:
            self._tcp.connect(cliente)
            resposta = self._tcp.recv(1024).decode('ascii')
            print(resposta)
            self._menu_interacao()
        except Exception as e:
            print('Erro na conexão: ', e.args)

    def _menu_interacao(self):
        '''
        Implementa opções de interação com o cliente
        '''
        try:
            while True:
                print("\nOpções:\n1 - Calcular IMC\n2 - Cadastrar na Fila de Espera\n3 - Ver posição na Fila de Espera\nx - Sair")
                opcao = input("Escolha uma opção: ")

                if opcao == '1':
                    self._metodo_imc()
                elif opcao == '2':
                    self._cadastrar_fila_espera()
                elif opcao == '3':
                    self._ver_fila_espera()
                elif opcao.lower() == 'x':
                    print("Encerrando a conexão...")
                    self._tcp.send(bytes("ENCERRAR\n", 'ascii'))
                    reply = self._tcp.recv(1024).decode('ascii')
                    print(reply) # Informa ao servidor que o cliente deseja encerrar
                    break
                else:
                    print("Opção inválida! Tente novamente.")
            
            self._tcp.close()

        except Exception as e:
            print("Erro ao realizar a comunicação com o servidor", e)
            self._tcp.send(bytes("#ERRO#\n", 'ascii'))  # Envia erro para o servidor

    def _metodo_imc(self):
        '''
        Método que implementa as requisições do cliente
        '''
        try:
            peso = input("Digite o seu peso (kg): ")
            altura = input("Digite a sua altura (cm): ")
            if peso and altura:  # Verifica se os dados foram preenchidos
                dados = f"CALCULO_IMC=> PESO(kg), ALTURA(cm)|{peso},{altura}\n"  # Formato de envio
                self._tcp.send(bytes(dados, 'ascii'))
                resposta = self._tcp.recv(1024)
                print(resposta.decode('ascii'))
            else:
                print("Dados inválidos. Tente novamente.")
        except Exception as e:
            print("Erro ao enviar dados para o cálculo de IMC: ", e)

    def _cadastrar_fila_espera(self):
        '''
        Método para enviar o nome e telefone para cadastro na fila de espera
        '''
        try:
            nome = input("Digite o seu nome: ")
            telefone = input("Digite o seu telefone: ")
            if nome and telefone:  # Verifica se os dados foram preenchidos
                dados = f"CADASTRAR=> NOME, TELEFONE|{nome},{telefone}\n"  # Formato de envio
                self._tcp.send(bytes(dados, 'ascii'))
                resposta = self._tcp.recv(1024)
                print(resposta.decode('ascii'))
            else:
                print("Dados inválidos. Tente novamente.")
        except Exception as e:
            print("Erro ao enviar dados de cadastro: ", e)

    def _ver_fila_espera(self):
        '''
        Método para solicitar a posição na fila de espera ao servidor
        '''
        try:
            nome = input("Digite o seu nome: ")
            telefone = input("Digite o seu telefone: ")
            if nome and telefone:  # Verifica se os dados foram preenchidos
                dados = f"VER_POSICAO|{nome},{telefone}"
                self._tcp.send(bytes(dados, 'utf-8'))  # Envia a solicitação para o servidor
                resposta = self._tcp.recv(1024).decode('utf-8')  # Recebe a resposta do servidor
                print(resposta)
            else:
                print("Dados invalidos. Tente novamente.")
        except Exception as e:
            print("Erro ao solicitar a posicao na fila de espera: ", e)

