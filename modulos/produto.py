import os

def exibir_produtos(lista_produtos): ### Créditos: GEMINI --- formatação do relatório
  os.system('clear')
  print()
  print("############################################")
  print("#####    Exibir produtos cadastrados   #####")
  print("############################################")
  print()
  # Cabeçalho com colunas de tamanho fixo usando ljust (alinhar à esquerda) e rjust (alinhar à direita)
  print("## " + "ID".ljust(4) + " | " + "Nome".ljust(20) + " | " + "Valor".rjust(10) + " | " + "Estoque".rjust(10) + "##")
  print("## " + "-"*4 + " | " + "-"*20 + " | " + "-"*10 + " | " + "-"*10 + "##")
  
  for id, produto in lista_produtos.items():
      nome = produto['nome']
      # Limita o tamanho do nome para não quebrar a interface
      if len(nome) > 20:
          nome = nome[:17] + "..."

      # Converte tudo para string e alinha nas colunas
      print("## " + str(id).ljust(4) + " | " + nome.ljust(20) + " | " + str(produto['valor']).rjust(10) + " | " + str(produto['estoque']).rjust(10) + "##")
      
  print()
  input("Tecle <ENTER> para continuar...")


def exibir_produtos_inativos(lista_produtos): ### Créditos: GEMINI --- formatação do relatório
  os.system('clear')
  print()
  print("############################################")
  print("#####    Exibir produtos inativos      #####")
  print("############################################")
  print()
  # Cabeçalho com colunas de tamanho fixo usando ljust (alinhar à esquerda) e rjust (alinhar à direita)
  print("## " + "ID".ljust(4) + " | " + "Nome".ljust(20) + " | " + "Valor".rjust(10) + " | " + "Estoque".rjust(10) + "##")
  print("## " + "-"*4 + " | " + "-"*20 + " | " + "-"*10 + " | " + "-"*10 + "##")
  
  for id, produto in lista_produtos.items():
      nome = produto['nome']
      # Limita o tamanho do nome para não quebrar a interface
      if len(nome) > 20:
          nome = nome[:17] + "..."
      if produto['inativo'] == True: #verifica se o produto ta inativo
        # Converte tudo para string e alinha nas colunas
        print("## " + str(id).ljust(4) + " | " + nome.ljust(20) + " | " + str(produto['valor']).rjust(10) + " | " + str(produto['estoque']).rjust(10) + "##")
      
  print()
  input("Tecle <ENTER> para continuar...")



def alterar_produto(lista_produtos): #altera todos os dados do produto do zero
  os.system('clear')
  print()
  print("############################################")
  print("#####     Altera Dados do produto      #####")
  print("############################################")
  print()
  id = int(input("Informe o id do produto: "))
  if id in lista_produtos:
      print("Informe os novos dados do produto: ")
      nome = input("##### Nome: ")
      print()
      valor = float(input("##### Valor do produto: "))
      print()
      estoque = float(input("##### Quantidade em estoque: "))
      print()
      lista_produtos[id] = {
      'nome': nome,
      'valor': valor,
      'estoque': estoque
      }
      print("produto alterado com sucesso!")
  else:
      print("produto inexistente!")
  input("Tecle <ENTER> para continuar...")



def inativar_produto(lista_produtos):
  os.system('clear')
  print()
  print("############################################")
  print("#####         inativa produto           #####")
  print("############################################")
  print()
  id = int(input("Informe o id do produto: "))
  if id in lista_produtos and lista_produtos[id]['inativo'] == False:
      print("Produto encontrado!")
      print("Nome:", lista_produtos[id]['nome'])
      resp = input("Tem certeza que deseja inativar o produto [S/N]? ")
      if resp.upper() == 'S':
       lista_produtos[id]['inativo'] = True
       print("produto inativado com sucesso!")
      else:
        print("Exclusão não realizada!")
  elif id in lista_produtos and lista_produtos[id]['inativo'] == True:
    print("produto já inativo!")
    resp = input("deseja ativar o produto [S/N]?")
    if resp.upper() == 'S':
      lista_produtos[id]['inativo'] = False
      print("produto ativado com sucesso!")
    
  else:
      print("produto(a) inexistente!")
  input("Tecle <ENTER> para continuar...")



def menu_produto():
  os.system('clear')
  print()
  print("############################################")
  print("#####           Módulo produto         #####")
  print("############################################")
  print("##### 1 - Cadastrar produto            #####")
  print("##### 2 - Exibir Dados do produto      #####")
  print("##### 3 - Alterar Dados do produto     #####")
  print("##### 4 - inativar produto              #####")
  print("##### 0 - Retornar ao Menu Principal   #####")
  op_produto = input("##### Escolha sua opção: ")
  return op_produto







def cadastrar_produto(lista_produtos):
  os.system('clear')
  print()
  print("############################################")
  print("#####         Cadastra Produto         #####")
  print("############################################")
  id = max(lista_produtos.keys()) + 1 
  nome = input("##### Nome do produto: ")
  print()
  valor = float(input("##### Valor do produto: "))
  print()
  estoque = float(input("##### Quantidade em estoque: "))
  print()
  lista_produtos[id] = {
      'nome': nome,
      'valor': valor,
      'estoque': estoque
  }
  print("Produto cadastrado com sucesso!")
  input("Tecle <ENTER> para continuar...")

