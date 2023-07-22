     ### Desafio
     ----
     Criando um fluxo de trabalho
     
     Vamos criar um repositório para este módulo!
     
     - 1-) Crie um repositório para o curso da Ada
     - 2-) Faça o clone desse numa pasta na máquina local
     - 3-) Adicione um README.md descrevendo o repositório
     - 4-) Faça o push desse conteúdo
     
     Na máquina local, crie uma pasta `projetos`
     
     Nela adicione a pasta `calculadora`.
     
     Ficaria dessa forma `<repositorio>/lógica_de_programacao_II/projetos/calculadora`
     
     Crie um arquivo `app.py`
     Crie uma pasta `calculadora`  
     Adicione os seguintes arquivos
     - `__init__.py`
     - `funcoes.py`
     
     Agora iremos criar as seguintes funcionalidades no arquivo `funcoes.py`  
     - soma
     - subtracao
     - divisao
     - multiplicao
     
     No arquivo, `__init__.py`:
     - Importe as funções criadas, p.ex. `from funcoes import soma`
     - Nesse arquivo crie uma funcao `calcule`
     
     Requisitos:
      - soma:
       - aceita dois parâmetros `a`, `b`
       - retorna a soma desses dois números
       - levanta um TypeError se a ou b forem diferentes de `int` e `float`
         - Mensagem: `O input 'a' e 'b' devem ser uma int ou float, recebido {a}, tipo(a), b tipo (b)`
     - subtração:
       - aceita dois parâmetros `a`, `b`
       - retorna a subtração desses dois números
     
     - divisao:
       - aceita dois números `a`, `b`
       - retorna:
         - divisão de a/b se b != 0
         - 0 se b = 0
           - Exibe na tela uma mensagem de erro mencionando uma divisão inválida
       
     - multiplicação:
       - aceita dois números `a`, `b`
       - retorna multiplicação desses dois números
       - levanta um TypeError se a ou b forem diferentes de `int` e `float`
       
     
     Na função `calcule`:  
     - Pede um input de um número -> a
     - Pede um input de um número -> b
     - Pede um input de operação -> opções válidas: 'soma', 'subtracao', 'divisao', 'multiplicacao', '+', '-', '/', '*'
     - Chama a função correspondente ('soma', 'subtracao', 'divisao', 'multiplicacao')
     - Imprime o resultado na tela informando o resultado
     
     -----
     Para testar a funcionalidade:
     
     Adicione no arquivo `app.py`
     ```
     # Importanto a função do arquivo calculadora/__init__.py
     import sys
     import os
     sys.path.insert(0, os.getcwd())
     from projetos.calculadora import calcule
     
     # Executando a aplicação
     calcule()
     
     ```
     
     Execute o código no terminal com `python app.py`
     
     ----
     No arquivo funcoes.py
     ```
     def soma(...):
       pass
     
     def subtracao(...):
       pass
     ...
     ```
     
     No arquivo `__init__.py`
     ```
     def calcule():
       pass
     ```
