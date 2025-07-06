import threading
import random
import time
import os

TAMANHO_PISTA = 50
vencedor = None
lock = threading.Lock()

# Limpa a tela do terminal
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

class Sapo(threading.Thread):
    def __init__(self, nome, posicoes):
        super().__init__()
        self.nome = nome
        self.posicao = 0
        self.posicoes = posicoes  # Lista compartilhada para atualizar visualmente

    def run(self):
        global vencedor
        while self.posicao < TAMANHO_PISTA:
            pulo = random.randint(1, 5)
            self.posicao += pulo
            if self.posicao > TAMANHO_PISTA:
                self.posicao = TAMANHO_PISTA

            self.posicoes[self.nome] = self.posicao
            time.sleep(random.uniform(0.1, 0.3))

        with lock:
            if vencedor is None:
                vencedor = self.nome

def mostrar_corrida(posicoes):
    limpar_tela()
    print("🐸 Corrida dos Sapos 🐸\n")
    for nome, pos in posicoes.items():
        pista = "-" * pos + "🐸" + "-" * (TAMANHO_PISTA - pos)
        print(f"{nome}: {pista}")

# Lista de sapos
nomes = [f"Sapo {i+1}" for i in range(5)]
posicoes = {nome: 0 for nome in nomes}

# Criar threads dos sapos
sapos = [Sapo(nome, posicoes) for nome in nomes]

# Inicia as threads
for sapo in sapos:
    sapo.start()

# Loop de visualização da corrida
while any(sapo.is_alive() for sapo in sapos):
    mostrar_corrida(posicoes)
    time.sleep(0.1)

# Aguarda todas as threads terminarem
for sapo in sapos:
    sapo.join()

# Mostrar resultado final
mostrar_corrida(posicoes)
print(f"\n🏁 Corrida finalizada! O vencedor foi: {vencedor} 🏆\n")
