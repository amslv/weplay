# WePlay
Sistema de rádio online.
## Setup do ambiente
Instalação do Node.JS para Windows: [aqui](https://nodejs.org/en/download/)

Instalação do Node.JS para Ubuntu e derivados: [aqui](https://www.digitalocean.com/community/tutorials/como-instalar-o-node-js-no-ubuntu-16-04-pt)

## Como executar
Para instalar as dependências da aplicação execute o seguinte comando:

    pip install -r requirements.txt

Em seguida, execute o seguinte comando para setar a variável de ambiente referente a aplicação Flask.

    export FLASK_APP=server.py

Para executar a aplicação execute:

    flask run

Caso esteja utilizando Windows, execute os comandos acima utilizando o **Git Bash**.
