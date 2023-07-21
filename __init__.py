from funcoes import *

def calcule():
    cond1, cond2 = False, False
    while True:
      a = input('Digite o primeiro número: ')
      try:
        a = float(a)
        break
      except ValueError:
        print('Digite um valor inteiro ou float para o primeiro número!')

    while True:
      b = input('Digite o segundo número: ')
      try:
        b = float(b)
        break
      except ValueError:
        print('Digite um valor inteiro ou float para o segundo número!')

      
    oper = input('Digite a operação desejada [soma, subtracao, divisao, multiplicacao, +, -, /, *]: ')
    if oper == 'soma' or oper == '+':
      soma(a, b)
    elif oper == 'subtracao' or oper == '-':
      sub(a, b)
    elif oper == 'divisao' or oper == '/':
      div(a, b)
    elif oper == 'multiplicacao' or oper == '*':
      mult(a, b)