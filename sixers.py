#001 Crie um programa que escreva 'Hello, World!' na tela.

# print('Hello, World!')

#002 Faca um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas

# name = input('What is your name? ')
# print(f'Nice to meet you, {name}!')

#003 Crie um programa que leia dois numeros e mostre a soma entre eles.

# num = int(input('Type a number: '))
# num2 = int(input('Type another one: '))
# print(f'The sum between {num} and {num2} is {num + num2}.')

#004 Faca um programa que leia algo pelo teclado e mostre na o seu tipo primitivo e todas as informacoes possiveis sobre ele.

# from curses.ascii import isalnum, isalpha, isupper, isdigit, isstring


# v = input('Type something: ')
# print(f'These value "{v}" is alphanumeric?', isalnum(v))
# print(f'These value "{v} is alpha? ', isalpha(v))
# print(f'These value "{v}" is numeric? ', type(v))

#005 Make a program that reads an integer and show on the screen its successor and predecessor

# num = int(input('Type a number: '))
# print(f'The successor of {num} is {num + 1} and the predecessor is {num - 1}.')

#006 Crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada.

# from math import sqrt


# num = int(input('Type a number: '))
# print(f'The double of the number {num} is {num*2} and the triple is {num*3}. \nThe square root is {sqrt(num):.2f}.')

#007 Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

# f = float(input('Your first grade: '))
# s = float(input('Second grade: '))
# p = f + s
# print(f'You averages {p / 2:.1f}')

#008 Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
#Km Hm Dam M Dm Cm Mm

# m = float(input('Give me a value in meters: '))
# print(f'These value {m}m in Decimeters is {m * 10:.0f}dm \nCentimeters {m * 100:.0f}cm \nMillimeters {m * 1000:.0f}mm')
# print(f'\nDecamters {m / 10}dam \nHectometers {m / 100}hm \nKilometers {m / 1000}km')

#009 Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

# num = int(input('Give a value so i can read in multiplication table: '))
# print('-' * 12)
# print(f'{num} x {1:2} = {num*1}')
# print(f'{num} x {2:2} = {num*2}')
# print(f'{num} x {3:2} = {num*3}')
# print(f'{num} x {4:2} = {num*4}')
# print(f'{num} x {5:2} = {num*5}')
# print(f'{num} x {6:2} = {num*6}')
# print(f'{num} x {7:2} = {num*7}')
# print(f'{num} x {8:2} = {num*8}')
# print(f'{num} x {9:2} = {num*9}')
# print(f'{num} x {10:2} = {num*10}')
# print('-' * 12)

#010 Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

# w = float(input('How much money you have in you wallet? R$'))
# print(f'With {w:.2f} reais you can buy {w / 5.28:.2f} USD.')

#011 Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua area e  quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta
#uma área de 2 metros quadrados

# w = float(input('Type a width: '))
# h = float(input('Type a height: '))
# print(f'Your wall have a dimension of {w}x{h} and the area is {w * h}m². \nTo paint your wall, you are going to need {w * h / 2}l of ink.')

#012 Faça um algoritmo que leia o preço de um produto e mostre o seu novo preço, com 5% de desconto.

# p = float(input('what is the price of the product? R$'))
# r = p * (5/100)
# print(f'The product cost {p} and now with the 5% discount will be {p - r:.2f}.')

#013 Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

# s = float(input('What is the salary of the employee? R$'))
# r = s * (6/100)
# print(f'The salary right now is {s:.2f} but with the 6% increase it is gonna be {s + r:.2f}.')