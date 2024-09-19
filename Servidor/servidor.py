import socket

class Servidor:
    def __init__(self, host, porta) -> None:
        self._host = host
        self._porta = porta
        self._tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        # AF_INET -> especifica a familia internet -> Nosso programa poderá se comunicar com qualquer endereço IPV4
        # SOCK_STREAM -> indicamos que vamos trabalhar com TCP

    def start(self):
        '''
        Inicia a execução do servidor
        '''
        servidor = (self._host, self._porta)
        try:
            self._tcp.bind(servidor)
            self._tcp.listen(1)
            print('O servidor foi iniciado em ', self._host, ':', self._porta)
            while True:
                con, cliente = self._tcp.accept()
                self._servico(con, cliente)
                # con -> objeto socket utilizado para envio e recebimento de dados
                # cliente -> endereço e porta do cliente
        except Exception as e:
            print('Erro ao inicializar o servidor ', e.args)

    def _servico(self, con, cliente):
        '''
        Implementa o serviço de calculadora de IMC
        '''
        try: 
            print ("Atendendo cliente", cliente)
            while True: 
                dados = con.recv(1024)
                dados_d=str(dados.decode('ascii'))  #recebe os dados do cliente no formato bytes; decodifica e remove espaços
                if not dados_d:
                    print(f"Conexão encerrada pelo cliente {cliente}")
                    break 
                print(f"Recebido: {dados}")
                peso, altura = map(float, dados_d.split(',')) #60, 120  #aplica float e atribui a dados 
                altura_f = altura/100
                imc = peso / (altura_f ** 2)
                if imc < 18.5:
                    classificacao = "Abaixo do peso"
                elif 18.5 <= imc < 25:
                    classificacao = "Peso normal"
                elif 25 <= imc < 30:
                    classificacao = "Sobrepeso"
                elif 30 <= imc < 40:
                 classificacao = "Obesidade"
                else:
                    classificacao = "Obesidade grave"
                
                con.send(classificacao.encode('ascii')) #envia os dados ao cliente 
                print (cliente, "Requisição atendida")
        except OSError as e:
            print ("Erro de socket', {e}")
        finally:
            print(f"Fechando a conexão com {cliente}")
            con.close() 

