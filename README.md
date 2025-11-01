# Ping Simples e Ping Múltiplo com Biblioteca OS no Python
<p align="center">
  <img src="" alt="Imagem não carregada :(" width="650"/>
</p>

Usando a biblioteca **`os`** do Python para interagir com o sistema operacional e realizar testes de *conectividade de rede* através do comando `ping`.

---

## Resumo

Este arquvio README descreve uma Contextualização breve e geral do código desmonstrado.

1. **Ping Simples** — Pode ser usado para Pingar diretamente um HOST ou IP por vez, escolhendo o número de dísparos de Pacotes para avaliação de tempo de resposta e comunicação entre o Dispositivo Nativo e o Destino final.
2. **Ping Múltiplo** — Possibilita de leitura de Arquivos ( No exemplo, [hosts.txt](./Pings_Códigos/hosts.txt) ),  contendo todos os Hosts a serem testados na Empresa, sendo possível utilizá-lo em rotinas de controle e Teste de Rede.

---

## Índice

1. [Objetivo](#objetivo)  
2. [Ferramentas utilizadas](#ferramentas-utilizadas)  
3. [Conceito: o que é o ping](#conceito-o-que-é-o-ping)  
4. [Descrição](#descrição)  
5. [Códigos](#códigos)

---

## Objetivo

Demonstrar códigos funcionais e realizar testes de conectividade usando Python e a biblioteca `os`, executando o comando `ping` nativo do sistema operacional(Tanto Linux quanto Windows) e proveniete do Protocolo ICMP - "Internet Control Message Protocol".

O objetivo é compreender a interação entre a Linguagem **Python** e o **Sistema Operacional**, além de promover scripts a serem usados em automatizações via Bibliotecas como `schedule` e `time` a automatização de rotinas simples de diagnóstico de rede.

---

## Ferramentas utilizadas

- PyCharm --V 2025.23;
- Pyhton --V 3.12.7;

---

## Conceito: o que é o `ping`

O comando **`ping`** é uma ferramenta de diagnóstico de rede utilizada para verificar a **disponibilidade** e **tempo de resposta** entre dois dispositivos.  
Ele envia pacotes **ICMP Echo Request** para o destino e aguarda respostas **Echo Reply**.  
A partir desses resultados, é possível medir:

- **Latência (tempo de resposta)**;  
- **Perda de pacotes**;  
- **Conectividade geral** entre hosts.

---

## Descrição

- Usa o comando `ping` via `os.system()`;
- Identifica o sistema operacional (Windows ou Linux/macOS);
- Define o parâmetro adequado (`-n` ou `-c`);
- Exibe o resultado no terminal.

## Códigos

[📨 Ping Simples](./Pings_Códigos/pingsimples.py)  
[📦 Ping Múltiplo](./Pings_Códigos/pingmultiplo.py)
