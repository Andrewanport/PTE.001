""""
5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:

a) Essa string pode ser informada através de qualquer entrada de sua preferência
   ou pode ser previamente definida no código;

b) Evite usar funções prontas, como, por exemplo, reverse;

"""

A1 = input('Digite uma frase qualquer: ').strip()

A2 = A1.split()

T = ' '.join(A2)

I = ''

for x in range((len(T) - 1), -1, -1):

    # (len(T) - 1)     : Representa o último caractere da String (T).
    # -1               : Representa o penúltimo índice do fim da sequência, já que a mesma deve terminar em 0.
    # -1               : Representa o passo da sequência, neste caso subtraindo 1 do anterior a cada passo.

    I += T[x]

print('O inverso de {} é {}'.format(A1,I))

