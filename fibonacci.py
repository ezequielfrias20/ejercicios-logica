"""
    Escribe un programa que imprima los 50 primeros números de la sucesión
    de Fibonacci empezando en 0.
    - La serie Fibonacci se compone por una sucesión de números en
    la que el siguiente siempre es la suma de los dos anteriores.
    0, 1, 1, 2, 3, 5, 8, 13...
"""

def fibonacci():
    a1 = 0
    a2 = 1
    for index in range(1,51):
        print(a1)
        sum = a1 + a2
        a1 = a2
        a2 = sum

fibonacci()