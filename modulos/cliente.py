import os
def exibir_cliente(lista_clientes):
  os.system('clear')
  print()
  print("############################################")
  print("#####    Exibir clientes cadastrados   #####")
  print("############################################")
  print()
  # Cabeçalho com colunas de tamanho fixo
  print("## " + "CPF".ljust(14) + " | " + "Nome".ljust(25) + " | " + "Telefone".ljust(15) + " | " + "Email".ljust(30) + "##")
  print("## " + "-"*14 + " | " + "-"*25 + " | " + "-"*15 + " | " + "-"*30 + "##")

  for cpf, cliente in lista_clientes.items():
      nome = cliente['nome']
      email = cliente['email']
      # Limita o tamanho do nome e email para não quebrar a interface
      if len(nome) > 25:
          nome = nome[:22] + "..."
      if len(email) > 30:
          email = email[:27] + "..."
      
      print("## " + cpf.ljust(14) + " | " + nome.ljust(25) + " | " + cliente['fone'].ljust(15) + " | " + email.ljust(30) + "##")
  print()
  input("Tecle <ENTER> para continuar...")


def exibir_cliente_inativo(lista_clientes):
  os.system('clear')
  print()
  print("############################################")
  print("#####    Exibir clientes inativos      ####")
  print("############################################")
  print()
  # Cabeçalho com colunas de tamanho fixo
  print("## " + "CPF".ljust(14) + " | " + "Nome".ljust(25) + " | " + "Telefone".ljust(15) + " | " + "Email".ljust(30) + "##")
  print("## " + "-"*14 + " | " + "-"*25 + " | " + "-"*15 + " | " + "-"*30 + "##")

  for cpf, cliente in lista_clientes.items():
      nome = cliente['nome']
      email = cliente['email']
      # Limita o tamanho do nome e email para não quebrar a interface
      if len(nome) > 25:
          nome = nome[:22] + "..."
      if len(email) > 30:
          email = email[:27] + "..."
      if cliente['inativo'] == True:
        print("## " + cpf.ljust(14) + " | " + nome.ljust(25) + " | " + cliente['fone'].ljust(15) + " | " + email.ljust(30) + "##")
  print()
  input("Tecle <ENTER> para continuar...")




def alterar_cliente(lista_clientes):
  os.system('clear')
  print()
  print("############################################")
  print("#####     Altera Dados do cliente      #####")
  print("############################################")
  print()
  cpf = input("Informe o CPF do cliente: ")
  if cpf in lista_clientes:
      print("Informe os novos dados do produto: ")
      nome = input("##### Nome: ")
      print()
      fone = input("##### Número de telefone: ")
      print()
      email = input("##### Email do cliente: ")
      print()
      lista_clientes[cpf] = {
      'nome': nome,
      'fone': fone,
      'email': email
      }
      print("Cliente alterado com sucesso!")
  else:
      print("Cliente inexistente!")
  input("Tecle <ENTER> para continuar...")



def inativar_cliente(lista_clientes):
  os.system('clear')
  print()
  print("############################################")
  print("#####         inativar cliente         #####")
  print("############################################")
  print()
  cpf = input("Informe o cpf do cliente: ")
  if cpf in lista_clientes and lista_clientes[cpf]['inativo'] == False:
      print("cliente encontrado!")
      print("Nome:", lista_clientes[cpf]['nome'])
      resp = input("Tem certeza que deseja inativar o cliente [S/N]? ")
      if resp.upper() == 'S':
        lista_clientes[cpf]['inativo'] = True
        print("cliente inativado com sucesso!")
      else:
        print("inativação não realizada!")
  elif cpf in lista_clientes and lista_clientes[cpf]['inativo'] == True:
    print("cliente já inativo!")
    resp = input("deseja ativar o cliente [S/N]?")
    if resp.upper() == 'S':
      lista_clientes[cpf]['inativo'] = False
      print("cliente ativado com sucesso!")
    
  else:
      print("cliente inexistente!")
  input("Tecle <ENTER> para continuar...")



def menu_cliente():
  os.system('clear')
  print()
  print("############################################")
  print("#####           Módulo Cliente           #####")
  print("############################################")
  print("##### 1 - Cadastrar cliente              #####")
  print("##### 2 - Exibir Dados do cliente        #####")
  print("##### 3 - Alterar Dados do cliente       #####")
  print("##### 4 - inativar cliente                #####")
  print("##### 0 - Retornar ao Menu Principal   #####")
  op_cliente = input("##### Escolha sua opção: ")
  return op_cliente



def ler_cpf(lista_clientes): ##verifica se o cpf está na lista de clientes
  cpf = input("##### Informe o CPF do cliente: ")
  if cpf in lista_clientes:
    return cpf
  else:
    print("##### Cliente não encontrado! Cadastre o cliente primeiro.")
    input("##### Tecle <ENTER> para continuar...")
    return None



def cadastrar_cliente(lista_clientes): #cadastra o cliente no dicionário lista_clientes
  os.system('clear')
  print()
  print("############################################")
  print("#####       cadastrar cliente          #####")
  print("############################################")
  print()
  cpf = input("##### Informe o cpf do cliente: ")
  nome = input("##### Nome do cliente: ")
  print()
  fone = input("##### Telefone do cliente: ")
  print()
  email = input("##### Email do cliente: ")
  print()
  lista_clientes[cpf] = {
      'nome': nome,
      'fone': fone,
      'email': email
  }
  print("Cliente cadastrado com sucesso!")
  input("Tecle <ENTER> para continuar...")


