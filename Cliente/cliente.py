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
            print('Conexão estabelecida') 
            self._metodo()
        except Exception as e:
            print('Erro na conexão: ', e.args)

    def _metodo(self):
        '''
        Método que implementa as requisições do cliente
        '''
        # implementar interação com o cliente
        try:
            dados = ''
            # altura = ''
            while dados != 'x':
                dados = input("Calculadora IMC\n (digite 'x' para sair)\nDigite o seu peso (kg) e sua altura (cm): ")
                # altura = input("(digite 'x' para sair)/nDigite a sua altura: ")
                if dados == '':
                    continue
                elif dados == 'x':
                    break
                self._tcp.send(bytes(dados, 'ascii'))
                resp = self._tcp.recv(1024)
                print("= ", resp.decode('ascii'))
            self._tcp.close()
        except Exception as e:
            print("Erro ao realizar a comunicação com o servidor", e)
