import os #Importa a Biblioteca os que integra os programas e recursos do S.O

print("#" * 60) #Impressão # * 60

ip_ou_host = input("Digite o host a ser verificado: ") #variável recebendo o ping/host
print("-" * 60) #Impressão # * 60
os.system('ping -n 6 {}'.format(ip_ou_host)) #Usando metodo system da biblioteca OS
#para uso do pin com disparo de 6 pacotes.