import socket
import threading

class Servidor:
    def __init__(self, host, porta) -> None:
        self._host = host
        self._porta = porta
        self._tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._threads = {}

    def start(self):
        '''
        Inicia a execução do servidor
        '''
        servidor = (self._host, self._porta)
        try:
            self._tcp.bind(servidor)
            self._tcp.listen(5)
            print('O servidor foi iniciado em ', self._host, ':', self._porta)
            
            while True:
                con, cliente = self._tcp.accept()
                print(f"Cliente {cliente} conectado.")
                con.send(bytes("\nLSL-OK\n", 'ascii'))
                self._threads[cliente] = threading.Thread(target=self._servico, args=(con, cliente))
                self._threads[cliente].start()  # comando não bloqueante
        except Exception as e:
            print('Erro ao inicializar o servidor ', e.args)

    def _servico(self, con, cliente):
        '''
        Implementa o serviço de calculadora de IMC
        '''
        try:  

            while True:
                dados = con.recv(1024).decode('ascii').strip()  # Recebe dados do cliente
                if not dados:
                    break
                
                print(f"Recebido de {cliente}: {dados}")

                # Processa o comando recebido
                if dados.startswith("CALCULO_IMC"):
                    self._processar_imc(dados, con)
                elif dados.startswith("CADASTRAR"):
                    self._processar_cadastro(dados, con)
                elif dados.startswith("VER_POSICAO"):
                    _, valores = dados.split('|')
                    nome, telefone = valores.split(',')
                    posicao = self._buscar_posicao_na_fila(nome, telefone)
                    if posicao is not None:
                        con.send(bytes(f"\nSUA_POSICAO|Você está na posição {posicao}.\n", 'utf-8'))
                    else:
                        con.send(bytes("NAO_ENCONTRADO|Você não está na lista de espera.\n", 'utf-8'))
                elif dados == "ENCERRAR":
                    print(f"Cliente {cliente} encerrou a conexão.")
                    break

        except OSError as e:
            print("Erro de socket:", e)
        finally:
            print(f"Fechando a conexão com {cliente}")
            con.send(bytes('\nCONF-X\n', 'ascii')) # Mensagem de encerramento confirmado
            con.close()


    def _processar_imc(self, dados, con):
        '''
        Processa o cálculo do IMC e envia o resultado ao cliente
        '''
        _, valores = dados.split('|')
        check = valores.split(',')
        if check[0].isnumeric() and check[1].isnumeric():
            peso, altura = map(float, valores.split(','))
            altura_f = altura / 100
            imc = peso / (altura_f ** 2)

            # Classifica o IMC
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

            # Envia o resultado ao cliente
            con.send(bytes(f"\nIMC_RESULTADO|{classificacao}\n", 'ascii'))  # Inclui quebra de linha
        else:
            con.send(bytes("\n#ERRO-CLI#\n", 'ascii'))

    def _processar_cadastro(self, dados, con):
        '''
        Processa o cadastro de um cliente na fila de espera e envia a confirmação
        '''
        _, valores = dados.split('|')
        nome, telefone = valores.split(',')

        # Cadastra na fila de espera
        with open('fila_espera.txt', 'a') as f:
            f.write(f"{nome},{telefone}\n")

        # Envia a confirmação ao cliente
        con.send(bytes('\nCONF-CAD', 'ascii'))
        
    def _buscar_posicao_na_fila(self, nome, telefone):
        '''
        Função que busca a posição de um cliente na fila de espera com base no nome e telefone
        '''
        try:
            with open('fila_espera.txt', 'r') as f:
                lista = f.readlines()

            for idx, linha in enumerate(lista):
                nome_fila, telefone_fila = linha.strip().split(',')
                if nome_fila == nome and telefone_fila == telefone:
                    return idx + 1  # Posições começam em 1

            return None  # Retorna None se o cliente não for encontrado
        except FileNotFoundError:
            return None

