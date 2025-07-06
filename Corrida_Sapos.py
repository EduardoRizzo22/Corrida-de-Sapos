import threading
import random
import time

PISTA = 50
vencedor = None

lock = threading.Lock()

class Sapo(threading.Thread):
    def __init__(self, nome):
        super().__init__()
        self.nome = nome
        self.posicao = 0

    def run(self):
        global vencedor
        while self.posicao < PISTA:
            pulo = random.randint(1, 5)
            self.posicao += pulo
            print(f"{self.nome} pulou {pulo} casas e está na posição {self.posicao}")

            time.sleep(random.uniform(0.1, 0.5))

        with lock:
            if vencedor is None:
                vencedor = self.nome
                print(f"🏆 {self.nome} é o rei da lagoinha!\n")

sapos = [Sapo(f"Sapo {i+1}") for i in range(5)]

print("🐸 Que a corrida dos sapos comecem\n")

# inicia as threads
for sapo in sapos:
    sapo.start()

# espera as thread terminarem 
for sapo in sapos:
    sapo.join()

print("Corrida finalizada, o segundo lugar já pode chorar ;-(")
