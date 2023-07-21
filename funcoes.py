def soma(a, b):
    result = a + b
    print('*'*50)
    print(f'A soma de {a} + {b} = {result}')
    print('*'*50)
    return result

def sub(a, b):
    result = a - b
    print('*'*50)
    print(f'A subtração de {a} - {b} = {result}')
    print('*'*50)
    return result

def div(a, b):
    if b == 0:
      print('*'*50)
      print(f'Divisão inválida! O divisor (b) não pode ser igual a zero.')
      print('*'*50)
    else:
      result = a / b
      print('*'*50)
      print(f'A divisão de {a} / {b} = {result}')
      print('*'*50)
      return result

def mult(a, b):
    result = a * b
    print('*'*50)
    print(f'A multiplicação de {a} * {b} = {result}')
    print('*'*50)
    return result
