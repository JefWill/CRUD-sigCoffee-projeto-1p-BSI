import os
import datetime





def ler_produto(lista_produtos): #verufuca se o produto ta na lista e ta ativo ou inativo
  id_produto = int(input("##### Informe o ID do produto: "))
  if (id_produto in lista_produtos) and (lista_produtos[id_produto]['inativo'] == False):
    return id_produto
  
  elif lista_produtos[id_produto]['inativo'] == True:
    print("##### Produto inativo!")
    input("##### Tecle <ENTER> para continuar...")
    return None

  else:
    print("##### Produto não encontrado!")
    input("##### Tecle <ENTER> para continuar...")
    return None


def verifica_cliente(lista_clientes): #verifica se o cliente ta na lista e ta ativo ou inativo
  id_cliente = (input("##### Informe o ID do cliente: "))
  if (id_cliente in lista_clientes) and (lista_clientes[id_cliente]['inativo'] == False):
    return id_cliente
  
  elif lista_clientes[id_cliente]['inativo'] == True:
    print("##### cliente inativo!")
    input("##### Tecle <ENTER> para continuar...")
    return None

  else:
    print("##### cliente não encontrado!")
    input("##### Tecle <ENTER> para continuar...")
    return None


def ler_quantidade(lista_produtos,id_produto):
   qtd = float(input("##### Quantidade: "))
   if qtd <= lista_produtos[id_produto]['estoque']:
      return qtd
   else:
      print("##### Quantidade em estoque insuficiente!")
      input("##### Tecle <ENTER> para continuar...")
      return None



def menu_pedido():
  os.system('clear')
  print()
  print("############################################")
  print("#####           Módulo Pedido            #####")
  print("############################################")
  print("##### 1 - Realizar Pedido                #####")
  print("##### 2 - Listar Pedidos                 #####")
  print("##### 3 - Listar Pedidos cancedos        #####")
  print("##### 4 - Cancelar Pedido                #####")
  print("##### 0 - Retornar ao Menu Principal     #####")
  op_pedido = input("##### Escolha sua opção: ")
  return op_pedido



def exibir_totais(id, novo_pedido, lista_clientes, lista_produtos):
  os.system('clear')
  print()
  print("##### Pedido realizado com sucesso! #####")
  print("-----------------------------------------")
  print(f"ID do Pedido: {id}")
  print(f"Cliente:      {lista_clientes[novo_pedido['cpf']]['nome']}")
  print(f"Produto:      {lista_produtos[novo_pedido['id_produto']]['nome']}")
  print(f"Quantidade:   {novo_pedido['qtd']}")
  print(f"Valor Total:  R$ {novo_pedido['valor']:.2f}")
  print("-----------------------------------------")
  input("\n##### Tecle <ENTER> para continuar...")



def cadastrar_pedido(lista_pedidos, lista_clientes,lista_produtos):
  os.system('clear')
  print()
  print("############################################")
  print("#####         Realizar Pedido          #####")
  print("############################################")
  print()
  
  cpf = verifica_cliente(lista_clientes)
  if not cpf:
    return

  id_produto = ler_produto(lista_produtos)
  if not id_produto:
    return
  
  qtd = ler_quantidade(lista_produtos,id_produto)
  if not qtd:
    return
  
  if not lista_pedidos:  # Se a lista estiver vazia, começa com 1
      id = 1
  else:
      id = max(lista_pedidos.keys()) + 1  # Pega o maior ID existente e incrementa





  novo_pedido = calcular_pedido(cpf, id_produto, qtd, lista_produtos)

  lista_pedidos[id] = novo_pedido

  exibir_totais(id, novo_pedido, lista_clientes, lista_produtos)



def calcular_pedido(cpf, id_produto, qtd,lista_produtos):
  valor_unitario = lista_produtos[id_produto]['valor']
  valor_total_pedido = qtd * valor_unitario
  
  lista_produtos[id_produto]['estoque'] -= qtd

  data_criacao = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

  pedido = {'cpf': cpf, 'id_produto': id_produto, 'qtd': qtd, 'valor': valor_total_pedido, 'data_criacao': data_criacao}
  return pedido



def cancelar_pedido(lista_pedidos, pedidos_cancelados):
  os.system('clear')
  print()
  print("############################################")
  print("#####         Cancelar Pedido          #####")
  print("############################################")
  print()
  id_pedido = int(input("Informe o ID do pedido que deseja cancelar: "))

  if id_pedido in lista_pedidos:
    resp = input("##### Tem certeza que deseja cancelar o pedido [S/N]? ").upper()
    if resp == 'S':
      cancelado = lista_pedidos.pop(id_pedido)
      cancelado['data_cancelamento'] = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
      pedidos_cancelados[id_pedido] = cancelado
      print("\n##### Pedido cancelado e estoque atualizado com sucesso!")
    else:
      print("\n##### Operação de cancelamento abortada!")
  else:
      print("\n##### Pedido não encontrado!")
  input("##### Tecle <ENTER> para continuar...")


def exibir_pedidos(lista_clientes, lista_produtos, lista_pedidos):
  os.system('clear')
  for id in lista_pedidos:
      cpf = lista_pedidos[id]['cpf']
      print(f"ID do Pedido: {id}")
      print(f"Cliente:      {lista_clientes[cpf]['nome']}")
      print(f"Produto:      {lista_produtos[lista_pedidos[id]['id_produto']]['nome']}")
      print(f"Quantidade:   {lista_pedidos[id]['qtd']}")
      print(f"Valor Total:  R$ {lista_pedidos[id]['valor']:.2f}")
      print(f"Data de Criação: {lista_pedidos[id]['data_criacao']}")
      print("-----------------------------------------")
  input("##### Tecle <ENTER> para continuar...")



def exibir_pedidos_cancelados(pedidos_cancelados, lista_clientes, lista_produtos):
  os.system('clear')
  for id in pedidos_cancelados:
      print(f"ID do Pedido: {id}")
      print(f"Cliente:      {lista_clientes[pedidos_cancelados[id]['cpf']]['nome']}")
      print(f"Produto:      {lista_produtos[pedidos_cancelados[id]['id_produto']]['nome']}")
      print(f"Quantidade:   {pedidos_cancelados[id]['qtd']}")
      print(f"Valor Total:  R$ {pedidos_cancelados[id]['valor']:.2f}")
      print(f"Data de Cancelamento: {pedidos_cancelados[id]['data_cancelamento']}")
      print("-----------------------------------------")
  input("##### Tecle <ENTER> para continuar...")
