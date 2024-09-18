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
        