# 🍎📅 NutrIF 
Projeto desenvolvido na disciplina de <strong>Protocolos de Interconexões de Redes de Computadores</strong> do curso de Sistemas para Internet do IFPB, ministrada pelo professor Leonidas Lima. Esse projeto tem o cunho de produzir uma aplicação usando API de Sockets para uma clínica de nutricionistas.


* 1. [🔧 Funcionalidades/Protocolo de aplicação](#-funcionalidadesprotocolo-de-aplicação)
        * [1.1 📱 Calcular IMC ](#1--calcular-imc)
        * [1.2 👥 Cadastrar na Fila de Espera](#2--cadastrar-na-fila-de-espera)
        * [1.3 ⏳ Ver posição na Fila de Espera](#3--ver-posição-na-fila-de-espera)
        * [1.4 💌 Mensagens do protocolo](#4--mensagens-do-protocolo)
* 2. [📂 Arquivos do projeto](#-arquivos-do-projeto)
* 3. [🐍 Pré-requisitos para execução](#-pré-requisitos-para-execução)
* 4. [📖 Instruções para execução](#-instruções-para-execução)
* 5. [⭐ Autores](#-autores)

## 🔧 Funcionalidades/Protocolo de aplicação

### 1. 📱 Calcular IMC
   - **Descrição:** Ao digitar o número `1`, a função `Calcular IMC` é a responsável por realizar o cálculo do índice de massa corporal do usuário. Ela requisita o `peso em kg` e a `altura em cm` do usuário, realizando o cálculo e `retornando uma classificação`.
   - **Exemplos de classificações:**
     - "Abaixo do peso"
     - "Peso normal"
     - "Sobrepeso"
     - "Obesidade"
     - "Obesidade grave"

### 2. 👥 Cadastrar na Fila de Espera
   - **Descrição:** Ao digitar o número `2`, a função `Cadastrar na Fila de Espera` é a responsável por realizar o cadastro dos usuários, requerindo seus `nomes` e os seus respectivos `telefones` e colocando-os arquivo `fila_espera.txt`.
   
### 3. ⏳ Ver posição na Fila de Espera
   - **Descrição:** Ao digitar o número `3`, a função `Ver posição na Fila de Espera` é a responsável por realizar a consulta do índice do cadastro realizado anteriormente, pedindo o `nome` e `telefone`, retornando como a `posição` que o usuário se encontra.

### 4. 💌 Mensagens do protocolo
  - **Descrição:** Assim como nos protocolos estudados na disciplina, o nosso protocolo conta com mensagens padrão para confirmar a conexão, a realização de operações e o fechamento de conexão entre as partes da aplicação. Veja no quadro a seguir a descrição das mensagens:

|  Mensagem              |Significado                          |
|------------------------|-------------------------------------|
| *LSL-OK* | Confirmação de conexão entre cliente e servidor        | 
| *CONF-X*         |Confirmação de fechamento de conexão         |  
| *#ERRO-CLI#*          |Indica que o cliente inseriu dados inválidos no cálculo de IMC|
|*CONF-CAD*          | Indica confirmação de um cadastro|

Além disso, temos também as mensagens de resposta com as operações relizadas no servidor:
- SUA_POSICAO|Você está na posição {posicao}
- NAO_ENCONTRADO|Você não está na lista de espera.
- IMC_RESULTADO|{classificacao}

*Obs.: O que está entre chaves '{}' é calculado e devolvido pelo servidor*

## 📂 Arquivos do projeto
```
projeto-socket-api/
│
├── Cliente/
│      ├── cliente.py
│      └── main.py
├── Servidor/
│      ├── servidor.py
│      └── main.py
└── README.md

```

## 🐍 Pré-requisitos para execução
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)


## 📖 Instruções para execução
1. Clone e abra o projeto na sua IDLE:
    ```
     git clone https://github.com/SuetoneCarneiro/projeto-socket-api.git
    ```
2. Em seu terminal, execute o comando para rodar o servidor:
    ```
    python Servidor/main.py
    ```
3. Abra outro terminal e execute o comando seguinte para rodar o cliente:
    ```
    python Cliente/main.py
    ```
4. Você pode também rodar o cliente passando como parâmetros o IP e a porta do servidor:
    ```
    python Cliente/main.py 192.168.0.X 9000
    ```

  *Obs.: em sistemas operacionais Linux/mac, troque `python` por `python3`*


## ⭐ Autores
<table>
  <tr>
   <td align="center">
      <a href="https://github.com/leticiazlopes" title="gitHub">
        <img src="https://avatars.githubusercontent.com/u/129249488?v=4" width="100px;" alt="Foto de Letícia Lopes"/><br>
        <sub>
          <b>Letícia Lopes</b>
          <hr>
          <p>leticia.lima.3@academico.ifpb.edu.br</p>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/lailaaquino" title="gitHub">
        <img src="https://avatars.githubusercontent.com/u/140646861?v=4" width="100px;" alt="Foto de Laila"/><br>
        <sub>
          <b>Laila Aquino</b>
          <hr>
          <p>aquino.laila@academico.ifpb.edu.br</p>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/suetonecarneiro" title="gitHub">
        <img src="https://avatars.githubusercontent.com/u/148480989?v=4" width="100px;" alt="Foto de Suetone"/><br>
        <sub>
          <b>Suetone Carneiro</b>
          <hr>
          <p>suetone.neto@academico.ifpb.edu.br</p>
        </sub>
      </a>
    </td>
  </tr>
</table>

