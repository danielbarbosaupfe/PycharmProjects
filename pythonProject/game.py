#Aprimorado do livro:
#Mike McGrath
#Coding for Beginners
#Alteracoes Daniel Barbosa (Web09)
#2021-05-14
import random
num=(random.randint(1, 5))
#Num e o numero secreto
flag=True
print('Guess my number 1-5: ', end='')

while flag == True:
    guess=input()
    if not guess.isdigit():
        guess=0
        print('Invalid! Enter only digits 1-5')

    if int(guess) < num:
        print('Too low try again:', end='')
    elif int(guess)>num:
        print('To hight, try again', end='')
    else:
        print('Correct.. My number is', guess)
        flag = False



