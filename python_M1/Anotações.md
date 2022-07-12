# Anotações: Python Mundo 01


## [Anotações aula 04 - primeiros comandos em python 3](https://youtu.be/31llNGKWDdo)

Em python se os dados forem mensagens eles tem delimitadores especiais.

Considerando que a mensagem pode ter diversos caracteres e letras os delimitadores ideias sãos;

- aspas simples
- aspas duplas.

No python todos os comandos são funções e todas as funções deve estar entre parênteses.

Em python toda variavel é considerada um objeto.

Uma variaves pode receber um valor utilizando o sinal de =.

    mensg = 'oi'

### Desafio 01

Crie um script python que leia o nome de uma pessoa e mostre uma mensagem de boas vindas de acordo com o valor digitado.

- [exerc_01.py](exerc_01.py)

### Desafio 02

Crie um script python que leia o dia, o mês e o ano do nascimento de uma pessoa e mostre uma mensagem com a data formatada

- [exerc_02.py](exerc_02.py)

### Desafio 03

Crie um script python que leia dois números e tente mostrar a soma entre eles.

- [exerc_03.py](exerc_03.py)

## [Anotações aula 06 - tipos primitivos e saída de dados](https://youtu.be/hdDHg1p3YVc)

int() = Aceita números inteiros

Ex: 1,2,3,4,5,6,7

    msg = int(input('adicione um número: '))

float() = Aceita números reais

Ex: 4.5, 3.6, 7.8, 9.8

    msg = float(input('adicione um número: ))

bool() = Só aceita dois valores "True" ou "False"

Ex: True, False

    msg = bool(input('adicione um valor: '))

str() = aceita letras e caracteres que estejam apenas entre ('')

Ex: 'oi', '7.5', '??:>:?W'

    msg = srt(input('Informe seu nome: '))

### Desafio 04

Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ele.

- [exerc_04.py](exerc_04.py)

## [Anotações aula 07 - Operadores Aritméticos](https://youtu.be/Vw6gLypRKmY)

|Simbolo|Operador| Exemplos |
|:---:|:----:| :-----: |
|+|Adição| 5 + 5 = 10
|-|Subtração| 5-2 = 3
|*|Multiplicação| 5*5= 25
|/|Divisão|10/2= 5
|**|Potência|5**2= 25
|//|Divisão inteira|5//2= 2
|%|Resto da divisão|5%2= 1

### Ordem de precedência durante as operações.

|Orden|Operador
|:---:|:----:|
|1|()
|2|**
|3|* / // %
|4| + -
