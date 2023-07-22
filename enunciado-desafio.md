     ### Desafio
     ----
     Criando um fluxo de trabalho
     
     Vamos criar um reposit�rio para este m�dulo!
     
     - 1-) Crie um reposit�rio para o curso da Ada
     - 2-) Fa�a o clone desse numa pasta na m�quina local
     - 3-) Adicione um README.md descrevendo o reposit�rio
     - 4-) Fa�a o push desse conte�do
     
     Na m�quina local, crie uma pasta `projetos`
     
     Nela adicione a pasta `calculadora`.
     
     Ficaria dessa forma `<repositorio>/l�gica_de_programacao_II/projetos/calculadora`
     
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
     - Importe as fun��es criadas, p.ex. `from funcoes import soma`
     - Nesse arquivo crie uma funcao `calcule`
     
     Requisitos:
      - soma:
       - aceita dois par�metros `a`, `b`
       - retorna a soma desses dois n�meros
       - levanta um TypeError se a ou b forem diferentes de `int` e `float`
         - Mensagem: `O input 'a' e 'b' devem ser uma int ou float, recebido {a}, tipo(a), b tipo (b)`
     - subtra��o:
       - aceita dois par�metros `a`, `b`
       - retorna a subtra��o desses dois n�meros
     
     - divisao:
       - aceita dois n�meros `a`, `b`
       - retorna:
         - divis�o de a/b se b != 0
         - 0 se b = 0
           - Exibe na tela uma mensagem de erro mencionando uma divis�o inv�lida
       
     - multiplica��o:
       - aceita dois n�meros `a`, `b`
       - retorna multiplica��o desses dois n�meros
       - levanta um TypeError se a ou b forem diferentes de `int` e `float`
       
     
     Na fun��o `calcule`:  
     - Pede um input de um n�mero -> a
     - Pede um input de um n�mero -> b
     - Pede um input de opera��o -> op��es v�lidas: 'soma', 'subtracao', 'divisao', 'multiplicacao', '+', '-', '/', '*'
     - Chama a fun��o correspondente ('soma', 'subtracao', 'divisao', 'multiplicacao')
     - Imprime o resultado na tela informando o resultado
     
     -----
     Para testar a funcionalidade:
     
     Adicione no arquivo `app.py`
     ```
     # Importanto a fun��o do arquivo calculadora/__init__.py
     import sys
     import os
     sys.path.insert(0, os.getcwd())
     from projetos.calculadora import calcule
     
     # Executando a aplica��o
     calcule()
     
     ```
     
     Execute o c�digo no terminal com `python app.py`
     
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
