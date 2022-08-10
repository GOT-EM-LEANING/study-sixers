# import drink  ("import" will be all the stuffs)
# from candy import ("from" will be just a few things, not all the stuffs)
# math
#     ceil "rounding up"
#     floor "rounding down"
#     trunc "forward comma will be truncate" 
#     pow "is the same **"
#     sqrt "square root"
#     factorial "factorial maths"
# from math import  sqrt
# num = int(input('Type a number: '))
# print(f'The square root of {num} is {sqrt(num):.2f}.')

# from random import random, randint
# num = randint(1, 10)
# print(f'The number is... {num}.')

# import emoji
# print(emoji.emojize('Hello, World :earth_americas:', language='alias'))


#Challenge continues
#016 Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira

# from math import trunc
# num = float(input('Type a number: '))
# print(f'The numer {num} had a {trunc(num)} as a whole part.')

#017 Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa.

# from math import hypot
# oside = int(input('The opposite side: '))
# aside = int(input('The ajacent side: '))
# print(f'The lenght of opposite side is {oside} and the adjacent side {aside} so the hypotenusa lenghts is {hypot(oside, aside):.2f}')


#018 Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo.

# from math import sin, cos, tan
# a = int(input('Type an angle: '))
# print(f'The angle: {a} \nThe sine: {sin(a):.2f} \nThe cosine: {cos(a):.2f} \nThe tangent: {tan(a):.2f}')

#019 Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

from random import choice
fs = input('First student: ')
st = input('Second student: ')
ts = input('Third student: ')
ffs = input('Fourth student: ')
r = (fs, st, ts, ffs )
print(f'The chosen one to clear the board was {choice(r)}. Got clean it now!')


#020 O mesmo professor do desafio anterior quer sortear a ordem da apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro e mostre a ordem sorteada.

