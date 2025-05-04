DESCRIÇÃO DO SISTEMA

Lado do Cliente (client.py):
    Cada processo representa um cliente que tem 3 threads associados a ele, sendo cada thread uma conta que se deseja efetuar. A cada conta que o cliente deseja efetuar é sorteado um número de 1 a 20 para ser o tempo de espera em segundos para a conta ser enviada para o servidor
Lado do Servidor (server.py):
    Cada requsição é tratada por uma thread que efetua a conta recebida do cliente