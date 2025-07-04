# 🐸 Corrida dos Sapos – Programação Concorrente

Este projeto é um **toy program** (programa brinquedo) usado para demonstrar **conceitos de programação concorrente** com threads em Python. A proposta é simular uma **corrida entre sapos**, onde cada sapo é representado por uma thread.

## 🎯 Objetivo

Demonstrar:
- Criação de threads com Python (`threading.Thread`)
- Execução concorrente de múltiplas tarefas
- Uso de **`Lock`** para **exclusão mútua**
- Controle de condição de vitória com segurança de concorrência

## ⚙️ Como funciona

- Cada sapo pula uma distância aleatória (1 a 5 casas).
- A corrida ocorre até que um dos sapos atinja o fim da pista.
- O primeiro a chegar vence.
- O uso de `threading.Lock` garante que apenas **um** sapo seja declarado vencedor.

## 🧪 Execução

### ✅ Requisitos

- Python 3.6 ou superior

### ▶️ Executar

```bash
python corrida_sapos.py
