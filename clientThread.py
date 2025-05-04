from multiprocessing import Process
from threading import Thread
from time import * 
from random import * 
from socket  import *
from constCS import * 

s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT)) # connect to server (block until accepted)

def sleeping(name):
    

    t = gmtime() #-
    wait = randint(1,20)
    conta = str(randint(0,20)) + ' ' + str(randint(0,20)) + ' ' + geraOp()

    print(str(t.tm_min) + ':' + str(t.tm_sec) + ' '+ name + ': '+ conta + ' | Tempo de espera: ' + str(wait) + ' segundos')
    
    sleep(wait)

    s.send(str.encode(conta))  # send some data
    result = bytes.decode(s.recv(1024)) # receive the response (do servidor)
    t = gmtime()

    print(str(t.tm_min) + ':' + str(t.tm_sec) + ' '+ name + ': '+ conta + ' = ' + result)


def sleeper(number):
    sleeplist = list()

    for i in range(3):
        subsleeper = Thread(target=sleeping, args=('Cliente '  + number + ' - conta ' + str(i+1),))
        sleeplist.append(subsleeper)

    for k in sleeplist: k.start()
    for k in sleeplist: k.join()

def geraOp():
    op = randint(0,2)

    if op == 0:
        return 'add'
    elif op == 1:
        return 'sub'
    else:
        return 'mult'

        
if __name__ == '__main__':
    p = Process(target=sleeper, args=('1',)) 
    q = Process(target=sleeper, args=('2',)) 
    p.start() 
    q.start() 
    p.join()  
    q.join()  

    s.close()