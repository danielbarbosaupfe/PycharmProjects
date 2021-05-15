# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252

num = int(input("Digite um numero"))
if num < 2: # 0 e 1 não são primos, e vou desconsiderar os números negativos
    print('não é primo')
elif num == 2: # 2 é o único número par que é primo
    print('primo')
elif num % 2 == 0: # se for par e não é 2, não é primo
    print('não é primo')
else: # aqui eu sei que o número é ímpar
    # só testo se é divisível por números ímpares
    for i in range(3, num // 2, 2):
        if num % i == 0:
            print('não é primo')
            break # não é primo, interrompe o for
    else:
        print('é primo')
