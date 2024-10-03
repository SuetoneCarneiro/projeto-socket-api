from cliente import Cliente
import sys

if len(sys.argv) > 2:
    host = sys.argv[1]
    porta = int(sys.argv[2])
else:
    host = '127.0.0.1'
    porta = 9000

cli = Cliente(host, porta)
cli.start()

