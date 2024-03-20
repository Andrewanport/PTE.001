""""
 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores
 anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...).

 Escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne
 uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE:

Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código
"""

N = int(input('Digite um número inteiro para verificar sua presença na sequência de Fibonacci: '))

# Inicializa valores dos primeiros números da sequência
A, B = 0, 1

while B < N:

    # Valor do próximo número da sequência
    C = A + B

    # Atualiza os valores para os próximos da sequência
    A = B
    B = C

# Verificação
if B == N:
    print('\033[1;32mO número {} pertence à sequência de Fibonacci!'.format(N))
    quit()

else:
    print('\033[1;31mO número {} NÃO pertence à sequência de Fibonacci!'.format(N))
    quit()
