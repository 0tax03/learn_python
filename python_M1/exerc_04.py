# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
# e todas as informações possiveis sobre ele.
from curses.ascii import isspace

msg = int(input('digite algum número: '))

print(f'Isso que você digitou é um {type(msg)} ')
print('Isso contem espaço ?', isspace(msg))