import os
import time

with open('hosts.txt') as file: #abre como arquivo
    dump = file.read() #realiza leitura do arquivo
    dump = dump.splitlines() #split reconhece diferentes quebras de linha do arquivo

    for ip in dump:
        print('Verificando o ip: ', ip)
        print('-' * 68)
    os.system('ping -n 2 {}'.format(ip))
    print('-' * 60)
    time.sleep(5) #usa a biblioteca Time para mudar o tempo de execução ao decorrer do laço de repetição