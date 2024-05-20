"""
    Escribe un programa que muestre por consola (con un print) los
    números de 1 a 100 sustituyendo los siguientes:
    - Múltiplos de 3 por la palabra "fizz".
    - Múltiplos de 5 por la palabra "buzz".
    - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""

def fizzbuzz():
    for index in range(1,101):
        multipleByThree = (index % 3) == 0
        multipleByFive = (index % 5) == 0
        if (multipleByFive and multipleByThree):
            print()
        elif (multipleByFive): print('buzz')
        elif (multipleByThree): print('fizz')
        else: print(index)

fizzbuzz()