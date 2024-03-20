""""
1) Observe o trecho de código abaixo:

int INDICE = 13, SOMA = 0, K = 0;

enquanto K < INDICE faça

{

K = K + 1;

SOMA = SOMA + K;

}

imprimir(SOMA);

Ao final do processamento, qual será o valor da variável SOMA?

Resposta:

    O trecho do código está descrevendo um loop (do tipo while) que tem a função de incrementar o valor de K
    sempre que a condição K < INDICE for verdadeira.

    Inicialmente, foram definidos os valores sendo:

    INDICE = 13
    SOMA = 0
    K = 0

    Isso faz com que a condição do loop while seja verdadeira até que K seja incrementado ao valor 13.

    Considerando que K é incrementado em 1 e somado ao valor *atual* da SOMA, esse programa descreve basicamente,
    a soma dos números naturais de 1 a 13.

    ou seja:

    SOMA = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12 + 13

    Tendo como resultado: 91 (INT)


"""

# Exemplo prático, porém personalizado do programa em questão:

print(50*'-')
print('ESTE PROGRAMA CALCULA A SOMA DE NÚMEROS NATURAIS!')
print(50*'-')

I = int(input('Digite o índice que deseja calcular: '))

# Counter
K = 0

# Soma
S = 0

while K < I:

    K += 1

    S += K

print('A soma dos números naturais de 0 à {} é de \033[1;32m{}'.format(I,S))

# Se realizar os testes, vai perceber que a resposta, considerando o índice 13 é 91.
# Sinta-se à vontade para testar outros índices.




